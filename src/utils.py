def preprocess(data):
    temp = {}
    temp['algorithm'] = data['algorithm'][0]
    temp['keywords'] = data['keywords'][0]
    temp['text'] = data['input-text'][len(data['input-text']) - 1]

    return temp


def callbackdata(data):
    temp = {}
    temp['algorithm'] = data['algorithm'][0]
    temp['keywords'] = data['keywords'][0]
    temp['input-method'] = data['input-method'][0]
    temp['text'] = data['input-text'][len(data['input-text']) - 1]

    return temp


def commondata():
    temp = {}
    temp['algorithm'] = 'regex'
    temp['keywords'] = ''
    temp['input-method'] = 'text'    
    temp['text'] = ''

    return temp

