import datetime
import re
import operator

# Define supported operators
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def calculate(expression):
    try:
        tokens = re.findall(r'\d+|[-+*/]', expression)
        if len(tokens) != 3:
            return "Invalid calculation! Please enter a valid math expression like '5 + 3'."
        num1, op, num2 = int(tokens[0]), tokens[1], int(tokens[2])
        if op in ops:
            return f"Result: {ops[op](num1, num2)}"
        else:
            return "Unsupported operation! Try +, -, *, or /."
    except Exception:
        return "Error processing the calculation! Ensure you enter a valid math expression."

def get_greeting():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        return "Good morning! Have an amazing day!"
    elif current_hour < 18:
        return "Good afternoon! Hope your day is going great!"
    else:
        return "Good evening! Hope you're having a wonderful time!"

def simple_ai(user_input, first_interaction=False):
    user_input = user_input.lower().strip()
    
    if not user_input:
        return "Please enter a valid input!"
  