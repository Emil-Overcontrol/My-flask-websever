from flask import Flask, request, render_template, redirect, url_for

namey = "permanent_name"  # Global variable to store the name across requests
# The project already uses a capitalized "Static" folder.
app = Flask(__name__, static_folder='Static')


@app.route('/')
def home():
    """Send visitors from the server's front page to the form."""
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('username', '').strip()
        if not name:
            return render_template('name.html', error='Please enter a name.')
        return f"Hello {name}, POST request received"
    return render_template('name.html')

@app.route('/hello', methods=['GET', 'POST'])
def hello ():
    namey = None  # Reset namey for each request
    if request.method == 'POST':
        namey = request.form.get('permanent_name', '').strip()
        if  namey is None or namey == '':
            return render_template('about_me_page.html', error='Please enter a name.')
        
    return render_template('about_me_page.html', namey = namey)     
    

if __name__ == '__main__':
    app.run(debug=True)
