import random

def generateUsername():
    with open("words.txt", 'r') as file:
        data = file.read().splitlines()

    userNumber = random.randint(0,1000)
    if random.randint(0,2) == 1:
        username = random.choice(data)
        return username + str(userNumber)
    else:
        username = random.choice(data) + random.choice(data)
        return username + str(userNumber)

print(generateUsername())