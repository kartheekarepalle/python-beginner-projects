questions = {
    "What is the capital of France? ": "paris",
    "What is 5 + 7? ": "12",
    "Who developed Python? ": "guido van rossum",
}

score = 0

for q, ans in questions.items():
    user_ans = input(q).strip().lower()
    if user_ans == ans:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The answer is {ans.capitalize()}")

print(f"\nYour final score: {score}/{len(questions)}")
