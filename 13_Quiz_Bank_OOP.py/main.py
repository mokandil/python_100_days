# create a list of Question objects from the list of dictionaries
# the list of Question objects should be saved in a variable called question_bank

from data import data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(question['question'], question['correct_answer']) for question in data]

# create a QuizBrain object and pass in the list of Question objects
quiz = QuizBrain(question_bank)

# test it
quiz.next_question()

