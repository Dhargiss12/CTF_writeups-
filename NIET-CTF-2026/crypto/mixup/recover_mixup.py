
#!/usr/bin/env python3
"""
NIET CTF 2026 — MIXUP
Technique: RSA common-modulus attack
"""

from math import gcd


def extended_gcd(a, b):
    """Return (g, x, y), where a*x + b*y = g."""
    if b == 0:
        return a, 1, 0

    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def recover_plaintext(n, e1, e2, c1, c2):
    """Recover m when both ciphertexts encrypt the same message."""
    g, a, b = extended_gcd(e1, e2)

    if g != 1:
        raise ValueError("Public exponents must be coprime.")

    if gcd(c1, n) != 1 or gcd(c2, n) != 1:
        raise ValueError(
            "A ciphertext is not invertible modulo n; "
            "this implementation cannot use that input."
        )

    part1 = pow(c1, a, n)
    part2 = pow(c2, b, n)

    return (part1 * part2) % n


def main():
    print("NIET CTF — MIXUP RSA Recovery")
    n = int(input("RSA modulus n: ").strip())
    e1 = int(input("Public exponent e1: ").strip())
    e2 = int(input("Public exponent e2: ").strip())
    c1 = int(input("Ciphertext c1: ").strip())
    c2 = int(input("Ciphertext c2: ").strip())

    try:
        m = recover_plaintext(n, e1, e2, c1, c2)
        plaintext = m.to_bytes((m.bit_length() + 7) // 8, "big")

        print("\n[+] Recovered integer:", m)
        print("[+] Plaintext bytes:", repr(plaintext))

        try:
            print("[+] Decoded text:", plaintext.decode("utf-8"))
        except UnicodeDecodeError:
            print("[!] Result is not valid UTF-8.")

    except ValueError as exc:
        print("[!] Recovery failed:", exc)


if __name__ == "__main__":
    main()
