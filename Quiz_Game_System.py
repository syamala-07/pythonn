def quiz():
    questions = {
        "Python is a ___ language?": "high",
        "Which symbol is used for comments?": "#",
        "Which data type stores True/False?": "bool",
        "Which keyword is used to create function?": "def"
    }
    score = 0
    for question, answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.lower() == answer:
            print("Correct")
            score += 1
        else:
            print("Wrong → correct answer is", answer)
    print("\nFinal Score:", score, "/", len(questions))
quiz()