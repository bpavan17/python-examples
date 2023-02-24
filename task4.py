#Write a program which accepts a sequence of comma-separated
# numbers from console and generate a tuple. 
# Suppose the following input is supplied to the program: 

a=input("Enter the number :")
b=tuple(a.split(","))
print(b)