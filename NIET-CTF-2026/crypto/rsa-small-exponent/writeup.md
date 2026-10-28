
# RSA Small Exponent — Exact Cube Root Attack

**Event:** NIET CTF 2026  
**Category:** Cryptography  
**Language:** Python  
**Status:** Solved

## 1. Objective

Recover the plaintext from an RSA ciphertext by identifying a
weakness caused by a small public exponent and a sufficiently
small plaintext.

## 2. RSA Background

RSA encryption is defined as:

    c = m^e mod n

Where:
- `m` is the plaintext represented as an integer.
- `e` is the public exponent.
- `n` is the RSA modulus.
- `c` is the ciphertext.

## 3. Vulnerability

The challenge used the public exponent:

    e = 3

When the plaintext is small enough that:

    m^3 < n

the modular operation does not reduce the result. Therefore:

    c = m^3

The original plaintext can be recovered by calculating the exact
integer cube root of the ciphertext.

## 4. Solution Methodology

1. Inspected the supplied challenge files.
2. Identified the RSA public exponent.
3. Represented the ciphertext as an integer.
4. Calculated its exact integer cube root using Python.
5. Verified that cubing the recovered integer reproduced the
   ciphertext.
6. Converted the recovered integer into bytes.
7. Checked the resulting plaintext against the flag format.

The solution script was named `solve.py`.

## 5. Result

Recorded flag:

`NIET{2884c3a1af52fa399ccf9362157731b8}`

## 6. Key Takeaways

- A small RSA exponent is not automatically vulnerable.
- Plaintext size and modular wraparound are important.
- Exact integer arithmetic avoids floating-point precision errors.
- Recovery should be validated mathematically.

## 7. Further Reading

- https://en.wikipedia.org/wiki/RSA_(cryptosystem)
- https://docs.python.org/3/library/stdtypes.html
