from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']

    my_q = Question(question_text, question_answer)

    question_bank.append(my_q)

quiz = QuizBrain(question_bank)

# create a while loop --> to loop thru the answer of the specific question 

# if correct answer -- > +1 point
# if incorrect answer -- +0 point
while quiz.still_have_questions():# if quiz still has question remaining:
    quiz.next_question()

# display the last result
quiz.final_display()