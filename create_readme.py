readme_content = """
===============================
 PENETRATION TESTING TOOLKIT
===============================

👦 Made by: Your Name
📅 Date: 2025-04-09

🎯 What is this?
-----------------
This is a simple Python-based toolkit used for basic penetration testing.
It helps check if a computer or system is secure by using two tools:

1. 🔍 Port Scanner
2. 💪 Brute-Force Password Guesser

🧰 What's Inside?
-------------------
- main.py               👉 The main file that runs everything.
- port_scanner/         👉 Folder with the port scanner tool.
- brute_forcer/         👉 Folder with the brute-force tool.
- passwords.txt         👉 A list of passwords to use in the brute-force attack.
- README.txt            👉 You're reading it now! 😊

🚀 How to Use It?
--------------------
1. Make sure Python is installed on your computer.
2. Open a terminal or command prompt.
3. Go to this folder.
4. Run: python main.py
5. Follow the instructions.

⚠️ Educational Use Only! Don't scan others' systems without permission.
"""

with open("README.txt", "w", encoding="utf-8") as file:
    file.write(readme_content)

print("✅ README.txt file has been filled successfully!")
