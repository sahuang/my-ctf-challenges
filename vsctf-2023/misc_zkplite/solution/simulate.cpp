#include <bits/stdc++.h>
using namespace std;

class Keccak256 final {
	public: static constexpr int HASH_LEN = 32;
	private: static constexpr int BLOCK_SIZE = 200 - HASH_LEN * 2;
	private: static constexpr int NUM_ROUNDS = 24;
	public: static void getHash(const std::uint8_t msg[], std::size_t len, std::uint8_t hashResult[HASH_LEN]);
	private: static void absorb(std::uint64_t state[5][5]);
	// Requires 0 <= i <= 63
	private: static std::uint64_t rotl64(std::uint64_t x, int i);
	Keccak256() = delete;  // Not instantiable
	private: static const unsigned char ROTATION[5][5];

};

void Keccak256::getHash(const uint8_t msg[], size_t len, uint8_t hashResult[HASH_LEN]) {
	assert((msg != nullptr || len == 0) && hashResult != nullptr);
	uint64_t state[5][5] = {};

	// XOR each message byte into the state, and absorb full blocks
	int blockOff = 0;
	for (size_t i = 0; i < len; i++) {
		int j = blockOff >> 3;
		state[j % 5][j / 5] ^= static_cast<uint64_t>(msg[i]) << ((blockOff & 7) << 3);
		blockOff++;
		if (blockOff == BLOCK_SIZE) {
			absorb(state);
			blockOff = 0;
		}
	}

	// Final block and padding
	{
		int i = blockOff >> 3;
		state[i % 5][i / 5] ^= UINT64_C(0x01) << ((blockOff & 7) << 3);
		blockOff = BLOCK_SIZE - 1;
		int j = blockOff >> 3;
		state[j % 5][j / 5] ^= UINT64_C(0x80) << ((blockOff & 7) << 3);
		absorb(state);
	}

	// Uint64 array to bytes in little endian
	for (int i = 0; i < HASH_LEN; i++) {
		int j = i >> 3;
		hashResult[i] = static_cast<uint8_t>(state[j % 5][j / 5] >> ((i & 7) << 3));
	}
}

void Keccak256::absorb(uint64_t state[5][5]) {
	uint64_t (*a)[5] = state;
	uint8_t r = 1;  // LFSR
	for (int i = 0; i < NUM_ROUNDS; i++) {
		// Theta step
		uint64_t c[5] = {};
		for (int x = 0; x < 5; x++) {
			for (int y = 0; y < 5; y++)
				c[x] ^= a[x][y];
		}
		for (int x = 0; x < 5; x++) {
			uint64_t d = c[(x + 4) % 5] ^ rotl64(c[(x + 1) % 5], 1);
			for (int y = 0; y < 5; y++)
				a[x][y] ^= d;
		}

		// Rho and pi steps
		uint64_t b[5][5];
		for (int x = 0; x < 5; x++) {
			for (int y = 0; y < 5; y++)
				b[y][(x * 2 + y * 3) % 5] = rotl64(a[x][y], ROTATION[x][y]);
		}

		// Chi step
		for (int x = 0; x < 5; x++) {
			for (int y = 0; y < 5; y++)
				a[x][y] = b[x][y] ^ (~b[(x + 1) % 5][y] & b[(x + 2) % 5][y]);
		}

		// Iota step
		for (int j = 0; j < 7; j++) {
			a[0][0] ^= static_cast<uint64_t>(r & 1) << ((1 << j) - 1);
			r = static_cast<uint8_t>((r << 1) ^ ((r >> 7) * 0x171));
		}
	}
}

uint64_t Keccak256::rotl64(uint64_t x, int i) {
	return ((0U + x) << i) | (x >> ((64 - i) & 63));
}

// Static initializers
const unsigned char Keccak256::ROTATION[5][5] = {
	{ 0, 36,  3, 41, 18},
	{ 1, 44, 10, 45,  2},
	{62,  6, 43, 15, 61},
	{28, 55, 25, 21, 56},
	{27, 20, 39,  8, 14},
};

/*
function getAddress(bytes memory bytecode, uint256 _salt) public view returns (address) {
    bytes32 hash = keccak256(
        abi.encodePacked(bytes1(0xff), address(this), _salt, keccak256(bytecode)));
    return address(uint160(uint(hash)));
}
*/
vector<std::uint8_t> getAddress(string bytecodeStr, string thisAddress, std::uint32_t salt) {
    // calculate keccak256(bytecode)
    std::uint8_t bytecode[6] = {0};
    for (int i = 0; i < 6; i++) {
        string hexStr = bytecodeStr.substr(2*i+2, 2);
        bytecode[i] = (uint8_t)stoi(hexStr, nullptr, 16);
    }
    std::uint8_t hashResult[32];
    Keccak256::getHash(bytecode, 6, hashResult);

    std::uint8_t thisAddressBytes[20] = {0};
    for (int i = 0; i < 20; i++) {
        string hexStr = thisAddress.substr(2*i+2, 2);
        thisAddressBytes[i] = (uint8_t)stoi(hexStr, nullptr, 16);
    }

    std::uint8_t msg[1+20+32+32] = {0};
    msg[0] = 0xff;
    for (int i = 0; i < 20; i++) {
        msg[i+1] = thisAddressBytes[i];
    }

    // salt last 4 bytes are filled, others are 0
    msg[1+20+32-4] = (uint8_t)(salt >> 24);
    msg[1+20+32-3] = (uint8_t)(salt >> 16);
    msg[1+20+32-2] = (uint8_t)(salt >> 8);
    msg[1+20+32-1] = (uint8_t)(salt);

    for (int i = 0; i < 32; i++) {
        msg[1+20+32+i] = hashResult[i];
    }

    uint8_t finalHash[32] = {0};
    Keccak256::getHash(msg, 1+20+32+32, finalHash);
    vector<std::uint8_t> result;
    // last 20 bytes
    for (int i = 12; i < 32; i++) {
        result.push_back(finalHash[i]);
    }
    return result;
}

int main(int argc, char **argv) {
    /*
    Sanity check:
        address(this): 0x44338f8D58F86cdcB26Ee00BF587Ad6ca4a10659
        _salt: 0
        bytecode: 0x3859818153F3
        msg.sender: 0x56c6c9954fb166ff6d485f126ed31346c418d4db
        final hash: 0x11a692fd4eac1948abc70e1964177165a8dd968c79747848baf1857c89256c3b
    */
    string bytecodeStr = argv[1];
    string thisAddress = argv[2];

    for (std::uint32_t salt = 0; salt < 4*1e6; salt++) {
        // keccak256(abi.encodePacked(msg.sender, proof.a))
        auto res = getAddress(bytecodeStr, thisAddress, salt);
        std::uint8_t msg[20+32] = {0};
        for (int i = 0; i < 20; i++) {
            msg[i] = res[i];
        }
        uint8_t hashResult[32] = {0};
        Keccak256::getHash(msg, 20+32, hashResult);
        string result = "0x";
        for (int i = 0; i < 32; i++) {
            char buf[3];
            sprintf(buf, "%02x", hashResult[i]);
            result += buf;
        }
        cout << result << ",";
    }
    return 0;
}