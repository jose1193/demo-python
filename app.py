from flask import Flask, render_template
import datetime

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    text = 'Hola Mundo'
    result = 10 + 10
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', result=result, current_time=current_time,text=text)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


