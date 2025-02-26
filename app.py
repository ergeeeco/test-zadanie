from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args.get('name')
    message = request.args.get('message')

    # Возвращаем ответ с подставленными значениями
    return f'Hello {name}! {message}'


if __name__ == '__main__':
    # Запуск приложения на localhost:5000
    app.run(host='0.0.0.0', port=5000)