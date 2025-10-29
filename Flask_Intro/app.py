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

# Linked List simulator
@app.route('/linkedlist', methods=['GET', 'POST'])
def linkedlist():
    result = []
    action_message = ""
    
    # Maintain a session-like linked list
    if 'linked_list' not in globals():
        global linked_list
        linked_list = []

    if request.method == 'POST':
        action = request.form.get('action')
        value = request.form.get('value')

        if action == 'add_beginning' and value:
            linked_list.insert(0, value)
            action_message = f"Added '{value}' at the beginning."
        elif action == 'add_end' and value:
            linked_list.append(value)
            action_message = f"Added '{value}' at the end."
        elif action == 'remove_beginning':
            if linked_list:
                removed = linked_list.pop(0)
                action_message = f"Removed '{removed}' from the beginning."
            else:
                action_message = "List is empty!"
        elif action == 'remove_end':
            if linked_list:
                removed = linked_list.pop()
                action_message = f"Removed '{removed}' from the end."
            else:
                action_message = "List is empty!"
        elif action == 'clear_list':
            linked_list.clear()
            action_message = "Cleared the linked list."

    result = " → ".join(linked_list) + " → X" if linked_list else "X (Empty List)"
    return render_template('linkedlist.html', title="Linked List", result=result, message=action_message)

# Infix to Postfix Converter
def infix_to_postfix(expression):
    """Convert infix to postfix using Shunting Yard Algorithm"""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = []

    for token in expression.split():
        if token.isalnum():  # Operand (A, B, C, etc.)
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '('
        else:
            while stack and stack[-1] != '(' and precedence.get(token, 0) <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return ' '.join(output)


@app.route('/infixtopostfix', methods=['GET', 'POST'])
def infixtopostfix():
    postfix = None
    message = ""

    if request.method == 'POST':
        expression = request.form['expression']
        try:
            postfix = infix_to_postfix(expression)
            message = "Successfully converted!"
        except Exception as e:
            postfix = "Error in expression!"
            message = f"Error: {e}"

    return render_template('infixtopostfix.html', title="Infix to Postfix", postfix=postfix, message=message)

if __name__ == '__main__':
    app.run(debug=True)
