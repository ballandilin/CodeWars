def to_camel_case(text):

    word = [character for character in text]

    for character in range(len(word)):
        if word[character] == "-" or word[character] == "_":
            word[character] = ""
            word[character+1] = word[character+1].capitalize()

    word = "".join(word)
    return word