#მომხმარებელს შემომატანინეთ რიცხვი და შემდეგ დაბეჭდეთ მომხმარებლის შემოტანილი რიცხვი არის თუ არა ხუთის ჯერადი


# მომხმარებელს სთხოვს რიცხვის შეყვანას
number = int(input("100"))

# ამოწმებს ხუთის ჯერადობას
if number % 5 == 0:
    print(f"{number} არის ხუთის ჯერადი")
else:
    print(f"{number} არ არის ხუთის ჯერადი")
