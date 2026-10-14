f = open("data.txt", "r")
data = f.read()

words = data.split()

print("Total words:", len(words))

unique = set(words)
print("Unique words:", unique)

f.close()