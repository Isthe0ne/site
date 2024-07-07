from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('formulaire.html')

@app.route('/submit', methods=['POST'])
def submit():
	return redirect(url_for('phished'))

@app.route('/phished')
def phished():
	return render_template('phished.html')

if __name__ == '__main__':
    app.run(debug=True)
