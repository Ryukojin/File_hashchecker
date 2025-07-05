import file_scanner as fs
from key import vt_api

#Enter file path here
file_path = 'C:\\Users\\Fahim\\Downloads\\DCP_Interview_Qtns.txt'


#Generate file hash
file_hash = fs.get_file_hash(file_path)

#Send file hash to VirusTotal for scanning
fs.vt_file_scan(file_hash)
