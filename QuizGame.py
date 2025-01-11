def new_game():
    
     guesses = []
     correct_guesses = 0
     question_num = 1
     
     for key in questions:
         print("--------------------")
         print(key)
         for i in options[question_num-1]:
             print(i)
             
         guess = input("Enter (A, B or C): ") 
         guess = guess.upper()
         guesses.append(guess)
         correct_guesses += check_answers(questions.get(key), guess)
         question_num += 1
     display_score(correct_guesses, guesses)
     
def check_answers(answer, guess):
    
    if answer == guess:
        print("You are correct. Congrats !!!")
        return 1
    else:
        print("You are wrong !")
        return 0 
    
def display_score(correct_guesses, guesses):
    print("--------------------")
    print("Results")
    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    
    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()
    
    score = int((correct_guesses/len(questions))*100)
    print("Your score is: " +str(score)+"%")
        
def play_again():
    response = input("Do you want to play again? (Yes/No): ").lower()
    if response != "yes":
        return False
    else:
        return True

questions = {
    "What is the largest planet in our solar system?: " : "A",
    "Do you think aliens really exist?: " : "B",
    "What is the process in which plants convert sunlight into energy?: " : "C",
    "What is the fastest animal in the world?:" : "A"
    }

options = [["A. Jupiter", "B. Earth", "C. Mercury"],
           ["A. Yes, I do", "B. No, they are just myth","C. I don't know exactly"],
           ["A. Lightining", "B. Reproduction", "C. Photosynthesis"],
           ["A. Falcon", "B. Cheetahe", "C. Panthera"]]

new_game()

while play_again():
    new_game()
    
print("Byeeee!")
