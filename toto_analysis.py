
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
winning_numbers = []
analysis = []

max_n = 6
selected = []
while len(selected) < max_n:
    number = random.randint(1,49)
    if number not in selected:
        selected.append(number)

selected.sort()
# winning numbers
print("Winning number: ", selected)

tally = []
def generate_sets(iter):
    count = 0
    for x in range(iter):
        random.shuffle(toto_numbers)
        winning_numbers = toto_numbers[:6]
        analysis.append(winning_numbers)

    return analysis

generate_sets(5)

count = 0
for ticket in analysis:
    print(ticket)
    if ticket == selected:
        print(ticket)
    else:
        count +=1
        print(count, "tries for matching", selected)

# not completed

