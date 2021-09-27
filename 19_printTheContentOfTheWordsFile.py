#this script reads and prints the content of text file input

file = open('words.txt', 'r') #store the opened text file in file var
contents = file.read() #store the opened file contents in contents var
print(contents) #print contents 