from flask import Flask

app=Flask(__name__)
#making obj of flask

@app.route('/')
def index():
    return 'Hello World!'

if __name__=='__main__':
    app.run(debug=True)

# plan:- this code will the backend for our chatbot, currency convertion karke result chatbot ko bhej dega
# chatbot is running on google servers
#while this is running on our local machines-->offline
#so how will this communication happen?

#ways:- code ko utha kr ke host karde kahi
# but problem is development ke time mei bohot saare changes honge --> so har baar server pr changes karne padenge with changing code
#so we will be using a tunneling software
#what it does is machine ke kisi port ko online le ata (and 8 ghante tak anyone can use it) hai yeh -->ngrok