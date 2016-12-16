__author__ = 'jc437351'

vowels = ["a","e","i","o","u","A","E","I","O","U"]

vowel_count = 0

name=input("Enter your name:")

for c in name:
    if c.lower() in vowels:
        vowel_count +=1

print("out of {} letters, {} has {} vowels".format(len(name),name,vowel_count))