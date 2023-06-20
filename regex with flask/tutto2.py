from flask import Flask, render_template, request
import re
rt=request

app = Flask(__name__)


@app.route("/",methods=['GET','post'])
def regular():
    if request.method == 'POST':
        regex_value =rt.form['regex_value']
        regex101 =rt.form['regex101']
        matches = re.finditer(regex101,regex_value)
        return render_template('regex.html',matches=matches)
    else:
        return render_template('regex.html')

if __name__ == "__main__":
    app.run(debug=True)