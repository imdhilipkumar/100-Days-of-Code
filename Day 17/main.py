from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# create the empty list
question_bank = []
# for loop over the question Data
for question in question_data:
    # to get the init text and answer value
    question_text = question["text"]
    question_answer = question["answer"]
    # object creation with two attributes  of class value
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

    # Object Creation
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
