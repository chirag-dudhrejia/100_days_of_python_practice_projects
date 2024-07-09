import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_num = 0
        self.current_question = None
        self.questions_list = q_list
        self.score = 0

    def has_next_question(self):
        return self.question_num < len(self.questions_list)

    def get_next_question(self):
        self.current_question = self.questions_list[self.question_num]
        self.question_num += 1
        return f"Q{self.question_num} : {html.unescape(self.current_question.text)}"
        # user_answer = input(f"Q{self.question_num} : {html.unescape(self.current_question.text)} : ")

    def check_answer(self, user_ans: str):
        if self.current_question.ans.lower() == user_ans:
            self.score += 1
            return True
        else:
            return False