CharacterCount = 0
wordCount = 1

intro = input("Please give us your intro\n\n")

for i in intro:
    CharacterCount = CharacterCount + 1
    if (i == ' '):
        wordCount += 1

print("\nWords: ", wordCount)
print("Character: ", CharacterCount)
