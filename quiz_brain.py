# TODO: asking questions
# TODO: Checking the answer
# TODO: check if the quiz eneded

class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    

    def still_has_questions(self):
        return len(self.question_list) > self.question_number
            

    def check_answer(self, correct_answr, user_answr):
        if correct_answr.lower() == user_answr.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answr}")
        print(f'Your current score is: {self.score}/{self.question_number}.')
        print("\n")


    def next_question(self):
        next_quest = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {next_quest.text} (True/False)?: ")
        self.check_answer(next_quest.answer, answer)
        
