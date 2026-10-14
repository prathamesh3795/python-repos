sentence = input("Enter a sentence: ")

words = sentence.split()

if words:
    longest = max(words, key=len)
    print("Longest word:", longest)
else:
    print("No words entered")