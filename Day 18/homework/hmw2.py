#2) თქვენით მოიფიქრეთ რაიმე სავარჯიშო რასაც გააკეთებთ if elif else ით ივარჯიშეთ დღევანდელ ნასწავლ მასალაზე ძალიან ბევრი




def categorize_age(age):
    if age < 0:
        return "შეყვანილი ასაკი არ შეიძლება იყოს უარყოფითი."
    elif age <= 2:
        return "თქვენ ბავშვი ხართ (0-2 წლები)."
    elif age <= 5:
        return "თქვენ სკოლამდელი ასაკის ბავშვი ხართ."
    elif age <= 12:
        return "თქვენ სასკოლო ასაკის ბავშვი ხართ."
    elif age <= 19:
        return "თქვენ თინეიჯერი ხართ."
    elif age <= 64:
        return "თქვენ ზრდასრული ხართ."
    elif age <= 120:
        return "თქვენ ხანდაზმული ხართ."
    else:
        return "შეყვანილი ასაკი არარეალურია."

while True:
    age = int(input("შეიყვანეთ თქვენი ასაკი: "))
    print(categorize_age(age))
    
    choice = input("გსურთ სხვა ასაკის შეყვანა? (დიახ/არა): ").lower()
    if choice != 'დიახ':
        break