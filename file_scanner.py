import requests
import hashlib
from key import vt_api

file_path = "C:\\Users\\Fahim\\Downloads\\Interview_qtn_bank.txt"

def get_file_hash(file_path, algo='sha256'):
        # Choose hashing algorithm
    hash_func = getattr(hashlib, algo)()
        
    with open(file_path, 'rb') as file:
            # Read and update hash string value in blocks
        for chunk in iter(lambda: file.read(4096), b""):
                hash_func.update(chunk)
    return hash_func.hexdigest()

 
file_hash = 'cd10fb91d93196728122f41363b97c161e8ca31b158dbacedf2c4cb52c6417e7'


def vt_file_scan(file_hash):

    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"

    headers = {
        "accept": "application/json",
        "x-apikey": vt_api
    }

    response = requests.get(url, headers=headers)

    print(response.json())
    #return response.json()
    #What will be output if the file is not found in VT database
#http://jsonlint.vearne.cc/


if __name__ == "__main__":
    #vt_file_scan(file_hash)
    print(get_file_hash(file_path, algo='sha256'))