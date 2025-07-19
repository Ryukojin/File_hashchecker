import sys
import scanner as sc


file_path = sys.argv[1]
the_hash = sc.get_file_hash(file_path)

print("Processing hash of target file: " + "'" + file_path + "'")
print("The file hash is: " + the_hash)


clip = sc.get_clipboard()


if(clip == the_hash):
    print("\nThe hash matches the file hash!")
else:   
    print("\nThe hashes did not match!")


#Make the CLI output stay until user decides to exit
input("\nPress enter to exit...")

