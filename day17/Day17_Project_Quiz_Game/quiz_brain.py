# quiz_brain.py
class QuizBrain():
    def __init__(self, questions=[]):
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def next_question(self):
        q = self.question_list[self.question_number]
        self.question_number += 1
        q_num = self.question_number
        user_answer = input(f"Q{q_num}: {q.text} (True/False)?: ").lower()
        if user_answer == "":
            user_answer = "pass"
            print("You chose to pass on the question.")
        self.check_answer(user_answer, q.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, u_answer, q_answer):
        is_correct = u_answer[0] == q_answer[0].lower()
        if is_correct:
            print("You got it right!")
            self.score += 1
        else:
            if u_answer != "pass":
                print("That's incorrect!")
        print(f"The correct answer was: {q_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")

    def print_final_score(self):
        q_total = len(self.question_list)
        percentage_score = (self.score / q_total) * 100
        message = ""
        if percentage_score <= 50:
            # 50% or less
            message = "Good effort, keep trying!"
        elif 50 < percentage_score < 70:
            # between 50% and 70%
            message = "Almost there, keep practicing!"
        elif 70 <= percentage_score < 90:
            # between 70% and 90%
            message = "Great Work, you're making progress!"
        else:
            # above 90%
            message = "You're amazing! Keep up the good work!"
        print(f"You're final score is: {self.score}/{q_total}")
        print(message)
