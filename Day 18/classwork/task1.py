#მომხმარებელს შემოატანინოთ რიცხვი, შემდეგ კი დაბეჭდეთ ეს რიცხვი კენტია თუ ლუწი

# Ask the user to enter a number
user_input = int(input("10"))

# Check if the number is even or odd
if user_input % 2 == 0:
    print(f"თქვენმა რიცხვმა {user_input} არის ლუწი.")
else:
    print(f"თქვენმა რიცხვმა {user_input} არის კენტი.")

