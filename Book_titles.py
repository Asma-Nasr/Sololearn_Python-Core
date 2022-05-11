'''You have been asked to make a special book categorization program, which assigns each book a special code based on its title.
The code is equal to the first letter of the book, followed by the number of characters in the title.
For example, for the book "Harry Potter", the code would be: H12, as it contains 12 characters (including the space).

You are provided a books.txt file, which includes the book titles, each one written on a separate line.
Read the title one by one and output the code for each book on a separate line.'''

file = open("/usercode/files/books.txt", "r")

#your code goes her

line=file.readlines()
    
for name in line:
    print(name[0] + str(len(name.rstrip('\n'))))
file.close()
