import random
import time

def calculate(blossom, n, m):
    assert len(blossom) == n
    res = 0
    curr = 0
    l, r = 0, 0
    # iterate blossom array, find the max subarray sum whose length is less or equal to m
    while r < n:
        curr += blossom[r]
        if curr < 0:
            l = r + 1
            r = l
            curr = 0
            continue
        res = max(res, curr)
        r += 1
        if r == n: break
        if r - l + 1 > m:
            curr -= blossom[l]
            l += 1
    return res

def main():
    for t in range(1, 11):
        print(f"Test case {t}/10:")
        print("Input:")
        n = random.randint(1, 1000000)
        m = random.randint(1, 1000000)
        print(n, m)
        blossom = []
        for _ in range(n):
            blossom.append(random.randint(-1000000000, 1000000000))
            print(blossom[-1], end=" ")
        print()
        currtime = time.time()
        res = input("Output: ")
        if res != str(calculate(blossom, n, m)):
            print("Incorrect!")
            exit(0)
        # if more than 5 seconds, then it's too slow
        if time.time() - currtime > 5:
            print("Too slow!")
            exit(0)
    print("All Correct! Your flag: cvctf{H4v3_u_s33n_th3_ch3rry_bl0ss0m?}")

if __name__ == "__main__":
    try:
        main()
    except:
        exit(0)