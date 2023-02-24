#Given a dictionary d = {'apple': 'red', 'banana': 'yellow', 'grapes': 'GREEN', 'pomegranate': 'red', 'guava': 'GREEN', 'mango': 'yellow'} 
#Create a new dictionary  
#d_new = {3:[‘red’, ‘red’], 6:[‘yellow’, ‘yellow’], 5:[‘green’, ‘green’]} 

d = {'apple': 'red', 'banana': 'yellow', 'grapes': 'GREEN', 'pomegranate': 'red', 'guava': 'GREEN', 'mango': 'yellow'}

d_new = {}
for key, value in d.items():
    
    value = value.lower()
    if len(value) in d_new:
        d_new[len(value)].append(value)
    else:
        d_new[len(value)] = [value]


print(d_new)
sorted_d_new=dict(sorted(d_new.items()))
print(sorted_d_new)

