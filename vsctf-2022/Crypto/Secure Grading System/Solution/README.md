# Secure Grading System

## Solution

After reading `Grading system documentation`, we know there are several steps to solve the challenge.

1. Proof of work: this is trivial as we can just brute force the 4 characters.
2. Signing: `ECDSA` is used as signing schema. There is a clear vulnerability in the signing scheme that second signature is using the same nonce `k` as the first signature. Attacker can easily recover private key: [Nonce Reuse in ecdsa](https://billatnapier.medium.com/ecdsa-weakness-where-nonces-are-reused-2be63856a01a#:~:text=It%20is%20a%20well%2Dknown,is%20used%20for%20different%20messages.)
3. RSA: `e=3` and 3 messages are sent. Then [Hastad Broadcast Attack](https://en.wikipedia.org/wiki/Coppersmith%27s_attack#H%C3%A5stad's_broadcast_attack) can be used to recover the plaintext if we know all 3 ciphertexts.

In the challenge we are given the ciphertexts of the messages. Therefore we first recover the plaintexts and then we can recover the private key `d` in ecdsa.

Check `exploit.py` for exploit script.