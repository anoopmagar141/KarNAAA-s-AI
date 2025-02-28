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
    
    # Predefined responses with improved flexible matching
    responses = {
        "who are you": "Hey there! I'm KarNAAA, your AI assistant!",
        "who made you": "I was created by anoopmagar141!",
        "who created you": "I was created by anoopmagar141!",
        "who built you": "I was created by anoopmagar141!",
        "who designed you": "I was created by anoopmagar141!",
        "what can you do": "I can assist with basic arithmetic calculations and answer simple predefined questions!",
        "tell me a joke": "Why don’t some couples go to the gym? Because some relationships don’t work out!",
        "what is the meaning of life": "The meaning of life is a mix of joy, purpose, and the pursuit of knowledge!"
    }
    