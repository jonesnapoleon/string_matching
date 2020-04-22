import requests
from bs4 import BeautifulSoup
import re


def web_scrape(data):
    url = data['url']
    pattern = data['keywords']
    
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        soup = str(soup)
        text = soup

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
                    string += "<mark>" + to_be_checked + "</mark>"
                    index += len(to_be_checked)
                    if len(solution) > 0:                    
                        to_be_checked = solution.pop(0)
                    else:
                        break
            else:
                string = text
            
            string_html = ""
            for i in range(len(soup)):
                string_html += soup[i]

            response = {
                "inner_HTML": string.strip(),
                "raw_output": saved_solution,
                "genuine_HTML": string_html
            }
        
        except:
            response = {
                "inner_HTML": "<h4 class='highlight'>Keywords error</h4>",
                "raw_output": [],
                "genuine_HTML": "<div></div>"
            }

    except:
        response = {
            "inner_HTML": "<center>Fail to retrieve page</center>",
            "raw_output": [],
            "genuine_HTML": "<div></div>"
        }

    return response
