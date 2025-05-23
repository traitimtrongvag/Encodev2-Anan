### Data Encryption V2

### Developed by: An An

### Overview

Data Encryption V2 is a simple yet powerful Python tool that compiles Python source files into bytecode, marshals them, and encodes them using Base85 to obfuscate the original code. The resulting script can be executed directly while keeping the source code hidden from plain view.

This project also features a visually appealing terminal interface using pystyle and rich.


---

### Features

Source Code Obfuscation
Convert Python scripts into a single-line executable form, making it hard to reverse-engineer.

Base85 Encoding
Uses base64.a85encode for efficient and compact encoding.

Visual UI in Terminal
Stylized terminal output using pystyle and rich.console.

Multi-Platform Support
Compatible with Windows, macOS, and Linux.



---

### How It Works

1. Reads a Python source file.


2. Compiles it into bytecode.


3. Marshals the bytecode.


4. Encodes it with Base85.


5. Wraps it into an exec() statement.


6. Saves the encoded version to a new file.




---

### Directory Structure

.
├── FileCanMaHoa/      # Source files to be encoded
├── FileDaMaHoa/       # Encoded output files
├── encrypt.py         # Main encryption script
└── README.md          # Project documentation


---

### Requirements

Install the dependencies using pip:
```bash
pip install pystyle rich
```

---

Usage

1. Place the Python file you want to encode into the FileCanMaHoa directory.


2. Run the script:


```bash
python Main.py
```
3. Enter the name of the file when prompted (e.g., myscript.py).


4. The encoded file will be saved in the FileDaMaHoa directory with the prefix enc_.




---

### Example

Input: myscript.py
Output: FileDaMaHoa/enc_myscript.py (contains obfuscated exec(...) code)


---

### Disclaimer

This tool is intended for educational purposes and protecting your own code. Do not use it to hide malicious content or for unauthorized obfuscation.


---

### License

This project is open-source and free to use under the MIT License.


---

Let me know if you'd like a Vietnamese version or want this turned into an actual GitHub repo for you.

