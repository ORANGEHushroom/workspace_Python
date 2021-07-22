def get_secret_word(x):
    total = 0
    for i in x:         
        total += ord(i)
    return total

      
print(get_secret_word('tom'))