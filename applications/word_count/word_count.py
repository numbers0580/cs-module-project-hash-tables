def word_count(s):
    # Your code here
    symbols = ['"', ',', '.', ':', ';', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

    cache = {}

    if s == "":
        return {}
    else:
        for x in s.lower().split():
            # Went to w3schools.com to test.
            # For the 'Hello, my cat. And my cat doesn\'t say "hello" back.' string...
            # Found x = ["hello,", "my", "cat.", "and", "my", "cat", "doesn't", "say", "\"hello\"", "back."]

            temp = ""
            # Getting each character of each word and only appending non-symbols to the temp string.
            # Once the non-symbol word has been fully concatenated, we'll store that back to x
            for c in x:
                if c not in symbols:
                    temp += c
            x = temp

            if x in cache:
                # Found a duplicate word, increment it's count
                cache[x] += 1
            elif x == "" or x == " ":
                # Empty string
                break
            else:
                # Found a new word
                cache[x] = 1

        return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))