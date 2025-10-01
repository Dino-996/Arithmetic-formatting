def arithmetic_arranger(problems, show_answers=False):
    
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_line = []
    second_line = []
    dashes_line = []
    answers_line = []

    for problem in problems:
        parts = problem.split()
        # Ogni problema deve avere il formato (operando, operatore, operando)
        if len(parts) != 3: 
            return "Error: Invalid problem format."
        
        num1, operator, num2 = parts    

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calcolo larghezza (max + 2, per operatore e spazio)
        width = max(len(num1), len(num2)) + 2

        # Aggiungo alle liste
        first_line.append(num1.rjust(width))
        second_line.append(operator + num2.rjust(width - 1))
        dashes_line.append("-" * width)

        if show_answers:
            if operator == "+":
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            answers_line.append(result.rjust(width))

    # Unisco le varie parti con 4 spazi
    arranged_problems = "    ".join(first_line) + "\n" + \
                        "    ".join(second_line) + "\n" + \
                        "    ".join(dashes_line)

    if show_answers:
        arranged_problems += "\n" + "    ".join(answers_line)

    return arranged_problems

# Test
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print()
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
