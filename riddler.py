import csv
import bcrypt
with open('riddles_encrypted_answers.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    riddles = []
    answers = []
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            riddles.append(row[1])
            answers.append(bytes(row[2][2:-1], encoding='utf-8'))
            line_count += 1
    #print(f'Processed {line_count} lines.')
salt = b'$2b$12$bJS3eJyNaenoz7XhI9bTKe'
print(len(riddles), "riddles")
for i in range(len(riddles)):
    answer = answers[i]
    print(riddles[i])
    reanswer = True
    while reanswer:
        guess = input()
        guess = bytes(guess.capitalize(), encoding='utf-8')
        guess = bcrypt.hashpw(guess, salt)
        if guess == answer:
            reanswer = False
            print("Correct!")
        else:
            print("Incorrect")
