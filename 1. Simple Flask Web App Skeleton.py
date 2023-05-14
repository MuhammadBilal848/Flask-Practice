from flask import Flask

# WSGI Application
app = Flask(__name__)

@app.route('/')
def home():
    return 'Drop your video here'


@app.route('/download')
def download():
    return 'Download your video here'



if __name__ == '__main__':
    app.run(debug=True) 