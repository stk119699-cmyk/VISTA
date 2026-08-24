from flask import Flask, render_template_string
import requests

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Hey Vista</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 20px; }
        h2 { color: #333; }
    </style>
</head>
<body>
    <h2>Hey Vista App is Working!</h2>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
