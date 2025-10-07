from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Profile page
@app.route('/profile')
def profile():
    return render_template('profile.html')

# Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Circle area calculator
@app.route('/circle', methods=['GET', 'POST'])
def circle():
    area = None
    radius = None
    if request.method == 'POST':
        try:
            radius = float(request.form['radius'])
            area = 3.14159 * radius * radius
        except ValueError:
            area = "Invalid input"
    return render_template('circle.html', area=area, radius=radius)

# Triangle area calculator
@app.route('/triangle', methods=['GET', 'POST'])
def triangle():
    area = None
    base = None
    height = None
    if request.method == 'POST':
        try:
            base = float(request.form['base'])
            height = float(request.form['height'])
            area = 0.5 * base * height
        except ValueError:
            area = "Invalid input"
    return render_template('triangle.html', area=area, base=base, height=height)

if __name__ == '__main__':
    app.run(debug=True)
