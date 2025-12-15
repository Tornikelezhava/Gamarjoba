import random
numlist = input("შემოიყვანე სხვადახვა რიცხვები:").strip().split(" ")

def correct(text):
    for num in text:
        if not num.isdigit():
            return False
    return True

while not correct(numlist):
    numlist = input("შემოიყვანე სხვადახვა რიცხვები:").strip().split(" ")
sort_type =  input("როგორი სორტირება გინდა? random, კლებადობით, ზრდადობით, უნიკალური:")

while sort_type not in ["random", "კლებადობით", "ზრდადობით", "უნიკალური"]:
    sort_type = input("შემოიყვანე სწორი ბრძანება!")

for i in range(len(numlist)):
    numlist[i] = int(numlist[i])
if sort_type == "random":
    random.shuffle(numlist)
if sort_type == "ზრდადობით":
    numlist.sort()
if sort_type == "კლებადობით":
    numlist.sort(reverse=True)
if sort_type == "უნიკალური":
    numlist = list(set(numlist))
print (numlist)