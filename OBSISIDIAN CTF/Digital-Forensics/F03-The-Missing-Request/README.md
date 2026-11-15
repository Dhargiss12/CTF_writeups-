# 🌐 [F03] The Missing Request

**Competition:** Obsidian Labs CTF 2026  
**Category:** Digital Forensics  
**Difficulty:** Medium  
**Points:** 250  
**Mode:** Online  

---

## 📋 Incident Background
During an alert investigation on endpoint `192.168.1.45`, network monitoring flagged suspicious egress towards external IP `93.184.216.34` between `03:12` and `03:41 UTC` on `2026-10-27`[cite: 3].

Traditional HTTP inspection showed no cleartext file transfers or standard download URIs[cite: 3]. Intelligence indicates the threat actor used a non-HTTP covert tunneling mechanism to exfiltrate a compressed system archive from the endpoint[cite: 3].

### Provided Artifacts
- `F03_The_Missing_Request.zip` (44 KB) — Challenge archive[cite: 4]
- `network_dump.pcap` (121 KB) — Raw network traffic capture[cite: 4]
- `sslkeylog.log` (1 KB) — Extracted TLS session keylog (NSS key log format)[cite: 4]

---

## 🛠️ Tools & Environment
- Wireshark / `tshark`
- Python 3 (`scapy` / `pyshark`)
- Archive Utilities (`unzip` / `7z`)

---

## 🔎 Investigation Methodology
1. **TLS Session Triage:** Load `sslkeylog.log` into Wireshark (`Preferences -> Protocols -> TLS -> (Pre)-Master-Secret log filename`) to decrypt the endpoint's TLS update-check session and rule out standard HTTPS exfiltration[cite: 4].
2. **Time-Window & Traffic Filtering:** Filter `network_dump.pcap` to isolate traffic involving `192.168.1.45` and `93.184.216.34` strictly within the `03:12`–`03:41 UTC` window (`2026-10-27`), separating routine LAN chatter and ping sweeps from anomalous ICMP streams[cite: 3, 4].
3. **ICMP Covert Channel Reassembly:** Inspect the ICMP data payloads, strip the short binary implant header from the legitimate exfiltration stream, and reassemble the raw payload bytes in sequence[cite: 4].
4. **Archive Extraction:** Verify the magic bytes of the reassembled compressed archive, decompress it, and read the endpoint triage notes to obtain the flag[cite: 4].

---

## 🚩 Flag
```text
OBSIDIAN{1cmp_c0v3rt_ch4nn3l_7a3f}
