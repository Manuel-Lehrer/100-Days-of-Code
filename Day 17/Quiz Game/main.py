from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for questions in question_data:
    new_question = Question(questions["question"], questions["correct_answer"])
    question_bank.append(new_question)


brain = QuizBrain(question_bank)


while brain.still_has_questions():
    brain.next_question()

print("You've completed the final quiz")
print(f"Your final score was {brain.score}/{brain.question_number}")
