from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Jenkins CI/CD Pipeline on AWS!"

if __name__ == '__main__':
    # Keep Flask running on all interfaces for Docker
    app.run(host='0.0.0.0', port=8080, debug=True)
