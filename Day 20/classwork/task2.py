#2)1 დან 100 მდე დაბეჭდეთ ყოველი ლუწი რიცხვი და მიუწერეთ მათ რომ ლუწია, შემდეგ 1 და 100 მდე დაბეჭდეთ ყოველი კენტი რიცხვი და მიუწერეთ რომ კენტია, გამოიყენეთ მხოლოდ ლუპი


# 1-დან 100-მდე ლუწი და კენტი რიცხვების დაბეჭდვა

for num in range(1, 101):
    if num % 2 == 0:
        print(f"{num} ლუწი")
    else:
        print(f"{num} კენტი")


#ეს კოდი გადის რიცხვებზე 1-დან 100-მდე. თუ რიცხვი ლუწია (დაიყოფა 2-ზე ნაშთის გარეშე), მაშინ ბეჭდავს "ლუწი", ხოლო თუ კენტია, ბეჭდავს "კენტი".
