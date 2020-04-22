from flask import Flask, render_template, url_for, request
from src.algorithm.kmp import knuth_morris_pratt, tubes_knuth_morris_pratt
from src.algorithm.bm import boyer_moore, tubes_boyer_moore
from src.algorithm.regex import regular_expression
from src.algorithm.web import web_scrape
from src.utils import preprocess, callbackdata, commondata, commonwebdata, callbackwebdata

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        previous = commondata()
        return render_template('index.html', previous=previous, show=False)
    
    else:
        data = request.form
        data = data.to_dict(flat=False)
        previous = callbackdata(data)
        data = preprocess(data)
        if data['tubes-mode']:
            if data['algorithm'] == 'regex':
                result = tubes_knuth_morris_pratt(data)
            elif data['algorithm'] == 'kmp':
                result = tubes_knuth_morris_pratt(data)
            else:
                result = tubes_boyer_moore(data)
        else:
            if data['algorithm'] == 'regex':
                result = regular_expression(data)
            elif data['algorithm'] == 'kmp':
                result = knuth_morris_pratt(data)
            else:
                result = boyer_moore(data)

        return render_template('index.html', result=result, previous=previous, show=True)


@app.route('/web', methods=['GET', 'POST'])
def web():
    if request.method == 'GET':
        previous = commonwebdata()
        return render_template('web.html', previous=previous, show=False)

    else:
        data = request.form
        data = data.to_dict(flat=False)
        previous = callbackwebdata(data)
        data = previous

        result = web_scrape(data)
        return render_template('web.html', result=result, previous=previous, show=True)

if __name__ == "__main__":
    app.run(debug=False)