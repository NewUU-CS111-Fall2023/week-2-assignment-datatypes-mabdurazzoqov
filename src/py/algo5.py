import random


def spawnEnemies(c):
    n = random.randint(1, 10)
    if c[0] <= n <= c[1]:
        return True
    else:
        return False
