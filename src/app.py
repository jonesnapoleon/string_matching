from flask import Flask, render_template, url_for, request
from algorithm.kmp import knuth_morris_pratt
from algorithm.bm import boyer_moore
from algorithm.regex import regular_expression
from utils import preprocess, callbackdata, commondata

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    

    if request.method == 'GET':
        previous = commondata()
        print('previous', previous)
        return render_template('index.html', previous=previous, show=False)
    
    else:
        data = request.form
        data = data.to_dict(flat=False)
        previous = callbackdata(data)
        data = preprocess(data)

        if data['algorithm'] == 'regex':
            result = regular_expression(data)
        elif data['algorithm'] == 'kmp':
            result = knuth_morris_pratt(data)
        else:
            result = boyer_moore(data)
        
        print('previous', previous)
        return render_template('index.html', result=result, previous=previous, show=True)


if __name__ == "__main__":
    app.run(debug=False)