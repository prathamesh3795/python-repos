f = open("data.txt", "r")
lines = f.readlines()

print("Total lines:", len(lines))

if len(lines) >= 2:
    print("2nd line:", lines[1].strip())

if len(lines) >= 4:
    print("4th line:", lines[3].strip())

f.close()