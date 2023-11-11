import random


def get_random_int(min, max):
    """
    Create a random integer from the interval [min, max].

    Args:
        min (int): The minimum integer.
        max (int): The maximum integer.

    Returns:
        int: A random int.

    """
    return random.randint(min, max)


def get_random_operator():
    """
    Get a randomized operator from the choice of {+, -, *}

    Returns: 
        str: An operator.
    
    """
    return random.choice(['+', '-', '*'])


def calculate(n1, n2, o):
    """
    Calculates a term.

    Args:
        n1 (int): The first number.
        n2 (int): The second number.
        o (str): An operator.
    
    Returns:
        str: The term as string.
        int: The result of the calculation.
    """

    p = f"{n1} {o} {n2}"
    if o == '+':
        a = n1 + n2
    elif o == '-':
        a = n1 - n2
    else: 
        a = n1 * n2
    return p, a

def math_quiz():
    s = 0
    t_q = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = get_random_int(1, 10); 
        n2 = get_random_int(1, 5); 
        o = get_random_operator()

        PROBLEM, ANSWER = calculate(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")

        try:
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)
        except:
            print("Input an integer!")
            
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
