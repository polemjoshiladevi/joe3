import os
list_files= os.listdir("C:\\Users\\training\\PycharmProjects\\joshila\\prank")
print(list_files)
os.chdir("C:\\Users\\training\\PycharmProjects\\joshila\\prank")
    #repeat the following steps for all the files in prank directory
for file in list_files:
    #get oldname of file
    old_name=file
    print(old_name)

    #newname of file=old_name_numbers
    new_name=old_name.lstrip("0123456789")
    print (new_name)
    #rename the file(oldname,newname)
    os.rename(old_name,new_name)
    print(new_name)