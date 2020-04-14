import re

def regular_expression(data):
    pattern = data['keywords']
    text = data['text']

    try:
        solution = re.findall(pattern, text)        
        saved_solution = [sol for sol in solution]
        string = ""

        if len(solution) > 0:
            to_be_checked = solution.pop(0)
            index = 0
            while index < len(text):
                while text[index : index + len(to_be_checked)] != to_be_checked:
                    string += text[index]
                    index += 1
                string += "<span class='highlight'>" + to_be_checked + "</span>"
                index += len(to_be_checked)
                if len(solution) > 0:                    
                    to_be_checked = solution.pop(0)
                else:
                    break
        else:
            string = text
        
        response = {
            "inner_HTML": string.strip(),
            "raw_output": saved_solution,
        }
    
    except:
        response = {
            "inner_HTML": "<h4 class='highlight'>Keywords error</h4>",
            "raw_output": [],
        }

    return response