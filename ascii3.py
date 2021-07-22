def get_strong_word(x1,x2):
    return1 = 0    
    return2 = 0
    for a in x1 :         
        return1 += ord(a)
    for b in x2 : 
        return2 += ord(b)

    if return1 > return2:
        return x1        
    return x2
    
print(get_strong_word('z','a'))
print(get_strong_word('tom','john'))