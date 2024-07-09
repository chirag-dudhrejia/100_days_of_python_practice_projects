from data import question_data
from question_structure import Question
from quiz_brain import QuizBrain
from UI import QuizInterface


question_bank = []
for question in question_data:
    question_text = question["question"]
    correct_answer = question["correct_answer"]
    new_question = Question(question_text, correct_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_gui = QuizInterface(quiz)

# while quiz.has_next_question():
#     quiz.get_next_question()

print(f"Final Score : {quiz.score}/{quiz.question_num}")