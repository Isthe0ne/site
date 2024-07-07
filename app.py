from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/<user_id>')
def index():
    return render_template('formulaire.html', user_id=user_id)

@app.route('/submit', methods=['POST'])
def submit():
    try:
        user_id = request.form.get('user_id')
        response = requests.post(f'https://app-api-ebp4.onrender.com/mail-phished/{user_id}', json={"user_id": user_id})

        
        # Redirigez vers la page 'phished'
        return redirect(url_for('phished'))
    except Exception as e:
        print(f"An error occurred: {e}")
        return "An error occurred", 500

@app.route('/phished')
def phished():
    return render_template('phished.html')

if __name__ == '__main__':
    app.run(debug=True)

