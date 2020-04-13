import re

def boyer_moore(data):
    pattern = data['keywords']
    text = data['text']

    solution = re.findall(pattern, text)
    
    saved_solution = [sol for sol in solution]
    string = ""

    if len(solution) > 0:
        to_be_checked = solution.pop()
        for index in range(len(text) - 1, -1, -1):
            string = text[index] + string
            if string[0: len(to_be_checked)] == to_be_checked:
                string = string.replace(to_be_checked, "<span class='highlight>" + to_be_checked + "</span>", 1)
                if len(solution) > 0:
                    to_be_checked = solution.pop()
                else:
                    break
    else:
        string = text

    response = {
        "inner-HTML": string,
        "raw_output": saved_solution,
    }

    return response
