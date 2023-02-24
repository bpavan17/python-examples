#Find the word ‘and’ and print how many times it’s in the doc. 


a=open("/home/pavanb/Documents/task/doc.txt",'r')
b=a.read()
if 'and' in b:
    print('"and"is present ')
else:
    print('"and"is not present')

c=b.split()
print(c)
d=c.count('and')
print(d)