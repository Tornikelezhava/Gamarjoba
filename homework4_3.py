import random
word = input("შემოიყვანე მხოლოდ ერთი სიტყვა:")
while len(word.strip().split())>1 or word.isdigit():
    word = input("ახლიდან ჩაწერე რიცხვი")
adding = ["123","012","007","2005","999"]
def nickname (word, adding):
    for part in adding:
        print(f"{word}{part}")
nickname(word, adding)



