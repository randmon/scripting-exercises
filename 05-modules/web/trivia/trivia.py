import json
from urllib.request import urlopen
from html import unescape
import random

LETTERS = "ABCDEFGH"

def get_question():
    with urlopen("https://opentdb.com/api.php?amount=1&category=15") as response:
        question = json.loads(response.read().decode("utf-8"))['results'][0]
        print(unescape(question['question']))
        correct = randomize_answers(question["correct_answer"], question["incorrect_answers"])
        
        # print(LETTERS[correct-1])
        return [LETTERS[correct-1], unescape(question["correct_answer"])]

def randomize_answers(correct, incorrect):
    amount = len(incorrect)+1
    i = random.randint(1, amount)
    incorrect.insert(i-1, correct)
    for x in range(amount):
        print(f"{LETTERS[x]}) {unescape(incorrect[x])}")
    # print(correct)
    return i
    
def get_input():
    return input("Answer: ").strip().upper()

def check_answer(quiz, user):
    if quiz[0] == user:
        print("Correct!")
    else:
        print(f"Wrong! Answer was: ({quiz[0]}) {quiz[1]}")
print()
letter, correct = get_question()
answer = get_input()
check_answer([letter, correct], answer)