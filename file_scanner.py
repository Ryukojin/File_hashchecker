import requests
import hashlib
from key import vt_api

file_path = 'C:\\Users\\Fahim\\Downloads\\DCP_Interview_Qtns.txt'

def get_file_hash(file_path, algo='sha256'):
        # Choose hashing algorithm
    hash_func = getattr(hashlib, algo)()
        
    with open(file_path, 'rb') as file:
            # Read and update hash string value in blocks
        for chunk in iter(lambda: file.read(4096), b""):
                hash_func.update(chunk)
    return hash_func.hexdigest()

 

file_hash = '052b35727ed88753b4de63dedab884fe919482f666e37b10d6ee6f9d2e9091dc'


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
    scan = vt_file_scan(file_hash)
    #get_file_hash(file_path)



