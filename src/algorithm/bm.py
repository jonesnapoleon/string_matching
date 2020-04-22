import nltk
from nltk.tokenize import sent_tokenize
from src.algorithm.moment import get_time, get_number
import re
nltk.download('punkt')


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


def render_result(response, text, pattern):
    length = len(pattern)
    keys = len(response)
    string = ""

    if len(response) > 0:
        j = response.pop(0)
        i = 0
        while i < len(text):
            if i == j:
                string += "<mark>" + text[i : i + length] + "</mark>"
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


def boyer_moore(data):
    pattern = data['keywords']
    text = data['text']
    is_case_sensitive = data['case-sensitive']
    
    response = []
    border = get_prefix(pattern, is_case_sensitive)
    length = len(pattern) - 1
    last = length
    i = 0

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



#TUBES STARTS HERE
def preprocess_sentences(sentence):
    sentences = sentence.strip()
    sentences = sentences.replace("\r\n", ". ")
    sentences = sent_tokenize(sentences)
    return sentences


def tubes_boyer_moore(data):
    pattern = data['keywords']
    text = data['text']
    sentences = extract_text_to_sentence(text)
    response = []
    statements = []
        
    border = get_prefix(pattern, False)
    length = len(pattern) - 1

    for j in range(len(sentences)):
        sentence = sentences[j]
        last = length
        i = 0
        while last < len(sentence):
            while i < length and sentence[last].lower() == pattern[length - i].lower():
                last -= 1
                i += 1
            if i == length and sentence[last].lower() == pattern[length - i].lower():
                response.append({"sentence-order": j, "relative-pos": last})
                statements.append(parse_information(sentence))
                last += length
            i = 0
            last += border[sentence[last].lower()] if sentence[last].lower() in border else border['*']
    return generator(response, statements, sentences)


def extract_text_to_sentence(text):
    text = sent_tokenize(text)
    print(text)
    array = []
    for sentence in text:
        statements = preprocess_sentences(sentence)
        for statement in statements:
            array.append(statement)
    return array


def set_final(numbers, moments):
    must_delete_numbers = []
    must_delete_moments = []

    if len(numbers) > 0 and len(moments) > 0:
        for i in range(len(numbers)):
            num_init = numbers[i]['span'][0]
            num_last = numbers[i]['span'][1]
            for j in range(len(moments)):
                mom_init = moments[j]['span'][0]
                mom_last = moments[j]['span'][1]
                if num_init <= mom_init and num_last >= mom_last:
                    if moments[j] not in must_delete_moments:
                        must_delete_moments.append(moments[j])
                    break
                elif num_init >= mom_init and num_last <= mom_last:
                    if numbers[i] not in must_delete_numbers:
                        must_delete_numbers.append(numbers[i])

        final_numbers = [num for num in numbers if num not in must_delete_numbers]
        final_moments = [mom for mom in moments if mom not in must_delete_moments]
    else:
        final_numbers = [num for num in numbers]
        final_moments = [mom for mom in moments]
    return {'final_numbers': final_numbers, 'final_moments': final_moments}


def set_html_number(sentence, number):
    string = ''
    if len(number) > 0:
        to_be_checked = number.pop(0)['group']
        index = 0
        while index < len(sentence):
            while sentence[index : index + len(to_be_checked)] != to_be_checked:
                string += sentence[index]
                index += 1
            string += "<mark class='numbers'>" + to_be_checked + "</mark>"
            index += len(to_be_checked)
            if len(number) > 0:
                to_be_checked = number.pop(0)['group']
            else:
                string += sentence[index : index + len(sentence)]
                break
    else:
        string = sentence

    return string


def set_html_moment(sentence, moment):
    string = ''
    if len(moment) > 0:
        to_be_checked = moment.pop(0)['group']
        index = 0
        while index < len(sentence):
            while sentence[index : index + len(to_be_checked)] != to_be_checked:
                string += sentence[index]
                index += 1
            string += "<mark class='moments'>" + to_be_checked + "</mark>"
            index += len(to_be_checked)
            if len(moment) > 0:
                to_be_checked = moment.pop(0)['group']
            else:
                string += sentence[index : index + len(sentence)]
                break
    else:
        string = sentence

    return string


def set_html(sentence, number, moment):
    string = set_html_number(sentence, number)
    final = set_html_moment(string, moment)    
    return str(final)


def parse_information(one_sentence):
    numbers_pattern = get_number()
    moment_pattern = get_time()
    numbers = []
    moments = []
    
    for matched_number in re.finditer(numbers_pattern, one_sentence):
        numbers.append({'span': matched_number.span(), 'group': matched_number.group(0).strip()})

    for matched_moment in re.finditer(moment_pattern, one_sentence):
        moments.append({'span': matched_moment.span(), 'group': matched_moment.group(0).strip()})

    final = set_final(numbers, moments)
    copy_number = [f for f in final['final_numbers']]
    copy_moment = [f for f in final['final_moments']]

    html = set_html(one_sentence, final['final_numbers'], final['final_moments'])
    return {
        "innerHTML": html,
        "number": copy_number,
        "moment": copy_moment,
    }


def generator(response, statements, sentences):
    temp = []
    final_inner_HTML = ""
    plain_output = []
    for res in response:
        temp.append(res['sentence-order'])
    
    if len(temp) > 0:
        count = temp.pop(0)
        for i in range(len(sentences)):
            if count == i:
                final_inner_HTML += statements[0]['innerHTML'] + '\n'
                plain_output.append(manage(statements[0]))
                if len(temp) > 0:
                    count = temp.pop(0)
                    statements.pop(0)
            else:
                final_inner_HTML += sentences[i] + '\n'
    else:
        final_inner_HTML = sentences
    return {
        "raw_output": plain_output,
        "inner_HTML": final_inner_HTML
    }


def manage(statement):
    string = "<mark class='numbers'>"

    if len(statement['number']) > 0:
        for num in statement['number']:
            string += num['group']
    else:
        string += "No detected value"
    string += "</mark> - <mark class='moments'>"

    if len(statement['moment']) > 0:
        for mom in statement['moment']:
            string += mom['group'] + " "
    else:
        string += "No detected date"
    string += "</mark>"
    return string