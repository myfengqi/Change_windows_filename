import subprocess
import os

unit_str = input("Do you need a common string?(yes or no):")

if unit_str == "yes":
    string = input("Please input string:")
elif unit_str == "no":
    string = ""
else:
    exit()

extract_file = open("zzz_extract_filename.bat","w")
extract_file.write("DIR *.*/B > zzz_filename.txt\n")
extract_file.close()

filepath = 'zzz_extract_filename.bat'
p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)
stdout, stderr = p.communicate()

f = open("zzz_filename.txt","r")
lines_origin = f.readlines()
f.close()

length = len(lines_origin)


change_file_name = open('zzz_change_filename.bat','w')

count = 0
while count < (length-3):
    count = count + 1
    lines_origin[count-1] = lines_origin[count-1].rstrip('\n')
    change_file_name.write("ren " + "\"" + lines_origin[count-1] + "\"" + " " + string + str(count).zfill(3)+ ".jpg\n")

change_file_name.close()

filepath = 'zzz_change_filename.bat'
p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)
stdout, stderr = p.communicate()


os.remove("zzz_extract_filename.bat")
os.remove("zzz_filename.txt")
os.remove("zzz_change_filename.bat")

    
