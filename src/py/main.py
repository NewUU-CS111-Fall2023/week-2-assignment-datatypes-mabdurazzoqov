# * Mirzohid Abdurazzoqov:
# * 25.10.2023:

import algo1
import algo2
import algo4
import algo5

print("Task 1")
y = int(input("Enter a year: "))
print(f"{y} is a leap year." if algo1.leapYear(y) else f"{y} is not a leap year.")


print("Task 2")
n = algo2.randomNumber()
algo2.playGame(n)

print("Task 4")
s = input("Enter a sentence: ")
w = input("Enter a word: ")
r = algo4.checkWord(s, w)

if r[0]:
    print("The word was found at index", r[1])
else:
    print("No match")


print("Task 5")
N = int(input("Enter the number of coordinates: "))
c = []
for i in range(N):
    x, y = map(int, input(f"Enter the x and y coordinates for drop-off {i + 1}: ").split())
    c.append((x, y))

for i in range(N):
    print(f"Dropping off character at ({c[i][0]}, {c[i][1]})")
    if algo5.spawnEnemies(c[i]):
        print("The character died")
    else:
        print("The character survived")