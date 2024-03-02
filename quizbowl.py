import sqlite3

# Connect to the database
conn = sqlite3.connect('FridayProj5 (1).db')

# Select all data from the quiz_data table
cursor = conn.cursor()
cursor.execute("SELECT question, answer FROM QuestAns;")
data = cursor.fetchall()

# Create a dictionary from the fetched data
questions = dict(data)

# Close the connection
conn.close()

print("Hello user. Play along.\n")

varCorrectanswer = 0
playTest = input("Would you like to play?: ")

while playTest.lower() == "yes":
    for question, answer in questions.items():
        print(question)

        user = input("Your answer: ")

        if user.lower() == answer.lower():
            print("\nGreat job!\n")
            varCorrectanswer += 1
        else:
            print("\nBetter luck next time kid.\n\nThe answer is", answer + ".\n")

    playTest = input("Would you like to play again?: ")
    if playTest.lower() == "yes":
        continue
    else:
        break

print("\nThanks for Playing!")
print("You got", varCorrectanswer, "questions right!")

input()