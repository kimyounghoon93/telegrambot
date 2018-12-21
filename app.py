import os
import requests
from flask import Flask, request
app = Flask(__name__)

token = os.getenv('TELEGRAM_BOT_TOKEN')

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route(f'/{token}', methods=['POST'])
def telegram():
    
    from_telegram = request.get_json() #=>dict
    print(from_telegram)
    
    # 2. 그대로 돌려보내기 (메아리)
    # ['message'] #=키가 없으면 에러
    # .get('message') #=>키가 없음 none이 나옴
    if from_telegram.get('message') is not None:
        chat_id = from_telegram['message']['from']['id']
        text = from_telegram['message']['text']
        # 주소수정 api.telegram.org => api.hphk.io/telegram
        requests.get(f'https://api.hphk.io/telegram/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    
    
    return '', 200

if __name__ == '__main__':
    app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',8080)))