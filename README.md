# ShellBin

I made these scripts to facilitate shellcode portability. 

# Usage

## ShellCode2Bin.py

This script takes in a shellcode array as described below and it will save it into a .bin file at the user's choice.

```
python3 ShellCode2Bin.py "0xFC, 0xA1, 0xB1" mybinFile.bin
```

## Bin2ShellCode.py
This script does the opposite and takes in a .bin file to then output shellcode to the console.

```
python3 Bin2ShellCode.py calc.bin

```
