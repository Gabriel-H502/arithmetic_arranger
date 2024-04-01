def arithmetic_arranger(problems, show_answers=False) -> str:
    """Arranges the problems vertically on a horizontal line."""
    # Checking the amount of problems
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    row1 = ""
    row2 = ""
    row3 = ""
    row4 = ""
    
    # Looping every problem
    for i, problem in enumerate(problems):
        problem = str(problem)
        
        # Checking operators
        if '+' in problem:
            problem = problem.split('+')
            operator = "+"
        elif '-' in problem:
            problem = problem.split('-')
            operator = "-"
        else:
            return "Error: Operator must be '+' or '-'."
        
        operand1 = problem[0].strip()
        operand2 = problem[1].strip()
        
        # Checking if numbers have more than four digits
        if len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        # Checking if numbers are integer-only
        if not operand1.isnumeric() or not operand2.isnumeric():
            return 'Error: Numbers must only contain digits.'    
            
        # Setting the arrange length
        largest_number = operand1 if int(operand1) > int(operand2) else operand2
        arrange_length = len(str(largest_number)) + 2
        result = str(eval(operand1 + operator + operand2))
        
        # Add to string for display
        row1 += f"{operand1:>{arrange_length}}"
        row2 += f"{operator}{operand2:>{arrange_length - 1}}"
        row3 += f"-" * arrange_length
        
        # If not last problem, add final spacing
        if i != len(problems) - 1:
            row1 += " " * 4
            row2 += " " * 4
            row3 += " " * 4
        
        # Showing the answer
        if show_answers is True:
            row4 += f"{result:>{arrange_length}}"
            
            # If not last problem, add final spacing
            if i != len(problems) - 1:
                row4 += " " * 4
    
    # Returning the arranged problems    
    arranged_problems += row1 + "\n" + row2 + "\n" + row3
    
    # This is for don't adding an empty extra line if show_answers is false
    if show_answers:
        arranged_problems += "\n" + row4
            
    return arranged_problems
