import random

class fruitQuiz:
    def __init__(self):
        self.fruits={'apple':'red','orange':'orange','watermelon':'green','strawberry':'red'}

    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            print("what is the color of {}".format(fruit))

            user_answer = input()

            if user_answer.lower() == color:
                print("correct answer")
            else:
                print("incorrect answer")

            option = int(input("enter 0, if you want to play again, otherwise enter 1 : "))
            if option:
                print("thanks for playing")
                break

fq = fruitQuiz()
fq.quiz()