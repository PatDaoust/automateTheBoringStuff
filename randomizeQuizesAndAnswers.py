# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 17:23:58 2022

@author: catal
"""

"""
you’re a geography teacher with 35 students in your class
you want to give a pop quiz on US state capitals.
Alas, your class has a few bad eggs in it, and you can’t trust the students not to cheat.
You’d like to randomize the order of questions so that each quiz is unique,
making it impossible for anyone to crib answers from anyone else.
Of course, doing this by hand would be a lengthy and boring affair.
Fortunately, you know some Python.

Here is what the program does:

Creates 35 different quizzes.
Creates 50 multiple-choice questions for each quiz, in random order.
Provides the correct answer and three random wrong answers for each question, in random order.
Writes the quizzes to 35 text files.
Writes the answer keys to 35 text files.
"""

"""
potential_questions format: dict()
values = string = question
value = string = answer


quiz format
header
Question 1: key
a. rand
b. value
c. rand
d. rand

x questions_per_quiz

answer key format
Question 1. a.

"""


def randomizeQuizesAndAnswers(potential_questions,
                              questions_per_quiz,
                              quiz_num,
                              destination_folder):
    """assumes potential_questions is a dict, with keys representing the questions
    and values representing correct answers
    assumes questions_per_quiz is an int, representing the number of questions in a quiz
    assumes quiz_num is an int, representing the number of quizes to be generated
    assumes destination_folder is a string, representing the path to store the generated quizzes
    returns None
    creates 2*quiz_num of files"""
    # test that questions_per_quiz > len(potential_questions)
    # TODO outline plan
    pass
