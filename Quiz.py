
questions = [
    {
        "prompt": "Which of the following is the longest river in the world?",
        "options": ["A. Nile", "B. Amazon", "C. Yangtze", "D. Mississippi"],
        "answer": "B"
     },
     {
        "prompt": "Who painted the Mona Lisa?",
        "options": ["A. Vincent Van Gogh", "B. Pablo Picasso", "C. Leonardo do Vinci", "D. Claude Monet"],
        "answer": "C"
     },
      {
        "prompt": "What is the capital of Japan?",
        "options": ["A. Seoul", "B. Beijing", "C. Tokyo", "D. Kyoto"],
        "answer": "C"
     },
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C or D): ").upper()
        if answer == question["answer"]:
            print("Correct, good job!\n")
            score += 1
        else:
            print("Nope, silly goose. The correct answer is", question["answer"], "\n")

    print(f"Quiz complete! You scored {score} out of {len(questions)}.")

run_quiz(questions)