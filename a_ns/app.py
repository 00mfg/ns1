from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from util import table1_data, table2_data

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    # data1 = table1_data()
    # data2 = table2_data()
    u1 = [['10.1.57.3', 6, ['10.1.11.224, 10.1.1.232, 10.2.3.233']], ['10.21.57.3', 3, ['100.1.11.224, 110.1.1.232, 17.2.3.233']], ['10.1.17.23', 1, ['10.12.11.124, 10.1.1.232, 192.2.3.233']]]
    u2 = [['10.1.57.3', '10.1.57.3', 6, '10.1.57.3', '10.1.11.224, 10.1.1.232, 10.2.3.233'], ['10.21.57.3', '10.1.57.3', 3, '100.1.11.224, 110.1.1.232, 17.2.3.233'], ['10.1.17.23', '10.1.57.3', 1, '10.12.11.124, 10.1.1.232, 192.2.3.233']]
    return render_template('index.html', u1=u1, u2=u2)


if __name__ == '__main__':
    app.run(host='172.17.0.2')