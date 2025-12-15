import random
pass_len = input ("რამდენი სიმბოლოსგან გინდა რომ შედგებოდეს პაროლი? (max 15)").strip()
pass_choice = ['კი','y','Y','yes','არა','n','N','no']
while not pass_len.isdigit() or int(pass_len) >=16:
    pass_len = input("პაროლის სიგრძე უნდა იყოს აუცილებლად ნატურალური რიცხვი და 15 სიმბოლოზე ნაკლები. ახლიდან სცადეთ").strip()
pass_len = int(pass_len)
incl_dig = input("გსურთ, რომ პაროლი შეიცავდეს ციფრებს? (ჩაწერეთ მხოლოდ ერთერთი კი,არა,y,n,Y,N,yes ან no").strip()
while incl_dig not in pass_choice:
    incl_dig = input("ჩაწერეთ მხოლოდ ერთერთი კი,არა,y,n,Y,N,yes ან no").strip()
incl_upp = input("გსურთ, რომ პაროლი შეიცავდეს დიდ ასოებს?ჩაწერეთ მხოლოდ ერთერთი კი,არა,y,n,Y,N,yes ან no").strip()
while incl_upp not in pass_choice:
    incl_upp = input("ჩაწერეთ მხოლოდ ერთერთი კი,არა,y,n,Y,N,yes ან no").strip()
incl_low = input ("გსურთ, რომ პაროლი შეიცავდეს პატარა ასოებს? ჩაწერეთ მხოლოდ ერთერთი კი,არა,y,n,Y,N,yes ან no").strip()
while incl_low not in pass_choice:
    incl_low = input("ჩაწერეთ მხოლოდ ერთერთი კი,არა,y,n,Y,N,yes ან no").strip()
incl_symbols = input("გსურთ, რომ პაროლი შეიცავდეს სიმბოლოებს? ჩაწერეთ მხოლოდ ერთერთი კი,არა,y,n,Y,N,yes ან no").strip()
while incl_symbols not in pass_choice:
    incl_dig = input("ჩაწერეთ მხოლოდ ერთერთი კი,არა,y,n,Y,N,yes ან no").strip()

digits = [chr(i) for i in range(ord('0'), ord('9') + 1)]
latin_capitals = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
latin_smalls = [chr(i) for i in range(ord('a'), ord('z') + 1)]
symbols = [chr(i) for i in range(33, 48)] + \
          [chr(i) for i in range(58, 65)] + \
          [chr(i) for i in range(91, 97)] + \
          [chr(i) for i in range(123, 127)]
psw_list = []
psw=""
YES = set(pass_choice[:4])
if incl_dig in YES:
    psw_list+= digits
if incl_upp in YES:
    psw_list += latin_capitals
if incl_low in YES:
    psw_list += latin_smalls
if incl_symbols in YES:
    psw_list += symbols
if len(psw_list) == 0:
    print ("სამწუხაროდ პაროლი ვერ დაგენერირდა, რადგან არ აგირჩევია არცერთი ელემენტი.")
    exit()
for i in range (int(pass_len)):
    letter = random.choice(psw_list)
    psw+=letter
print(psw)
