import requests
import json
from flask import Flask


def get_valutes_list():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = json.loads(response.text)
    valutes = list(data['Valute'].values())
    return valutes


app = Flask(__name__)


def create_html(valutes):
    text = '<html>\n<head>\n'
    text += '  <title>Таблица валют</title>\n'
    text += ('  <style type="text/css">\n'
             '    TABLE {\n'
             '           border-collapse: collapse; /* Убираем двойные линии между ячейками */\n'
             '          }\n'
             '    TD, TH {\n'
             '            padding: 3px; /* Поля вокруг содержимого таблицы */\n'
             '            border: 1px solid black; /* Параметры рамки */\n'
             '           }\n'
             '    TH {\n'
             '        background: #b0e0e6; /* Цвет фона */\n'
             '       }\n'
             '  </style>\n')
    text += '</head>\n'
    text += '<body>\n'
    text += '  <h1>Курс валют</h1>\n'
    text += '  <table>\n'
    text += '    <tr>\n'
    for title_cols in valutes[0]:
        text += f'      <th>{title_cols}</th>\n'
    text += '    </tr>\n'
    for valute in valutes:
        text += '    <tr>\n'
        for v in valute.values():
            text += f'      <td>{v}</td>\n'
        text += '    </tr>\n'

    text += '  </table>\n'
    text += '</body>\n</html>'
    return text


@app.route("/")
def index():
    valutes = get_valutes_list()
    html = create_html(valutes)
    return html


if __name__ == "__main__":
    app.run()
