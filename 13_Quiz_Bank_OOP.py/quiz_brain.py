
# create a class called QuizBrain that takes one argument: question_list
# the class should have an attribute called question_number that is initialized to 0
# the class should have an attribute called score that is initialized to 0
import os


class QuizBrain:

    # create a method called __init__ that takes two arguments: self and question_list
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    # create a method called still_has_questions that takes one argument: self
    def next_question(self):
        # create a variable called current_question that is initialized to the question at the index of question_number in question_list
        current_question = self.question_list[self.question_number]
        # increment question_number by 1
        self.question_number += 1

        # prompt the user to answer the current question
        user_answer = input(f"Q.{self.question_number}: {current_question.text}: ")
        # check if the user's answer is correct
        self.check_answer(user_answer, current_question.answer)

        # ask the user if he/she wants to continue the quiz or not
        response = input("Do you want to continue the quiz? (y/n): ")
        if response.lower() == "y":
            # if the user wants to continue the quiz, call the next_question method again but check if there are still questions left first

            if self.still_has_questions():

                os.system("cls" if os.name == "nt" else "clear")

                self.next_question()

            else:
                print("You've completed the quiz.")
                print(f"Your final score was: {self.score}/{self.question_number}")
        else:
            # if the user doesn't want to continue the quiz, print "Thanks for playing!"
            print("Thanks for playing!")
            print(f"Your final score was: {self.score}/{self.question_number}")


    # create a method called check_answer that takes three arguments: self, user_answer, and correct_answer   
    def check_answer(self, user_answer, correct_answer):
        # if the user's answer is correct
        if user_answer.lower() == correct_answer.lower():
            # print "You got it right!"
            print("You got it right!")
            # increment score by 1
            self.score += 1
        # otherwise
        else:
            # print "That's wrong."
            print("That's wrong.")

            # print the correct answer
            print(f"The correct answer was: {correct_answer}")

        # print the current score
        print(f"Your current score is: {self.score}/{self.question_number}")


# create a method called still_has_questions that takes one argument: self
    def still_has_questions(self):
        # if question_number is less than the length of question_list
        if self.question_number < len(self.question_list):
            # return True
            return True
        # otherwise
        else:
            # return False
            return False
    

    def __repr__(self):
        return f"QuizBrain({self.question_list})"
    

    def __str__(self):
        return f"QuizBrain({self.question_list})"
    

    def __len__(self):
        return len(self.question_list)
    

    def __getitem__(self, index):
        return self.question_list[index]
    

    def __setitem__(self, index, value):
        self.question_list[index] = value
    

