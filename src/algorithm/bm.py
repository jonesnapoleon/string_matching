def get_prefix(pattern, is_case_sensitive):
    if not is_case_sensitive:
        pattern = pattern.lower()
    length = len(pattern)
    prefix = {}

    for i in range(len(pattern)):
        char = str(pattern[i])
        prefix[char] = (length - i - 1) if i != (length - 1) else length
    prefix['*'] = length

    return prefix


def boyer_moore(data):
    pattern = data['keywords']
    text = data['text']
    is_case_sensitive = data['case-sensitive']
    
    response = []
    border = get_prefix(pattern, is_case_sensitive)
    length = len(pattern) - 1
    last = length
    i = 0
    print(border)
    if not is_case_sensitive:
        while last < len(text):
            while i < length and text[last].lower() == pattern[length - i].lower():
                last -= 1
                i += 1
            if i == length and text[last].lower() == pattern[length - i].lower():
                response.append(last)
                last += length
            i = 0

            last += border[text[last].lower()] if text[last].lower() in border else border['*']
        
    else:
        while last < len(text):
            while i < length and text[last] == pattern[length - i]:
                last -= 1
                i += 1
            if i == length and text[last] == pattern[length - i]:
                response.append(last)
                last += length
            i = 0

            last += border[text[last]] if text[last] in border else border['*']

    return render_result(response, text, pattern)


def render_result(response, text, pattern):
    length = len(pattern)
    keys = len(response)
    string = ""

    if len(response) > 0:
        j = response.pop(0)
        i = 0
        while i < len(text):
            if i == j:
                string += "<span class='highlight'>" + text[i : i + length] + "</span>"
                i += length - 1
                if len(response) > 0:
                    j = response.pop(0)
            else:
                string += text[i]
            i += 1

    else:
        string = text
    
    response_data = {
        "inner_HTML": string.strip(),
        "raw_output": [pattern for i in range(keys)],
    }
    
    return response_data