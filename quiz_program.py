
quiz = {
    "question 1": {
        "question": "What the capital of France?",
        "answer": "Paris"
    },
    "question 2": {
        "question": "What the capital of Germany?",
        "answer": "Berlin"
    },
    "question 3": {
        "question": "What the capital of Italy?",
        "answer": "Rome"
    },
    "question 4": {
        "question": "What the capital of Spain?",
        "answer": "Madrid"
    },
    "question 5": {
        "question": "What the capital of Portugal?",
        "answer": "Lisbon"
    },
    "question 6": {
        "question": "What the capital of Switzerland?",
        "answer": "Bern"
    },
    "question 7": {
        "question": "What the capital of Austria?",
        "answer": "Vienna"
    }

}


score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer ?")

    if answer.lower() == value['answer'].lower():
        print("Correct")
        score = score+1
        print("score is :"+str(score))
        print("")

    else:
        print("Wrong!")
        print("the answer is :"+value['answer'])
        print("score is :"+str(score))
        print("")

print("you got"+str(score)+"out of 7 question correctly")
print("your percentage is  "+str(int(score/7 * 100)) + "%")
