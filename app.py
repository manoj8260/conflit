import os
from functools import wraps

from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Never commit a hard-coded secret key to version control.
# Prefer an env var and fall back to a random key for local development.
app.secret_key = os.environ.get("SECRET_KEY", os.urandom(24))

# -----------------------------------------------------------------------------
# Dummy in-memory user "database". In a real app, replace with persistent store.
# -----------------------------------------------------------------------------
USER_RECORD = {
    "username": "admin",
    "password_hash": generate_password_hash("123"),  # store only the hash!
}

# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------

def login_required(view_func):
    """Decorator that redirects anonymous users to the login page."""
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        if "user" not in session:
            flash("Please log in to access this page.", "warning")
            return redirect(url_for("login"))
        return view_func(*args, **kwargs)

    return wrapper


# -----------------------------------------------------------------------------
# Routes
# -----------------------------------------------------------------------------

@app.route("/")
def home():
    # If already logged in, go straight to the welcome page.
    if "user" in session:
        return redirect(url_for("welcome"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if (
            username == USER_RECORD["username"]
            and check_password_hash(USER_RECORD["password_hash"], password)
        ):
            session["user"] = username
            flash("Logged in successfully!", "success")
            return redirect(url_for("welcome"))

        flash("Invalid credentials. Please try again.", "danger")
        return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/welcome")
@login_required
def welcome():
    return render_template("welcome.html", user=session["user"])


@app.route("/logout")
@login_required
def logout():
    session.pop("user", None)
    flash("Logged out.", "info")
    return redirect(url_for("login"))


# -----------------------------------------------------------------------------
# Entry-point
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    # Never enable debug mode in production!
    debug_mode = bool(os.environ.get("FLASK_DEBUG", "1"))
    app.run(debug=debug_mode)