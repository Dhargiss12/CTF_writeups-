# 🔍 [F01] Format Archaeology

**Competition:** Obsidian Labs CTF 2026  
**Category:** Digital Forensics  
**Difficulty:** Easy  
**Points:** 100  
**Mode:** Offline  

---

## 📋 Scenario
During an active incident response investigation, security analysts intercepted an image file named `evidence.png` captured from an internal workstation.

The image shows the Obsidian Security Archival Interface mid-session: a system audit was active, a host registry hive had just been captured, and an encrypted container had been staged for archival. The screen confirms the staging but does not hand over the container's location or its key.

Not everything the tools flag is the staged container. The screen itself warns about debris past the image's `IEND` boundary and notes that the registry holds the ground truth, while the vault key at rest requires applying vault policy.

### Provided Artifacts
- `F01_Format_Archaeology.zip` (56 KB) — Challenge archive
- `evidence.png` (60 KB) — Intercepted archival interface capture
- `registry_export.reg` (1 KB) — Captured host registry hive

---

## 🛠️ Tools & Environment
- Image Viewer
- Hex Editor (`HxD` / `010 Editor` / `ImHex`)
- Archive Utilities (`unzip` / `7z`)
- Carving Utilities (`binwalk` / `dd` / Python)
- Decoding Utilities (`CyberChef` / Python)

---

## 🔎 Investigation Methodology
1. **PNG Boundary Analysis:** Inspect `evidence.png` in a hex editor to locate the `IEND` chunk marker (`49 45 4E 44 AE 42 60 82`) and separate false-positive debris from appended trailing data.
2. **File Carving:** Extract the embedded/appended payload past the `IEND` boundary using `binwalk`, `dd`, or Python.
3. **Registry Examination:** Parse `registry_export.reg` to verify the ground-truth staging path, container metadata, and vault policy rules governing the key at rest.
4. **Key Transformation & Decryption:** Apply the vault policy transformation to the raw key and unlock the staged container to recover the incident memo.

---

## 🚩 Flag
```text
OBSIDIAN{c4rv3d_4nch0r_chr0n1cl3_5520}
