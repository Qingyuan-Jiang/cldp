from flask import Flask, render_template_string
import os

app = Flask(__name__)

# Read the HTML content
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)