import sys
import scanner as sc


file_path = sys.argv[1]


print("Processing hash of target file: " + "'" + file_path + "'")
print("The file hash is: " + sc.get_file_hash(file_path))
clip = sc.get_clipboard()
the_hash = sc.get_file_hash(file_path)


if(clip == the_hash):
    print("\nThe hash matches the file hash!")
else:   
    print("\nThe hashes did not match!")
    #print("The clipboard hash is: " + clip)
    #print("But the file hash is: " + the_hash)


#Make the CLI output stay until user decides to exit
input("\nPress enter to exit...")

