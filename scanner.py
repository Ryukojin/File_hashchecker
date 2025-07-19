import requests
import hashlib
import pyperclip
import re
from key import vt_api


def get_file_hash(file_path, algo='sha256'):
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
            print(f"✅ Hash found: {matches[0]}")
        else:
            print("No hash found in clipboard, please copy a hash to the clipboard")
    
    return matches[0] if matches else None


#What will be output if the file is not found in VT database
#http://jsonlint.vearne.cc/
def vt_file_scan(file_hash):

    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"

    headers = {
        "accept": "application/json",
        "x-apikey": vt_api
    }

    response = requests.get(url, headers=headers)

    print(response.json())
    #return response.json()


'''
if __name__ == "__main__":
    #vt_file_scan(file_hash)
    print(get_file_hash(file_path, algo='sha256'))
'''