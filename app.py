from flask import Flask, render_template
import random
import os

app = Flask(__name__)

# List of random text to display
random_texts = [
    "Hello, welcome to my Flask app!",
    "This is a random text generator.",
    "Flask is awesome for web development.",
    "You are viewing a dynamically generated page.",
    "Randomness makes things interesting!"
]

@app.route('/')
def home():
    # Select a random text
    selected_text = random.choice(random_texts)
    return render_template('index.html', text=selected_text)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)