from flask import Flask, request
from dotenv import load_dotenv
from flask_cors import CORS
from service.app_service import chat_bot_service, register_chromadb


load_dotenv()

app = Flask(__name__)
CORS(app,origins=["http://localhost:8080"])

# 챗봇과 대화 분석 및 message 반환
@app.route('/chatBot', methods=["POST"])
def index():

    message = request.get_json()['message']
    user_id = request.get_json()['user_id']
    response = chat_bot_service(user_input = message, user_id=user_id)
    
    messages = {'bot' : response}
    return messages

#상품 등록시 chromadb에 저장
@app.route('/register', methods=["POST"])
def register_product():
     register_chromadb(request.get_json())



if __name__ == "__main__":
    app.run(debug=True)

