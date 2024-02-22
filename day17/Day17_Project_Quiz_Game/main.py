# main.py
# Day17 Project - Quiz Game
"""
Quiz Game Project:
    In this program the user is asked a series of questions,
    which are selected at random.

    The user inputs an answer either True or False.
    The program only takes the first character into consideration.
    the input is not case-sensitive.

    The total number of questions that the user is given is
    defined in the 'MAX_QUESTIONS' variable.
    There are a total of 20 available questions to be selected.

    The program will keep track of the user's score.
    The program loops until all questions have been answered.
    The user is given a message depending on their score at the
    end of the quiz.
"""
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import sys
import os
import random
MAX_QUESTIONS = 10


def clear_screen():
    OS = sys.platform
    if OS.startswith('linux') or OS.startswith('darwin'):
        os.system('clear')
    else:
        os.system('cls')


def check_for_duplicates(q_item, q_list):
    has_duplicate = False
    if q_list == []:
        return has_duplicate
    for item in q_list:
        if q_item.text == item.text:
            has_duplicate = True
    return has_duplicate


question_bank = []
while len(question_bank) < MAX_QUESTIONS:
    item = random.choice(question_data)
    new_question = Question(item["question"], item["correct_answer"])
    if not check_for_duplicates(new_question, question_bank):
        question_bank.append(new_question)
    else:
        continue

quiz = QuizBrain(question_bank)

clear_screen()
while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz!")
quiz.print_final_score()
