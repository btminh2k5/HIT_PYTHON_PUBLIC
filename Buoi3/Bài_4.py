def normalize_name(name):
    tmp = ' '.join(name.split())
    
    lst = tmp.split()
    normalized_words = []
    
    for word in lst:
        if len(word) > 0:
            tmp2 = word[0].upper() + word[1:].lower()
            normalized_words.append(tmp2)
    
    normalized_name = ' '.join(normalized_words)
    return normalized_name

s = input()
print(normalize_name(s))