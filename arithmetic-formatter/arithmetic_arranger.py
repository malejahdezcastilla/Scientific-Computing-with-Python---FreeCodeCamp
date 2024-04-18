import re 

def arithmetic_arranger (problems, display_results= False):
    problems_arranged_vertically = []
    results = []

    if len(problems) > 5 :
        return "Error: Too many problems."

    for problem in problems:
        letters_in_problem = re.findall ('[a-zA-Z]', problem)
        
        if len (letters_in_problem) >= 1:
            return "Error: Numbers must only contain digits."

    for problem in problems:
        try :
            problems_arranged_vertically.append (vertical_arrangement_one_problem (problem))
        except BaseException as e :
                return  str(e)

     
    if display_results == True :
        size_range = 4
    else :
        size_range = 3 

    for line in range (size_range):
        current_line = []

        for element in range (len (problems)):
            current_line.append (problems_arranged_vertically [element] [line])
        
        join_line = "    ".join (current_line)
        results.append (join_line)

    
    arranged_problems = "\n".join (results)
    
    return arranged_problems


def vertical_arrangement_one_problem (problem):
    numbers_and_operator= problem.split (' ')
    

    if '+' in numbers_and_operator :
        result= int(numbers_and_operator [0]) + int(numbers_and_operator [2])
    elif '-' in numbers_and_operator :
        result= int(numbers_and_operator [0]) - int(numbers_and_operator [2])
    else :
        raise BaseException("Error: Operator must be '+' or '-'.")

    first_operand_length= len(numbers_and_operator [0])
    second_operand_length= len (numbers_and_operator [2])

    if first_operand_length > 4 or second_operand_length > 4 :
        raise BaseException ("Error: Numbers cannot be more than four digits.")

    if first_operand_length > second_operand_length :
        number_of_dashes= first_operand_length + 2
    else :
        number_of_dashes= second_operand_length + 2
    
    dashes= '-'* number_of_dashes


    problem_arranged_vertically = [
        numbers_and_operator [0].rjust (number_of_dashes),
        numbers_and_operator [1] + ' ' + numbers_and_operator [2].rjust (number_of_dashes - 2),
        dashes,
        str(result).rjust(number_of_dashes)    
    ]


    return problem_arranged_vertically
