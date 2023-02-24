doc = """ IEEE and it's members inspire a global community to innovate for a 

better tomorrow through highly cited publications, conference, technology  

standards, and professional and educational activities. IEEE is the trusted 

"voice" for engineering computing, and technology information around the globe. 

""" 
if 'and' in doc:
    print('"and"is present ')
else:
    print('"and"is not present')

a=doc.split()
print(a)
b=a.count("and")
print(b)