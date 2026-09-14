from flask import Flask

app=Flask(__name__)
#making obj of flask

@app.route('/')
def index():
    return 'Hello World!'

if __name__=='__main__':
    app.run(debug=True)