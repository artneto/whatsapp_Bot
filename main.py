from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    print(request.values)
    reply = MessagingResponse()
    msg = reply.message()
    msg.body('Funcionou!')

    return str(reply)

@app.route('/')
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.run()
