import json, random

filtered8LetterWords = []

print("Manually filter words and shuffles.")
print("<Enter> accepts the word and it's shuffle.")
print("'x' <Enter> ends the program and writes the accepted words to _filtered8LetterWords.js")
print("any other key rejects the word and it's shuffle.")


with open(f'wordsin.csv') as file:
    content = file.read()
    words = content.split('\n')
    for word in words:
        shuff = ''.join(random.sample(word,len(word)))
        print(len(filtered8LetterWords), word, shuff)
        i = input()
        if ( i == 'x'):
            break
        elif (i == ''):
            filtered8LetterWords.append((word, shuff))
        else:
            print("rejecting")

with open(f'_filtered8LetterWords.js', 'w') as outfile:
    outfile.write("const words = ")
    outfile.write(json.dumps(filtered8LetterWords))
    outfile.write("\nexport default { words }")

print("Goodbye.")
