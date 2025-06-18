from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for session management

# Dummy credentials
valid_username = 'admin'
valid_password = '123'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == valid_username and password == valid_password:
            session['user'] = username
            return redirect(url_for('games'))
        else:
            error = 'Invalid username or password'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/games')
def games():
    if 'user' in session:
        return render_template('games.html', username=session['user'])
    else:
        return redirect(url_for('login'))

@app.route('/news')
def news():
    category = request.args.get('category', 'latest')
    print("Category received:", category)
    return render_template("news.html", category=category)

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@app.route('/email')
def email():
    return render_template('email.html')

@app.route('/phone')
def phone():
    return render_template('phone.html')

@app.route('/latest')
def latest():
    return render_template('latest.html')

@app.route('/trending')
def trending():
    return render_template('trending.html')

@app.route('/archives')
def archives():
    return render_template('archives.html')


if __name__ == '__main__':
    app.run(debug=True)