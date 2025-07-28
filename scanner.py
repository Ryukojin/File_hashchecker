import requests
import hashlib
import pyperclip
import re


def get_sha256(file_path, algo='sha256'):
        # Choose hashing algorithm
    hash_func = getattr(hashlib, algo)()
        
    with open(file_path, 'rb') as file:
            # Read and update hash string value in blocks
        for chunk in iter(lambda: file.read(4096), b""):
                hash_func.update(chunk)
    return hash_func.hexdigest()


def get_clipboard():
    hash_regex = r"\b([a-fA-F0-9]{32}|[a-fA-F0-9]{40}|[a-fA-F0-9]{64})\b"
    last_clipboard = ""
    print("\nScanning clipboard for existing hashes...")

    current_clipboard = pyperclip.paste()
            
    if current_clipboard != last_clipboard:
        last_clipboard = current_clipboard
        matches = re.findall(hash_regex, current_clipboard)
                
        if matches:
            print(f"The hash of this file is: {matches[0]}")
            print("✅ Both hashes match!")
        else:
            print("\nHashes don't match or no hash was copied to clipboard.")
            print("Please copy a hash to the clipboard.")
    
    return matches[0] if matches else None


'''
if __name__ == "__main__":
    print(get_md5(file_path, algo='md5'))
    print(get_sha256(file_path, algo='sha256'))
'''