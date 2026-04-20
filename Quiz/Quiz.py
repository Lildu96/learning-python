
questions = [
    {
        "prompt": "Which of the following is the longest river in the world?",
        "options": ["A. Nile", "B. Amazon", "C. Yangtze", "D. Mississippi"],
        "answer": "B. Amazon",
        "fact": "The Amazon River is the longest river in the world, stretching approximately 4,345 miles (7,062 kilometers) in length.\nIt flows through multiple countries including Brazil, Peru and Colombia.\nIt is home to pink river dolphins."
     },
     {
        "prompt": "Who painted the Mona Lisa?",
        "options": ["A. Vincent Van Gogh", "B. Pablo Picasso", "C. Leonardo Da Vinci", "D. Claude Monet"],
        "answer": "C. Leonardo Da Vinci",
        "fact": "The Mona Lisa was painted between 1503 and 1506.\nShe is displayed in La Louvre Museum behind bulletproof glass and was famously stolen in 1911."
     },
      {
        "prompt": "What is the capital of Japan?",
        "options": ["A. Seoul", "B. Beijing", "C. Tokyo", "D. Kyoto"],
        "answer": "C. Tokyo",
        "fact": "Tokyo is the largest metropolitan area in the world with a population of over 35 million (London being around 9 million).\nIt was originally named Edo before becoming the capital in 1868"
     },
]

def run_quiz(questions):
    print("------")
    print(f"Welcome to my Quiz! There are {len(questions)} questions. GL HF!")
    print("------")
    score = 0

    for i, question in enumerate(questions):
        print(question["prompt"])
        for option in question["options"]:
            print(option)
            
        print("------")

        answer = input("Enter your answer:\n").strip().title()
        print("------")
        if (
            answer in question["answer"].split(". ")
            or answer == question["answer"]
        ):
            print("Correct, good job!")
            score += 1
        else:
            print("Nope, silly goose. The correct answer is", question["answer"], "\n")

        print("------")
        print(f"Fun facts:\n{question['fact']}")
        print("------")

        if i == len(questions) - 1:
            input("End of questions. Press Enter to see your score...")
        else:
            input(f"Press Enter to go to question {i + 2} out of {len(questions)} ...")
        print("------")
        
    percentage = (score / len(questions)) * 100
        
    if percentage < 50:
        print(f"DUMBO! You scored {score} out of {len(questions)}.")
    elif percentage >= 50:
        print(f"Good Job you completed the quiz with a score of {score} out of {len(questions)}.")
    elif percentage == 100:
        print(f"Congratulations you completed the quiz with full marks! {score} out of {len(questions)}.")

    print("------")

run_quiz(questions)