from flask import Flask,request
import json
from bot import Bot
app = Flask(__name__)

bot = Bot()

@app.route('/',methods=['GET'])
def add():
    print "add"
    bot.create_post()
    result = {'result':200}
    return json.dumps(result)

@app.route('/',methods=['GET'])
def select():
    print select


if __name__ == '__main__':
    app.run()