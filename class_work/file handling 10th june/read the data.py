#open file read mode
f=open("data.txt","r")
lines=f.read()
vowels_count=0
chars_count=0
lines_count=0
vowels = "aeiouAEIOU"
for line in lines:
    chars_count += len(line)
    for char in line:
        if char in vowels:
            vowels_count += 1
            print(f"1. no. of vowels in file: {vowels_count}")
            print(f"2. no. of characters in file: {chars_count}")
            print(f"3. no. of lines in file: {lines_count}")
            
    
    