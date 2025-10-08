from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html', title="Home")

# Profile route
@app.route('/profile')
def profile():
    return render_template('profile.html', title="Profile")

# Contact route
@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")

# Circle area calculator
@app.route('/circle', methods=['GET', 'POST'])
def circle():
    area = None
    if request.method == 'POST':
        try:
            radius = float(request.form['radius'])
            area = 3.1416 * radius * radius
        except ValueError:
            area = "Invalid input"
    return render_template('circle.html', title="Circle", area=area)

# Triangle area calculator
@app.route('/triangle', methods=['GET', 'POST'])
def triangle():
    area = None
    if request.method == 'POST':
        try:
            base = float(request.form['base'])
            height = float(request.form['height'])
            area = 0.5 * base * height
        except ValueError:
            area = "Invalid input"
    return render_template('triangle.html', title="Triangle", area=area)

# Uppercase converter
@app.route('/touppercase', methods=['GET', 'POST'])
def to_uppercase():
    result = None
    if request.method == 'POST':
        text = request.form['text']
        result = text.upper()
    return render_template('touppercase.html', title="Uppercase", result=result)


if __name__ == '__main__':
    app.run(debug=True)
