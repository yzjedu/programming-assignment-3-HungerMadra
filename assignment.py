# Programmer: [Anierobi Eziolise]
# Course: CS701/GB-731, Dr. Yalew
# Date: [08-13-2024]
# Programming Assignment: 3
# Program Inputs: A string containing answer
# Program Outputs: Very good(If 100% correct) or Missed number and Score Presentage

def main():
    # Define a string containing the correct answers.
    CORRECT_ANSWERS = "adbdcacbdac"
    
    # Step 1: Input Validation
    # Prompt the user to enter their exam answers.
    # Ensure that the number of answers matches the number of questions.
    # If not, display an error message and prompt again.
    
    user_answers = ""
    
    while len(user_answers) != len(CORRECT_ANSWERS):
        user_answers = input("Enter your answers (e.g., 'Each question has four possible choices: a, b, c, or d'): ")
        if len(user_answers) != len(CORRECT_ANSWERS):
            print("Error: Number of answers does not match the number of questions. (Hint: there are 11 questions)")
            user_answers = input("Enter your answers (e.g., 'Each question has four possible choices: a, b, c, or d'): ") #implement modification read
    
    # Step 2: Check Exam
    # Compare each answer from the user to the corresponding correct answer.
    # Keep track of the number of correct answers.
    # Build a string showing correct answers and 'X' for incorrect ones.
    
    result_string = ""
    correct_count = 0
    
    for i in range(len(CORRECT_ANSWERS)):
        if user_answers[i] == CORRECT_ANSWERS[i]:
            result_string += user_answers[i]
            correct_count += 1
        else:
            result_string += 'X'
    
    # Step 3: Grade Exam
    # Calculate the user's score as a percentage and display it.
    score_percentage = (correct_count / len(CORRECT_ANSWERS)) * 100
    print("Your answers: ", user_answers)
    print("Correct answers: ",CORRECT_ANSWERS)
    print("Results: ",result_string)
    print("Your score: ", score_percentage, "%")
    
    # Provide feedback if the user scores 100%.
    if score_percentage == 100:
        print("Congratulations! You scored 100%!")

if __name__ == "__main__":
    main()