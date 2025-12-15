number = input("ჩაწერე სასურველი რიცხვი").strip()
while not number.isdigit():
    number = input (f"შემოტანილი სიმბოლო არ არის რიცხვი,რაც არასწორია! ჩაწერე მხოლოდ რიცხვი:").strip()
def fibbonacci (num):
    fibbo_list = [0, 1]
    for i in range(int(num) - 2):
        next_number = fibbo_list[-1] + fibbo_list[-2]
        fibbo_list.append(next_number)
    return fibbo_list
print(fibbonacci(number))
