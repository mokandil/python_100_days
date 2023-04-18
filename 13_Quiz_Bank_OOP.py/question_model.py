# create a class called Question that takes two arguments: text and answer

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
    
    # create a method called __repr__ that takes one argument: self
    # the method should return a string that contains the text of the question
    def __repr__(self):
        return self.text
    
    # create a method called __str__ that takes one argument: self
    # the method should return a string that contains the text of the question
    def __str__(self):
        return self.text

    