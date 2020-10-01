def no_dups(s):
    # Your code here
    cache = {}
    word = s.split() # parse to individual words

    temp = "" # like word_count, create an empty string to use in for-loop

    for c in word:
        # parsed each word to individual characters (not testing for symbols or capital letters, this time)
        if c not in cache:
            cache[c] = 1 # Just giving c some arbitrary value so it'll be found on duplicates
            temp += f"{c} " # Appending only the first iteration of the word found. Left a trailing space, but will strip last space after loop
    return temp.strip()



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))