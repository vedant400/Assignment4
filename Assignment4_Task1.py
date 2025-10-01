#Task 1
try:
    file = open('sample.txt','r')
    print("Reading file content: \nLine 1: ",file.readline(),"\nLine 2: ",file.readline())
    file.close()
except FileNotFoundError:
    print("Error : The file 'sample.txt' was not found.")

