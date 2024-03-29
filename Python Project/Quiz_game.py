print("welcome to my Computer Quiz")
playing = input("Do ypou want to play?(y/n): ")
if playing != "y":
    quit()
print("================================================================")
quetion_Answer = [
    {'question':"What does CPU stand for? ", 'answer':"central processing unit"},
    {'question':"What does PC stand for? ",'answer':"personal computer"},
    {'question': 'What does RAM stand for?', 'answer': 'random access memory'},
    {'question': 'What does GPU stand for?', 'answer': 'graphics processing unit'}
    ]

def play_quiz(quetion_Answer):
    """
        This function takes a list of dictionaries as input, where each dictionary represents a question and its answer.
        The function prompts the user with each question, checks if the user's input matches the correct answer, and updates the score accordingly.
        At the end of the quiz, the function prints the score and grade.

        Parameters:
        quetion_Answer (list): A list of dictionaries, where each dictionary represents a question and its answer.

        Returns:
        None

    """
    score = 0
    for item in quetion_Answer:
        question = item['question']
        correct_answer = item['answer']
        user_answer = input(question + '\nYour answer: ').lower()
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect! The correct answer is:", correct_answer)
        print("================================================================")  # Add a newline for better readability

    percentage = (score / len(quetion_Answer)) * 100
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "F"
        
    print("Quiz completed! You scored", score, "out of", len(quetion_Answer))
    print("Percentage:", percentage, "%")
    print("Grade:", grade)
    
play_quiz(quetion_Answer)