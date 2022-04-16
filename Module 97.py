intro = input( "Enter your name: ")
charactercount = 0
wordCount = 1

for i in intro:
    charactercount = charactercount + 1
    if( i == ' '):
        wordCount = wordCount + 1

print("Number of words in your name:")
print(wordCount)
print("Number of Characters in your name: ")
print(charactercount)
