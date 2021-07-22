def get_secret_word(x):
    total = ''
    for i in x:         
        total += chr(i)
    return total

      
print(get_secret_word([83,115,65,182,89]))