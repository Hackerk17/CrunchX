# ⚡ CrunchX

CrunchX is a **powerful wordlist generation and password research framework** designed for:

* Bug bounty hunters
* Penetration testers
* Red teamers
* Cybersecurity students

CrunchX combines **wordlist generation, OSINT collection, password analysis, and hash cracking** in a single CLI tool.

Inspired by tools like Hashcat and John the Ripper.


# 🚀 Features

* 🔐 Pattern wordlist generator
* 🤖 Smart password guessing
* 🎭 Mask attack generator
* 🎲 Random password generator
* 🏢 Company OSINT password generator
* 🕷 Website crawler wordlist generator
* 📊 Password entropy analyzer
* 📦 RockYou downloader
* 📚 SecLists downloader
* 🔓 Hash cracker (dictionary attack)

# 📥 Download

Clone repository

```bash
git clone https://github.com/Hackerk17/CrunchX.git
```

Enter directory

```bash
cd CrunchX
```

# 📦 Requirements

Python 3.x

Install dependency

```bash
pip install requests
```

# ⚙ Setup

Run CrunchX

```bash
python3 crunch.py
```

# 🖥 Menu

```
1 Pattern Wordlist
2 Smart Password Guess
3 Mask Attack
4 Random Passwords
5 Company OSINT
6 Website Wordlist
7 Password Entropy
8 Download Wordlists
9 Hash Cracker
0 Exit
```

---

# 🔐 Pattern Wordlist

Example

```
Pattern: pass@123
Count: 100
Output: passwords.txt
```

Generated examples

```
pass@123
Pass@123
PASS@123
```

---

# 🎭 Mask Attack

Supported masks

| Mask | Meaning           |
| ---- | ----------------- |
| ?l   | lowercase letters |
| ?u   | uppercase letters |
| ?d   | digits            |
| ?s   | symbols           |

Example

```
Mask: ?l?l?d?d
Count: 1000
```

---

# 🤖 Smart Guess

Example

```
Name: john
Count: 200
```

Generated passwords

```
john123
john@123
John2025
john_123
```

---

# 🕷 Website Wordlist Generator

Example

```
URL: https://example.com
Count: 1000
```

CrunchX will extract words from website content.

---

# 📊 Password Entropy Analyzer

Check password strength.

Example

```
Password: MyPassword@123
```

Output

```
Entropy: 72 bits
```

---

# 🔓 Hash Cracker

CrunchX supports dictionary-based hash cracking.

Supported hashes

* MD5
* SHA1
* SHA256

Example

```
Hash: 5f4dcc3b5aa765d61d8327deb882cf99
Type: md5
Wordlist: rockyou.txt
```

Output

```
Password Found: password
```

---

# 📦 Wordlist Downloads

CrunchX can download

RockYou (~134MB)

SecLists (~500MB)

---

# 🐉 Kali Linux RockYou

Location

```
/usr/share/wordlists/rockyou.txt.gz
```

CrunchX can automatically detect and extract it.

---

# 💻 CLI Usage

Generate wordlist from terminal.

Example

```bash
python3 crunch.py -p password -c 1000 -o wordlist.txt
```

Options

| Option | Description |
| ------ | ----------- |
| -p     | Pattern     |
| -c     | Count       |
| -o     | Output file |

---

# ⚠ Disclaimer

CrunchX is intended for **educational and authorized security testing only**.

Do not use it for illegal purposes.

---

# 👨‍💻 Author

Hackerk17
