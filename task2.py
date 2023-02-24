#Create a new dictionary where keys are values and values are number of times
# given value has occurred in the dictionary. 


dictinput = {6:1,4:2,9:1,1:2,7:8,3:2}

dictoutput = {}
for key, value in dictinput.items():
    if value in dictoutput:
     dictoutput[value] += 1
    else:
        dictoutput[value] = 1

print(dictoutput) 