
import random

toto_numbers = [
    1,2,3,4,5,6,7,
    8,9,10,11,12,13,14,
    15,16,17,18,19,20,21,
    22,23,24,25,26,27,28,
    29,30,31,32,33,34,35,
    36,37,38,39,40,41,42,
    43,44,45,46,47,48,49
]
random.shuffle(toto_numbers)

winning_numbers = []
winning_numbers = toto_numbers[:7]

maximum_number = 6
numbers_chosen = []
tallied_numbers = []
str_tallied_numbers = ""

print("Welcome to Singapore Whirlpools")
print("Enter 6      : Quick Pick")
print("Enter 7 to 12: System Entry")

option = int(input("Choose your game type: "))
print()
# option = 12

# choosing gameplay 
while option <= 5 or option >= 13:
    print("The number you entered have no assignment. Please choose between 6 and 12.")
    option = int(input("Choose your game type: "))

if option == 6:
    while len(numbers_chosen) < maximum_number:
        select_numbers = int(input("Choose number: "))

        if select_numbers in numbers_chosen:
            print("You have picked this number.")
        elif select_numbers > 49 or select_numbers < 1:
            print("Hello....know how to play one or not? Toto number until 49 only leh...")
        else:
            numbers_chosen.append(select_numbers)
            print(numbers_chosen, len(numbers_chosen))
    else:
        numbers_chosen.sort()
        numbers_chosen_final = " ".join(str(chosen) for chosen in numbers_chosen)
        print("You quick picked this numbers: "+ numbers_chosen_final)

elif option >= 7 and option <= 12:
    while len(numbers_chosen) < option:
        select_number = random.randint(1, 49)
        if select_number not in numbers_chosen: 
            numbers_chosen.append(select_number)
    else:
        numbers_chosen.sort()
        numbers_chosen_final = " ".join(str(chosen) for chosen in numbers_chosen)
        print("You drew a ticket for System "+str(option)+": "+ numbers_chosen_final)


# output draw numbers
winning_numbers.sort()
normal_number = " ".join(str(toto) for toto in winning_numbers[:-1])
add_number = winning_numbers[-1]

print("Winning Numbers: "+ normal_number)
print("Additional Number: "+ str(add_number))

def tally_winnings(numbers_chosen, winning_numbers, tallied_numbers):
    for number in numbers_chosen:
        if number in winning_numbers:
            tallied_numbers.append(number)

    str_tallied_numbers = " ".join(str(tally) for tally in tallied_numbers)

    # print the outcome
    if len(tallied_numbers) == 0:
        print("Walao, not a single number won!")
    elif len(tallied_numbers) > 3 and add_number in tallied_numbers:
        if   len(tallied_numbers) == 4: print("Your numbers " + str_tallied_numbers + " made you a Group 6 winner!") 
        elif len(tallied_numbers) == 5: print("Your numbers " + str_tallied_numbers + " made you a Group 4 winner!") 
        elif len(tallied_numbers) == 6: print("Your numbers " + str_tallied_numbers + " made you a Group 2 winner!") 
    elif len(tallied_numbers) >= 3 and add_number not in tallied_numbers:
        if   len(tallied_numbers) == 3: print("Your numbers " + str_tallied_numbers + " made you a Group 7 winner!")  
        elif len(tallied_numbers) == 4: print("Your numbers " + str_tallied_numbers + " made you a Group 5 winner!") 
        elif len(tallied_numbers) == 5: print("Your numbers " + str_tallied_numbers + " made you a Group 3 winner!") 
        elif len(tallied_numbers) == 6: print("Your numbers " + str_tallied_numbers + " made you a Group 1 (Jackpot) winner!") 
    else:
        print("Wa sian, only tio " + str_tallied_numbers + " not enough to win prize leh... next week try again!")

tally_winnings(numbers_chosen, winning_numbers, tallied_numbers)




