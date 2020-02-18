alphabet = "abcdefghijklmnopqrstuvwxyz"
newAlphabet = ""
n = 12  #This number determines the degree of the shift. 
for i in range(len(alphabet)):        
    if i+n >= len(alphabet):
        diff = i+n - len(alphabet) 
        newAlphabet = newAlphabet + alphabet[diff]
    else:
        newAlphabet = newAlphabet + alphabet[i+n]

print(newAlphabet)
