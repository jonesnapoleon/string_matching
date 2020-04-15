def get_prefix(pattern, is_case_sensitive):
    if not is_case_sensitive:
        pattern = pattern.lower()

    prefix = [0 for i in range(len(pattern))]
    j = 0

    for i in range(1, len(pattern)):
        val = prefix[i - 1]
        if prefix[i - 1] == 0:
            j = 0
            val = 0

        if pattern[i] == pattern[j]:
            prefix[i] = val + 1
        else:
            while j < i and pattern[i] != pattern[j]:
                j += 1
            prefix[i] = 0 if j == i else 1
        j += 1
    
    return prefix


def knuth_morris_pratt(data):
    pattern = data['keywords']
    text = data['text']
    is_case_sensitive = data['case-sensitive']

    border = get_prefix(pattern, is_case_sensitive)
    pattern = '0' + pattern
    border.insert(0, 0)
    response = []
    j = 0

    if is_case_sensitive:
        for i in range(len(text)):
            while j != 0 and pattern[j + 1] != text[i]:
                j = border[j]
            if text[i] == pattern[j + 1]:
                i += 1
                j += 1
            if j == len(border) - 1:
                response.append(i- len(pattern) + 1)
                j = 0
    else:
        for i in range(len(text)):
            while j != 0 and pattern[j + 1].lower() != text[i].lower():
                j = border[j]
            if text[i].lower() == pattern[j + 1].lower():
                i += 1
                j += 1
            if j == len(border) - 1:
                response.append(i- len(pattern) + 1)
                j = 0

    return render_result(response, text, pattern[1:])


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