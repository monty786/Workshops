__author__ = 'jc437351'

PICK_COLOR = {"AliceBlue": "f0f8ff", "azure1": "f0ffff","azure2": "e0eeee","azure3": "c1cdcd","azure1" :"838b8b","bisque1": "ffe4c4","bisque2": "eed5b7","bisque3": "cdb79e","bisque4": "8b7d6b"}
color= input("Enter the color name: ")
while color != "":
    if color in PICK_COLOR:
        print(color,"for",PICK_COLOR[color])
    else:
        print("invalid color name")
    color = input("Enter color name: ")
for key in PICK_COLOR:
    print("{} is {}".format(key,PICK_COLOR[key]))
