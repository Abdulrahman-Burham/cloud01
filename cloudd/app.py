from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy user data for authentication
users = {
    "user@example.com": "password123"
}

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    if email in users and users[email] == password:
        flash('Login successful!', 'success')
        return redirect(url_for('dashboard'))
    else:
        flash('Invalid email or password.', 'danger')
        return redirect(url_for('login_page'))

@app.route('/dashboard')
def dashboard():
    return "Welcome to your dashboard!"

@app.route('/forgot-password')
def forgot_password_page():
    return render_template('forgot_password.html')

@app.route('/forgot-password', methods=['POST'])
def forgot_password():
    email = request.form.get('email')
    if email in users:
        flash('Password reset link sent to your email.', 'success')
    else:
        flash('Email not found.', 'danger')
    return redirect(url_for('forgot_password_page'))

if __name__ == '__main__':
    app.run(debug=True)