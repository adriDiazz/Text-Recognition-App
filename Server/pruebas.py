text = r"b'wwww\n'"
separator = r"\n"

splited = text.split(separator)
for palabra in splited:
    if palabra == "'":
        splited.remove(palabra)
unido = ''.join(splited)

splited2 = unido.split("'")

for palabra in splited2:
    if palabra == "b":
        splited2.remove(palabra)
rawData = ''.join(splited2)

    
