# import requests
# from bs4 import BeautifulSoup

# def web_scrape(data):
#     url = data['url']
#     keywords = data['keywords']
#     try:
#         res = requests.get(url)
#         soup = BeautifulSoup(res.text, 'html.parser')
#         texts = soup.findAll(text=True)
#         soup = str(soup)
#         one_text = "".join(texts)



#         string = ""
#         for i in range(len(soup)):
#             string += soup[i]

#         result = {}        
#         result['inner_HTML'] = string
#         result['raw_output'] = []

#         return result

#     except:
#         result = {}        
#         result['inner_HTML'] = "<center>Fail to retrieve page</center>"
#         result['raw_output'] = []

#         return result
# import requests
# from bs4 import BeautifulSoup

# def web_scrape(data):
#     url = data['url']
#     keywords = data['keywords']
#     try:
#         res = requests.get(url)
#         soup = BeautifulSoup(res.text, 'html.parser')
#         texts = soup.findAll(text=True)
#         soup = str(soup)
#         one_text = "".join(texts)



#         string = ""
#         for i in range(len(soup)):
#             string += soup[i]

#         result = {}        
#         result['inner_HTML'] = string
#         result['raw_output'] = []

#         return result

#     except:
#         result = {}        
#         result['inner_HTML'] = "<center>Fail to retrieve page</center>"
#         result['raw_output'] = []

#         return result

# data = {
#     'url': 'http://informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/2019-2020/stima19-20.htm',
#     'keywords': 'Tugas'
# }

# temp = web_scrape(data)

# # print(temp)



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
                    string += "<span class='highlight'>" + to_be_checked + "</span>"
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


data = {
    'url': 'http://informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/2019-2020/stima19-20.htm',
    'keywords': 'Tugas'
}

temp = web_scrape(data)

print(temp)



