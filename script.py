import sys
import scanner as sc

#retrive file path from command line argument as string
file_path = sys.argv[1]
#retrieve the hash of the file
the_hash = sc.get_sha256(file_path)

print("Processing hash of target file: " + "'" + file_path + "'")
print("The file hash is: " + the_hash)


clip = sc.get_clipboard()

#Make the CLI output stay until user decides to exit
input("\nPress enter to exit...")

