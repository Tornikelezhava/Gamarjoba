text = input("შეიყვანეთ ტექსტი: ")
text_upd = ""
for char in text:
    if char.isalpha() or char == " ":
        text_upd += char
print (text_upd)

