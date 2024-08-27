questions = [
    "What is the capital of France?",
    "Who wrote 'Harry Potter' series?",
    "Which planet is known as the Red Planet?",
    "Who painted the Mona Lisa?"
]

options = [
    ["A. Paris", "B. London", "C. Berlin", "D. Rome"],
    ["A. J.K. Rowling", "B. Stephen King", "C. George R.R. Martin", "D. J.R.R. Tolkien"],
    ["A. Jupiter", "B. Mars", "C. Saturn", "D. Venus"],
    ["A. Leonardo da Vinci", "B. Michelangelo", "C. Pablo Picasso", "D. Vincent van Gogh"]
]

answers = ["A", "A", "B", "A"]

score = 0

for i in range(len(questions)):
    print(f"\nQ{i+1}. {questions[i]}")
    for option in options[i]:
        print(option)
    
    user_answer = input("Enter your answer (A, B, C, or D): ").upper()
    
    if user_answer == answers[i]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {answers[i]}")

print(f"\nYou scored {score} out of {len(questions)}")
