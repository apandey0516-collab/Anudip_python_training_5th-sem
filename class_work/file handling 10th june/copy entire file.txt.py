# copy entire file
# open the file in read mode
f = open("data.txt","r")

# open the file in write mode
f1 = open("data1.txt","w")

# copy the contents of the file
f1.write(f.read())

# close the files
f.close()
f1.close()

