from flask import Flask, url_for


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

@app.route("/promotion_image")
def promotion_mars():
    return f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
    <title>Колонизация</title>
</head>

<body>
    <h1>Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='img/mars.jpg')}" alt="картинка планеты Марс">
    <p style="background-color: grey;">Человечество вырастает из детства.</p>
    <p style="background-color: green;">Человечеству мала одна планета.</p>
    <p style="background-color: grey;">Мы сделаем обитаемыми безжизненные пока планеты.</p>
    <p style="background-color: yellow;">И начнем с Марса!</p>
    <p style="background-color: red;">Присоединяйся!</p>
</body>

</html>"""

@app.route("/astronaut_selection")
def otbor():
    return f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
    <title>Отбор астронавтов</title>
</head>

<body>
    <h1>Анкета претендента</h1>
    <p>на участие в миссии</p>
    <div class="form_for_astronaut">
        <form action="" class="form_cont">
            <input type="text" placeholder="Введите фамилию">
            <input type="text" placeholder="Введите имя">
            <input type="email" name="Введите адрес почты" id="">
            <div>
                <label for="education">Какое у Вас образование?</label>
                <select name="class" id="education">
                    <option>нет</option>
                    <option>основное общее</option>
                    <option>среднее общее</option>
                    <option>среднее профессиональное</option>
                    <option>высшее</option>
                </select>
            </div>
            <div>
                <input type="checkbox" id="ii">
                <label for="ii">Инженер-исследователь</label>
                <input type="checkbox" id="is">
                <label for="is">Инженер-строитель</label>
                <input type="checkbox" id="p">
                <label for="p">Пилот</label>
                <input type="checkbox" id="m">
                <label for="m">Метеоролог</label>
                <input type="checkbox" id="ipz">
                <label for="ipz">Инженер по жизнеобеспечению</label>
                <input type="checkbox" id="iprz">
                <label for="iprz">Инженер по радиационной защите</label>
                <input type="checkbox" id="v">
                <label for="v">Врач</label>
                <input type="checkbox" id="e">
                <label for="e">Экзобиолог</label>
            </div>
            <div class="form-group">
                <label for="form-check">Укажите пол</label>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                    <label class="form-check-label" for="male">
                        Мужской
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                    <label class="form-check-label" for="female">
                        Женский
                    </label>
                </div>
            </div>
            <div class="form-group">
                <label for="about">Немного о себе</label>
                <textarea class="form-control" id="about" rows="3" name="about"></textarea>
            </div>
            <div class="form-group">
                <label for="photo">Приложите фотографию</label>
                <input type="file" class="form-control-file" id="photo" name="file">
            </div>
            <div>
                <input type="checkbox" id="question">
                <label for="question">Готовы остаться на Марсе?</label>
            </div>
            <button type="submit">Записаться</button>
        </form>
    </div>
</body>

</html>"""

@app.route("/choice/<planet_name>")
def choice(planet_name):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Варианты выбора</title>
</head>
<body>
    <h1>Мое предложение: {planet_name}</h1>
    <h2>Эта планета близка к земле;</h2>
    <p style="background-color: rgba(0, 128, 0, 0.3); ">На ней много необходимых ресурсов;</p>
    <p style="background-color: rgba(128, 128, 128, 0.3); ">На ней есть вода и атмосфера;</p>
    <p style="background-color: rgba(238, 242, 3, 0.3); ">На ней есть небольшое магнитное поле;</p>
    <p style="background-color: rgba(255, 0, 0, 0.3); ">Наконец, она просто красива;</p>
</body>
</html>"""

@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    return f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Результаты</title>
</head>

<body>
    <h1>Результаты отбора</h1>
    <h2>Претендента на участие в миссии {nickname}</h2>
    <p style="background-color: rgba(0, 255, 0, 0.3);">Поздравляем! Ваш рейтинг после {level} отбора</p>
    <p>составляет {rating}</p>
    <p style="background-color: rgba(251, 255, 5, 0.3);">Желаем удачи!</p>
</body>

</html>"""


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")