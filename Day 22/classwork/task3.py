#3)მომხმარებელს შემოატანინეთ რიცხვი შემდეგ while loop ის გამოყენებით 1-დან მომხმარების შემოტანილ რიცხვამდე დაბეჭდეთ მხოლოდ ხუთის ჯერადი რიცხვები


# მომხმარებელს შემოატანინეთ რიცხვი
number = int(input("შეიყვანეთ რიცხვი: "))

# საწყისი მნიშვნელობა
i = 1

# while ციკლი, რომელიც გადის 1-დან შემოტანილ რიცხვამდე
while i <= number:
    # ვამოწმებთ, არის თუ არა რიცხვი ხუთის ჯერადი
    if i % 5 == 0:
        print(i)
    # ზრდა 1-ით
    i += 1
