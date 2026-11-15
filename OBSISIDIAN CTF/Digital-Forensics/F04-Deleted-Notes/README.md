# 💾 [F04] Deleted Notes

**Competition:** Obsidian Labs CTF 2026  
**Category:** Digital Forensics  
**Difficulty:** Medium  
**Points:** 250  
**Mode:** Online  

---

## 📋 Scenario
During a raid on a clandestine biochemical testing facility, digital forensics investigators recovered a USB thumb drive (`usb_evidence.img`) from an air-gapped terminal.

The primary evidence container `VAULT.ENC` is encrypted. Triage notes indicate the lead researcher recorded the emergency recovery passkey in a lab memorandum and deleted the file before abandoning the lab. However, multiple memoranda were deleted with damaged directory metadata, leaving orphaned FAT cluster chains, and the recovery key was split between the genuine memorandum and a night-shift audit log (`AUDIT.LOG`).

### Provided Artifacts
- `F04_Deleted_Notes.zip` (22 KB) — Challenge archive
- `usb_evidence.img` (16,384 KB) — 16 MB raw FAT filesystem image
- `decrypt_vault.py` (1 KB) — Local verification and decryption utility

---

## 🛠️ Tools & Environment
- The Sleuth Kit (`fls`, `icat`, `fsstat`) / Autopsy / FTK Imager
- Python 3
- Hex Editor

---

## 🔎 Investigation Methodology
1. **Filesystem & Orphan Cluster Analysis:** Inspect the FAT32 partition layout, directory tables, and FAT cluster chains in `usb_evidence.img` to locate deleted memoranda as well as unallocated/orphaned cluster chains lacking directory entries.
2. **Audit Log & Seal Hash Verification:** Analyze `AUDIT.LOG` to understand how case numbers, seal statuses, timestamps, and cryptographic seal hashes were generated, then recompute hashes against carved memoranda to identify the genuine memo.
3. **Passkey Reconstruction:** Combine the first half of the emergency recovery passkey from the verified memorandum with the second half stored in its corresponding seal record in `AUDIT.LOG`.
4. **Vault Decryption:** Extract `VAULT.ENC` from the filesystem image and run:
   ```bash
   python decrypt_vault.py VAULT.ENC <PASSKEY>

   OBSIDIAN{c4rv3d_f4t32_clvst3r_ch41n_9918}
