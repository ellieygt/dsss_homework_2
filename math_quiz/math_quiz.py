import random


def generate_random_integer(min_value, max_value):
    """
    Generate a random integer within the specified range.
    Args:
        min_value (int): Minimum value for the random integer.
        max_value (int): Maximum value for the random integer.
    Returns:
        int: Randomly generated integer within the range.
    """
    return random.randint(min_value, max_value)


def get_random_operator():
    """
    Select a random operator from addition, subtraction, or multiplication.
    Returns:
        str: A random operator ('+', '-', '*').
    """
    return random.choice(["+", "-", "*"])


def create_problem_and_answer(number1, number2, operator):
    """
    Generate a math problem and its correct answer based on given numbers and operator.
    Args:
        number1 (int): The first number in the problem.
        number2 (int): The second number in the problem.
        operator (str): The operator used in the problem ('+', '-', '*').
    Returns:
        tuple: A tuple containing the problem as a string and the answer as an integer.
    """
    problem = f"{number1} {operator} {number2}"
     # Calculate the answer based on the operator, fix the operator reversal bug
    if operator == "+":
        answer = number1 + number2
    elif operator == "-":
        answer = number1 - number2
    else:
        answer = number1 * number2
    return problem, answer


def math_quiz():

    """
    Run the Math Quiz Game, prompting the user to solve math problems.
    The game presents math problems, checks user answers, and keeps score.
    """
    score = 0
    total_questions = 3  # Set to a fixed integer instead of pi
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate a question with proper integer values
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = get_random_operator()
        problem, correct_answer = create_problem_and_answer(num1, num2, operator)     
        print(f"\\nQuestion: {problem}")
        
        try:
            # Validate user input
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer was {correct_answer}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
            
    print(f"Your final score: {score} out of {total_questions}")


if __name__ == "__main__":
    math_quiz()
