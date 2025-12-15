from flask import Flask, jsonify, render_template_string
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Docker App</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            background: white;
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            max-width: 600px;
            width: 100%;
            text-align: center;
        }
        h1 {
            color: #667eea;
            margin-bottom: 20px;
            font-size: 2.5em;
        }
        .badge {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 10px 20px;
            border-radius: 25px;
            display: inline-block;
            margin: 10px 0;
            font-weight: bold;
        }
        .info {
            margin: 20px 0;
            padding: 20px;
            background: #f7f7f7;
            border-radius: 10px;
            border-left: 4px solid #667eea;
        }
        .emoji {
            font-size: 4em;
            margin: 20px 0;
        }
        a {
            color: #667eea;
            text-decoration: none;
            font-weight: bold;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="emoji">🐍🐳</div>
        <h1>Flask Docker App</h1>
        <div class="badge">Python {{ python_version }}</div>
        <div class="badge">Flask {{ flask_version }}</div>
        <div class="info">
            <p><strong>Status:</strong> Running in Docker Container ✅</p>
            <p><strong>Port:</strong> 5000</p>
            <p><strong>Environment:</strong> {{ environment }}</p>
        </div>
        <p>Visit <a href="/api/health">/api/health</a> for API endpoint</p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    import sys
    import flask
    return render_template_string(
        HTML_TEMPLATE,
        python_version=f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        flask_version=flask.__version__,
        environment=os.getenv('ENVIRONMENT', 'development')
    )

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'app': 'Flask Docker App',
        'version': '1.0.0',
        'container': True
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
