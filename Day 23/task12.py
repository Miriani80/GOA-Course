#5)დაწერეთ პროგრამა რომელიც ბეჭდავს ყველა რიცხვს 1-100 მდე რომელიც იყოფა 3-ზე და 5-ზე


# რიცხვების გადაკვრა 1-დან 100-მდე
for i in range(1, 101):
    # შემოწმება, არის თუ არა რიცხვი 3-სა და 5-ზე გაყოფადი
    if i % 3 == 0 and i % 5 == 0:
        print(i)
ახსნა:
for i in range(1, 101):: range(1, 101) ქმნის რიცხვების სექვენციას 1-დან 100-მდე (100-ის ჩათვლით).

if i % 3 == 0 and i % 5 == 0:: ამ პირობით შემოწმდება, არის თუ არა რიცხვი i 3-სა და 5-ზე გაყოფადი. % ოპერატორი აჩვენებს, დარჩება თუ არა დანარჩენი რიცხვის გაყოფისას.

print(i): დაბეჭდავს იმ რიცხვებს, რომლებიც აკმაყოფილებენ პირობას.

ამ პროგრამას გაავლებს ყველა რიცხვს 1-დან 100-მდე, რომლებიც გაყოფილია როგორც 3-ზე, ისე 5-ზე.