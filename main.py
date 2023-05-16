import random

print("VÍTEJ V HÁDACÍ HŘE!")
print("-------------------")

attempts = 0

level = input("Zvol obtížnost. easy/medium/hard: ")
if level == "easy":
    attempts = 9
    print(f"Máš {attempts} pokusů.")
elif level == "medium":
    attempts = 6
    print(f"Máš {attempts} pokusů.")
else:
    attempts = 3
    print(f"Máš {attempts} pokusů.")  
    
    
random_number = random.randint(1,50)
print(random_number)

for one_number in range(1, 51):      
    guess_number = int(input("Hádej číslo od 1 do 50: "))
    if random_number == guess_number:
        print("Jsi vítěz!")
        play_again = input("Chceš hrát znovu? ano/ne: ")
        if play_again == "ne":
            break
    elif random_number > guess_number:
        print("Tvé číslo je moc nízké.")  
        attempts -= 1 
        print(f"Zbývá ti {attempts} pokusů.")
        if attempts == 0:
            print("Prohrál jsi!")
            play_again = input("Chceš hrát znovu? ano/ne: ")
            if play_again == "ne":
                break
    elif random_number < guess_number:
        print("Tvé číslo je moc vysoké.") 
        attempts -= 1 
        print(f"Zbývá ti {attempts} pokusů.")
        if attempts == 0:
            print("Prohrál jsi!")
            play_again = input("Chceš hrát znovu? ano/ne: ")
            if play_again == "ne":
                break


        



 
