# Define a dictionary with trivia questions and answers
trivia_questions = {
    "What is the capital of France?": "Paris",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the largest mammal?": "Blue whale",
    "What is the chemical symbol for water?": "H2O",
    "Which planet is known as the Red Planet?": "Mars"
}

# Initialize variables to track correct answers and total questions
correct_answers = 0
total_questions = len(trivia_questions)

# Iterate through the dictionary and ask questions
for question, answer in trivia_questions.items():
    print(question)
    user_answer = input("Your answer: ")
    if user_answer.lower() == answer.lower():
        print("Correct!\n")
        correct_answers += 1
    else:
        print("Incorrect. The correct answer is:", answer, "\n")

# Calculate the score and display the result
score = (correct_answers / total_questions) * 100
print("You answered", correct_answers, "out of", total_questions, "questions correctly.")
print("Your score:", score, "%")