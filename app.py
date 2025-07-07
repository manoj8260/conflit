from flask import Flask, request, url_for, Response, session, redirect

app = Flask(__name__)
app.secret_key = "superkey"

@app.route("/")
def home():
    return redirect(url_for('login'))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if username == "admin" and password == "123":
            session['user'] = username
            print('Login successfully')
            return redirect(url_for("welcome"))
        return Response("Invalid Credentials!", mimetype="text/plain")
    
    return '''
        <h2>Login Page</h2>
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
            <h1>Welcome, {session['user']}!</h1>
            <a href="{url_for("logout")}">Logout</a>
        '''
    return redirect(url_for('login'))

@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)