#Task 2
file1 = open('output.txt','w')
writing_file = file1.write(input("Enter the text to write to the file: ") + "\n")
print("Data successfully written to output.txt.")
file1.close()

file2 = open('output.txt','a')
appending_file = file2.write(input("Enter additional text to append: ") + "\n")
print("Data successfully appended.")
file2.close()

file3 = open('output.txt','r')
print("Final content of output.txt:\n",file3.read())