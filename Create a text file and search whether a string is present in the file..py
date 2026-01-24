# Write a Python program to create a text file and search whether a string is present in the file.
with  open("file1.txt", "w") as fp1:
    # appending the content to the file  
    fp1.write(
        ''' Rose is a beautiful flower\n They come in shades of red,white,orange and yellow\n They symbolise beauty love and compassion.''')
searchstring = input("Enter the string to be searched for : ")
flag = 0
lineno = 0
with open("file1.txt", "r") as fp1:
    for line in fp1:
        lineno += 1
        if searchstring in line:
            flag = 1
            break
if flag == 0:
    print('String', searchstring, 'Not Found in the file')
else:
    print('String', searchstring, 'Found In Line', lineno)
