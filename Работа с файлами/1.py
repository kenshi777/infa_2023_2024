with open('cheshki.txt', 'r') as file:
    for line in file.readlines():
        print(line[:-1])

