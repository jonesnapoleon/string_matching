def preprocess(data):
    print(data)
    temp = {}
    temp['algorithm'] = data['algorithm'][0]
    temp['keywords'] = data['keywords'][0]
    temp['text'] = data['input-text'][len(data['input-text']) - 1]
    try:
        if data['case-sensitive']:
            temp['case-sensitive'] = True
    except:
        temp['case-sensitive'] = False

    return temp


def callbackdata(data):
    print(data)
    temp = {}
    temp['algorithm'] = data['algorithm'][0]
    temp['keywords'] = data['keywords'][0]
    temp['input-method'] = data['input-method'][0]
    temp['text'] = data['input-text'][len(data['input-text']) - 1]
    try:
        if data['case-sensitive']:
            temp['case-sensitive'] = 'true'
    except:
        temp['case-sensitive'] = 'false'

    return temp


def commondata():
    temp = {}
    temp['algorithm'] = 'regex'
    temp['keywords'] = ''
    temp['input-method'] = 'text'
    temp['text'] = ''
    temp['case-sensitive'] = 'true'

    return temp


def commonwebdata():
    temp = {}
    temp['keywords'] = ''
    temp['url'] = ''

    return temp


def callbackwebdata(data):
    temp = {}
    temp['keywords'] = data['keywords'][0]
    temp['url'] = data['input-web'][0]

    return temp
