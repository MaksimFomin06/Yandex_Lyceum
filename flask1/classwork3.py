from flask import Flask


app = Flask(__name__)

@app.route("/")
def mission_name():
    return "Миссия Колонизация Марса"

@app.route("/index")
def index():
    return "И на Марсе будут яблони цвести!"

@app.route("/promotion")
def promotion():
    return f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>task 2</title>
</head>

<body>
    <p>Человечество вырастает из детства.</p>
    <p>Человечеству мала одна планета.</p>
    <p>Мы сделаем обитаемыми безжизненные пока планеты.</p>
    <p>И начнем с Марса!</p>
    <p>Присоединяйся!</p>
</body>

</html>"""

@app.route("/image_mars")
def image_mars():
    return f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Привет, Марс!</title>
</head>

<body>
    <h1>Жди нас, Марс!</h1>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/OSIRIS_Mars_true_color.jpg/307px-OSIRIS_Mars_true_color.jpg" alt="картинка планеты Марс">
    <p>Вот она какая, красная планета.</p>
</body>

</html>"""


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")