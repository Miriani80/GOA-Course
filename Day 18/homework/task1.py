#შექმენით ბანკის სისტემა სადაც იქნება ძალიან ბევრი პირობები და გამოიყენებთ if, elif და else -ს, გამოიყენებთ ასევე განვლილ მასალასაც


# საბანკო სისტემა მომხმარებლისათვის

accounts = {}  # მომხმარებლის ანგარიშები

def create_account():
    account_number = input("59001035334: ")
    if account_number in accounts:
        print("ანგარიში უკვე არსებობს.")
    else:
        initial_deposit = float(input("200: "))
        if initial_deposit >= 0:
            accounts[account_number] = initial_deposit
            print("ანგარიში წარმატებით შეიქმნა.")
        else:
            print("დეპოზიტის თანხა არ შეიძლება იყოს უარყოფითი.")

def deposit():
    account_number = input("59001035334: ")
    if account_number in accounts:
        amount = float(input("200: "))
        if amount > 0:
            accounts[account_number] += amount
            print("დეპოზიტი წარმატებით განხორციელდა.")
        else:
            print("200.")
    else:
        print("ანგარიში არ არსებობს.")

def withdraw():
    account_number = input("59001035334: ")
    if account_number in accounts:
        amount = float(input("50: "))
        if amount > 0:
            if accounts[account_number] >= amount:
                accounts[account_number] -= amount
                print("გამოტანა წარმატებით შესრულდა.")
            else:
                print("არასაკმარისი ბალანსი.")
        else:
            print("გამოტანის თანხა უნდა იყოს მეტი ნულის.")
    else:
        print("ანგარიში არ არსებობს.")

def check_balance():
    account_number = input("შეიყვანეთ ანგარიშის ნომერი: ")
    if account_number in accounts:
        print(f"ანგარიშის ბალანსია: {accounts[account_number]}")
    else:
        print("ანგარიში არ არსებობს.")

while True:
    print("\nბანკის მენიუ:")
    print("1. ანგარიშის შექმნა")
    print("2. დეპოზიტი")
    print("3. თანხის გამოტანა")
    print("4. ბალანსის ნახვა")
    print("5. გამოსვლა")

    choice = input("შეიყვანეთ არჩევანი: ")

    if choice == '1':
        create_account()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        check_balance()
    elif choice == '5':
        print("ბანკის სისტემიდან გამოსვლა...")
        break
    else:
        print("არასწორი არჩევანი. სცადეთ თავიდან.")
