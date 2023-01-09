# Read the contents of a file and print odd lines
# opening a existing file Data.txt for read and open another file for writing

read_open= open("Data.txt")
write_open= open("Contents.text",'w')

#store the lines in Data_lines

data_lines = read_open.readlines()
print("\n The real Contents OF DATA.text is:\n")
print(data_lines)

# writing datas to write_data

for i in range(0,len(data_lines)):
    if i % 2 == 0:
        write_open.write(data_lines[i])
    else:
        pass
write_open.close()

# closing the file write_open after writing the contents


write_open= open("Contents.text",'r')
write_on = write_open.readlines()
print("Odd lines Are:")
print(write_on,"\n")

# closing both files

read_open.close()
write_open.close()
