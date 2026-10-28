
# MIXUP — RSA Common Modulus Attack

**Event:** NIET CTF 2026  
**Category:** Cryptography  
**Language:** Python  
**Status:** Solved

## 1. Objective

Investigate the RSA parameters and recover the plaintext by
exploiting a mathematical relationship between the public
exponents.

## 2. Initial Findings

The challenge involved RSA ciphertexts using a common modulus
and public exponents:

    e1 = 65537
    e2 = 718813

The recorded Bézout coefficients were:

    a = 41536
    b = -3787

They satisfy:

    a * e1 + b * e2 = 1

This relationship enables a common-modulus attack when the
ciphertexts encrypt the same plaintext under the required
conditions.

## 3. Mathematical Principle

For two ciphertexts:

    c1 = m^e1 mod n
    c2 = m^e2 mod n

Bézout's identity gives:

    a * e1 + b * e2 = 1

Combining the ciphertexts with these coefficients can recover
the plaintext modulo the RSA modulus.

A negative coefficient requires a modular inverse. The relevant
ciphertext must be invertible modulo `n`.

## 4. Solution Workflow

1. Examined the RSA public parameters and ciphertexts.
2. Identified the shared-modulus relationship.
3. Verified the Bézout coefficients.
4. Applied the common-modulus recovery method.
5. Converted the recovered integer into bytes.
6. Checked the recovered plaintext against the expected flag.

The recorded Python script was named `recover_mixup.py`.

## 5. Result

Recorded flag:

`NIET{a4b3d6ecbb60c090c49d4136342d3644}`

## 6. Key Takeaways

- Reusing an RSA modulus can introduce security weaknesses.
- Bézout's identity can be useful in cryptanalysis.
- Negative modular exponents require modular inverses.
- Attack assumptions must be checked against the actual inputs.

## 7. Further Reading

- https://en.wikipedia.org/wiki/RSA_(cryptosystem)
- https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity
