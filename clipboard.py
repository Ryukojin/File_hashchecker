import pyperclip
import re

hash_example = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'



def get_clipboard():
    hash_regex = r"\b([a-fA-F0-9]{32}|[a-fA-F0-9]{40}|[a-fA-F0-9]{64})\b"
    last_clipboard = ""
    print("Scanning clipboard for existing hashes...")

    current_clipboard = pyperclip.paste()
            
    if current_clipboard != last_clipboard:
        last_clipboard = current_clipboard
        matches = re.findall(hash_regex, current_clipboard)
                
        if matches:
            print(f"✅ Hash found: {matches[0]}")
        else:
            print("No hash found in clipboard, please copy a hash to the clipboard")

