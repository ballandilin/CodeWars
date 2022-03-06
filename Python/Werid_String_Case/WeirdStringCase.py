def to_weird_case(word):
    
    
    

    if " " in word:
        word = word.split(" ")
        word_copy = []
    
        for i in range(len(word)):
    
            for j in range(len(word[i])):
                if j%2:
                    word_copy.append(word[i][j])
                else:
                    word_copy.append(word[i][j].upper())
    
            if i < len(word)-1:
                word_copy.append(" ")

    else:
        word_copy = ""
        for i in range(len(word)):
            if i%2:
                word_copy += word[i]
            else:
                word_copy += word[i].upper()
    
    
    word = "".join(word_copy)
    print(word)
    return word