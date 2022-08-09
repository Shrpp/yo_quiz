from api import random_data

questions_bank = []

class Question():
    
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
        
        
class QuizBrain:
    
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        
    def next_question(self):
        current_question = self.question_list [self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}): {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
        
    def still_has_question(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
        
        
for question in random_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    questions_bank.append(new_question)

quiz = QuizBrain(questions_bank)

while quiz.still_has_question():
    quiz.next_question()
    
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")