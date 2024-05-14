import sys

def bin_to_shellcode(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    
    shellcode = ', '.join([f"0x{byte:02X}" for byte in data])
    return shellcode

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python bin_to_shellcode.py <binary_file>")
        sys.exit(1)
    
    bin_file = sys.argv[1]
    try:
        shellcode = bin_to_shellcode(bin_file)
        print("Shellcode:")
        print(shellcode)
    except FileNotFoundError:
        print(f"Error: File '{bin_file}' not found.")
        sys.exit(1)
