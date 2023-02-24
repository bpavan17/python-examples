#Generate a random dictionary where keys and 
# values are of integer type and keys start from 2.
# Example- {2:3, 3:7, 4:13, 5:7}


import random

d = {}
for keys in range(2, 6 ):
  d[keys] = random.randrange(100)
print(d)





import random
d = {}
num = 7
d[2]=random.randint(2, 100)
# Generate the keys and values
for i in range(num):
  key = random.randint(2, 100)
  value = random.randrange(1, 100)
  d[key] = value
  
print(d)

import random
d={}
keys=random.uniform(1,9)
value=random.randint(1,88)
d[keys]=value
print(d)

