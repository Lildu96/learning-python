
questions = [
    {
        "prompt": "Which of the following is the longest river in the world?",
        "options": ["A. Nile", "B. Amazon", "C. Yangtze", "D. Mississippi"],
        "answer": ["B. Amazon","B","Amazon"],
        "fact": "The Amazon River is the longest river in the world, stretching approximately 4,345 miles (7,062 kilometers) in length.\nIt flows through multiple countries including Brazil, Peru and Colombia.\nIt is home to pink river dolphins."
     },
    #  {
    #     "prompt": "Who painted the Mona Lisa?",
    #     "options": ["A. Vincent Van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"],
    #     "answer": "C",
    #     "fact": "The Mona Lisa was painted between 1503 and 1506.\nShe is displayed in La Louvre Museum behind bulletproof glass and was famously stolen in 1911."
    #  },
    #   {
    #     "prompt": "What is the capital of Japan?",
    #     "options": ["A. Seoul", "B. Beijing", "C. Tokyo", "D. Kyoto"],
    #     "answer": "C",
    #     "fact": "Tokyo is the largest metropolitan area in the world with a population of over 35 million (London being around 9 million).\nIt was originally named Edo before becoming the capital in 1868"
    #  },
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer: ").strip().title()
        if answer in (question["answer"]):
            print(answer)
            print("Correct, good job!\n")
            score += 1
        else:
            print(answer)
            print("Nope, silly goose. The correct answer is", question["answer"][0], "\n")
        print(f"Fun facts:\n{question['fact']}")

    print(f"Quiz complete! You scored {score} out of {len(questions)}.")

run_quiz(questions)