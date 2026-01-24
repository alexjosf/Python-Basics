# Write a Python program to create a file and copy it to another file.
# Write a Python program to create a file and copy it to another file.
with open("file1.txt", "w") as fp1:
    # appending the content to the file  
    fp1.write(
        '''Rose is a beautiful flower\n They come in shades of red,white,orange and yellow\n They symbolise beauty 
        love and compassion.''')
with open("file1.txt", "r") as fp1, open("file2.txt", "w") as fp2:
    # read content from first file
    for line in fp1:
        # write content to second file
        fp2.write(line)
