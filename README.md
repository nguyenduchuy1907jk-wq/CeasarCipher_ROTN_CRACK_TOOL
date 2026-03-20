# 🔐 Caesar Cipher Tool
 
```
░█████╗░░█████╗░███████╗░██████╗░█████╗░██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗
██║░░╚═╝███████║█████╗░░╚█████╗░███████║██████╔╝
██║░░██╗██╔══██║██╔══╝░░░╚═══██╗██╔══██║██╔══██╗
╚█████╔╝██║░░██║███████╗██████╔╝██║░░██║██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝
```
 
> A clean, interactive CLI tool for encrypting, decrypting, and breaking Caesar ciphers — built for CTF players and crypto enthusiasts.
 
---
 
## ✨ Features
 
| Feature | Description |
|---|---|
| 🔒 **Encrypt** | Shift any text by a custom key |
| 🔓 **Decrypt** | Reverse a Caesar shift |
| 🔄 **ROT-N** | Apply any arbitrary rotation |
| 🔁 **ROT13** | Classic ROT13 in one command |
| 💣 **Brute Force** | Try all 26 possible keys at once |
| 🧠 **Auto Detect** | Automatically find the best key using common word scoring |
 
---
 
## 📖 Description
 
When you run the Python file, you'll be greeted with an **interactive menu** where you can choose from 6 different modes:
 
- **Mode 1 — Encrypt**: Type in any text and a numeric key, and the tool will shift every letter by that key to produce the ciphertext.
- **Mode 2 — Decrypt**: Got an encoded message and know the key? Paste it in and instantly get the original text back.
- **Mode 3 — ROT-N**: A flexible rotation — same as Caesar but lets you explicitly think of it as "rotating N positions".
- **Mode 4 — ROT13**: One-click ROT13. Since ROT13 is its own inverse, encrypting and decrypting are the same operation.
- **Mode 5 — Brute Force**: Don't know the key? No problem. The tool tries all 26 possible shifts and prints every result — you just scan for the one that makes sense.
- **Mode 6 — Auto Detect**: The smart mode. It scores all 26 decryptions by checking for common English words (`THE`, `AND`, `FLAG`, `CTF`, `PICO`...) and automatically picks the most likely answer.
 
After each operation the menu reappears, so you can keep working without restarting the script. Enter `0` at any time to exit.
 
---
 
## 🚀 Getting Started
 
### Requirements
 
- Python 3.6+
- No external dependencies — pure stdlib!
 
### Run it
 
```bash
git clone https://github.com/yourusername/caesar-cipher-tool.git
cd caesar-cipher-tool
python caesar.py
```
 
---
 
## 🎮 Usage
 
```
===== Caesar Cipher Tool =====
1. Encrypt (Caesar)
2. Decrypt (Caesar)
3. ROT N
4. ROT13
5. Brute Force
6. Auto Detect
0. Exit
```
 
### Examples
 
**Encrypt:**
```
Choose: 1
Enter text: Hello World
Enter key: 13
Result: Uryyb Jbeyq
```
 
**Brute Force:**
```
Choose: 5
Enter text: Khoor Zruog
 
=== Brute Force ===
[Key  0] Khoor Zruog
[Key  1] Jgnnq Yqtnf
[Key  2] Ifmmp Xpsme
[Key  3] Hello World   ✅
...
```
 
**Auto Detect:**
```
Choose: 6
Enter text: Khoor Zruog
 
=== Auto Detect ===
Best key: 3
Decrypted: Hello World
```
 
---
 
## 🧠 How It Works
 
The Caesar cipher shifts each letter by `k` positions in the alphabet:
 
```
Encrypt:  c = (m + k) mod 26
Decrypt:  m = (c - k) mod 26
```
 
The **Auto Detect** feature scores each of the 26 possible decryptions by counting how many common English words appear (THE, AND, FLAG, CTF, PICO, etc.) — whichever key produces the most matches wins.
 
---
 
## 🏴 CTF Use Cases
 
This tool is particularly useful for:
- **picoCTF** and similar beginner crypto challenges
- Recognizing ROT13 encoded strings
- Quickly brute-forcing unknown Caesar shifts
- Auto-detecting flags like `picoCTF{...}` in encoded text
 
---
 
## 📁 Project Structure
 
```
caesar-cipher-tool/
│
├── caesar.py       # Main script
└── README.md       # You are here
```
 
---
 
## 📜 License
 
MIT — do whatever you want with it.
 
---
 
<p align="center">Made with ❤️ for CTF players</p>
