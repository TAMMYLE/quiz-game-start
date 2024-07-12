# TODO: asking the questions
# TODO: checking if the answer was correct
# TODO: checking if we're the end of the question

class QuizBrain:

    def __init__(self, list):
        self.question_list = list
        self.question_number = 0
        self.score = 0
        

    def still_have_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        """ Returns a question of the list """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        u_response = input(f"\nQ.{self.question_number}: {current_question.machine_quest} (True/False)?: \n")   
        self.check_answer(u_response, current_question.answer) 
            
    def check_answer(self, u_response, correct_answer):

        if u_response.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
            print(f"Your current score is: {self.score}/{self.question_number}")
        else:
            print(f"That's wrong. Correct answer was {correct_answer}")
            print(f"Your current score os: {self.score}/{self.question_number}")

    def final_display(self):
        print("\n")
        print("You have completed your quiz!!!")
        print(f"Your final score is: {self.score}/{self.question_number}")




            
    
    
    

