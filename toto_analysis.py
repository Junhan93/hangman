
import toto_algorithm as tta
import random

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
        random.shuffle(tta.toto_numbers)
        winning_numbers = tta.toto_numbers[:6]
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

