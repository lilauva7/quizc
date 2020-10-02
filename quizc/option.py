from quizc.console.quiz_ui_handler import *


class Option(object):
    def __init__(self):
        self.car = ""
        self.name = ""
        self.quiz = None
        self.quiz_answers = None
        should_exit = False


class CreateQuiz(Option):
    def __init__(self):
        self.name = "Create quiz"

    def process(self):
        self.quiz = QuizUIHandler.create_quiz()

class FillQuiz(Option):
    def __init__(self):
        self.name = "Fill quiz"

    def process(self):
        if self.quiz is None:
            print("No quiz available, you must create first a quiz")
        else:
            self.quiz_answers = QuizUIHandler.fill_quiz(self.quiz)


class ShowQuiz(Option):
    def __init__(self):
        self.name = "Fill quiz"

    def process(self):
        if self.quiz is None:
            print("No quiz available, you must create first a quiz")
        else:
            self.quiz_answers = QuizUIHandler.fill_quiz(self.quiz)

class Exit(Option):
    def __init__(self):
        self.name = "Exit"

    def process(self):
        return False