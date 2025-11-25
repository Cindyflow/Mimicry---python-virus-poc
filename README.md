# Simple Python Virus

A basic example of a Python virus that displays a message box and replicates itself to the desktop. This project is intended for educational purposes and should be tested in a controlled environment, such as a virtual machine.

## Features

- Displays a message box with an infection alert.
- Replicates itself to the user's desktop.
- (Optional) Adds itself to the Windows startup folder for persistence.

## Requirements

- Python 3.x
- Windows operating system

## Usage

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/Simple-Virus.git
   cd Simple-Virus

## Run the Virus:

2. Open a command prompt or PowerShell window.
Navigate to the directory containing virus.py.
Execute the script

```sh
    python virus.py
```
## 3.Test in a Virtual Machine:
It is highly recommended to test this virus in a virtual machine to avoid accidental infections on your main system

## Files

**virus.py:** The main virus script.

**README.md:** This file, providing information about the project.

## Optional: Adding Persistence

To make the virus persistent (i.e., it runs on system startup), you can use the add_to_startup function in the script. This function adds an entry to the Windows registry to ensure the virus runs every time the system boots up.

## Disclaimer

This virus is for educational purposes only. Use it at your own risk. The author is not responsible for any damage caused by this virus.