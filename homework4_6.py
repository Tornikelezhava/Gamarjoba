import random
rand_list = input("ჩაწერეთ რიცხვები, გამოყავი მძიმით:").strip().split(",")
def correct(text):
    for num in text:
        if not num.strip().isdigit():
            return False
    return True
while not correct(rand_list):
    rand_list = input("შემოიყვანე მხოლოდ რიცხვები და გამოყავი მძიმით:").strip().split(",")

for i in range(len(rand_list)):
    rand_list[i] = int(rand_list[i])

def make_new_list (old_list):
    print(old_list)
    newlist = []
    for i in range(len(old_list)-1):
        newlist.append(old_list[i]+old_list[i+1])
    return newlist

while len(rand_list)>1:
    rand_list = make_new_list(rand_list)
print(rand_list)