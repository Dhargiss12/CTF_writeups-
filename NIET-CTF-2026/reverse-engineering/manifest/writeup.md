
# MANIFEST — Android Static Analysis

**Event:** NIET CTF 2026  
**Category:** Reverse Engineering / Android  
**Status:** Solved

## 1. Objective

Analyze the Android application's authentication logic and
reconstruct the key derivation and token transformation used
to recover the challenge's plaintext.

## 2. Artifacts

The investigation involved:

- `vault-manager.apk`
- `AndroidManifest.xml`
- `AuthService.java`
- `token.enc`
- Application resources

The encrypted token was associated with the application's
`res/raw/token.enc` resource.

## 3. Key Derivation

The application used a salt seed and resource values to derive
a key using SHA-256.

The documented resource order was:

    k3, k7, k1, k5, k2, k6, k4, k8

The SHA-256 input was constructed from the salt seed, a colon
separator, and the ordered resource values.

Conceptually:

    digest = SHA256(saltSeed + ":" + orderedResources)

The exact encoding and resource values must match the
application's original implementation.

## 4. XOR Transformation

The recorded byte-wise transformation was:

    transformed[i] =
        masterKey[i % 32] ^ ((i * 13 + 37) & 0xff)

The transformation uses a 32-byte key and a position-dependent
value combined with XOR.

The direction of the operation and input encoding must be
consistent with the original authentication code.

## 5. Investigation Workflow

1. Inspected the Android manifest and application resources.
2. Traced the authentication logic in `AuthService.java`.
3. Extracted the salt seed and ordered resource values.
4. Reconstructed the SHA-256-based key derivation.
5. Applied the XOR transformation.
6. Decoded the resulting bytes.
7. Validated the recovered flag.

The recorded recovery script was named `recover.py`.

## 6. Result

Recorded flag:

`NIET{368073de1a78feee284358cd7a793682}`

## 7. Key Takeaways

- Android resources can contain inputs used by authentication logic.
- Static analysis can expose application-specific key derivation.
- SHA-256 does not compensate for insecure key management.
- XOR must be analyzed in the context of the complete implementation.

## 8. Further Reading

- https://developer.android.com/
- https://docs.python.org/3/library/hashlib.html
