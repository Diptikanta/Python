

#This exercise asks user to enter a file name and it detects the extension of it.

fileName = input("Enter a file name with extension: ")

splitString = fileName.split('.')
#extsn = splitString[splitString.__len__()-1]

#print(extsn)

print("The file extension is: " + splitString[-1])

