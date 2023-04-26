print("Welcome to the Enneagram Personality Test!")
print("Explore the 9 Types and Discover Who You Truly Are :)")
print("-----------------------------------------------------")
print("Answer the following questions with a number between 1 and 5.")
print("1 being 'strongly disagree' and 5 being 'strongly agree'.")
print("-----------------------------------------------------")
# questions
questions = [
    "1. I am a perfectionist and always strive to do my best.",
    "2. I tend to avoid conflicts and prefer to keep the peace.",
    "3. I often put others' needs before my own.",
    "4. I have a strong desire for achievement and success.",
    "5. I value my independence and need my space.",
    "6. I am very loyal to my friends and family.",
    "7. I am very curious and enjoy exploring new ideas and experiences.",
    "8. I have a strong sense of justice and fairness.",
    "9. I am very empathetic and can easily sense other people's emotions."
]

# answers
answers = []

for question in questions:
    answer = input(question + " ")
    while answer not in ['1', '2', '3', '4', '5']:
        answer = input("Please enter a number from 1 to 5: ")
    answers.append(int(answer))

# Enneagram types
types = {
    1: "Perfectionist",
    2: "Helper",
    3: "Achiever",
    4: "Individualist",
    5: "Investigator",
    6: "Loyalist",
    7: "Enthusiast",
    8: "Challenger",
    9: "Peacemaker"
}

# scoring
scores = [0] * 9
for answer in answers:
    scores[0] += 6 - answer
    scores[1] += answer - 1
    scores[2] += answer - 1
    scores[3] += 6 - answer
    scores[4] += answer - 1
    scores[5] += 6 - answer
    scores[6] += answer - 1
    scores[7] += 6 - answer
    scores[8] += answer - 1

# results
result = max(range(len(scores)), key=scores.__getitem__)
print("\nYour Enneagram type is: " + types[result+1])
print("Thank you for taking the test!")
