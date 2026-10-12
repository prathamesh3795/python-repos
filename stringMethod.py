text=" I am Prathamesh"  

print("Upper Case :",text.upper())#uppercase

text= text.strip()#

print("Capitalized :",text.capitalize())

print(text.title())

print("Letter C Occur",text.count("c"),"times in text")

print("Position of prathamesh is",text.find("Prathamesh"))

print(text.replace("am","was"))

print(text.startswith("Pra"))
print(text.endswith(" h"))

print(text.split())

word=["Python","is","fun"]
print(" ".join(word))

# a=input("Enter string:")
# count=a.count('a')+a.count('e')+a.count('i')+a.count('o')+a.count('u')+a.count('A')+a.count('E')+a.count('I')+a.count('O')+a.count('U')
# print(count)

# txt="ha"
# print(txt*3)

a="Prathamesh"
b=a.replace('a','z')
print(b)

print(a.split())

print(sorted(a))