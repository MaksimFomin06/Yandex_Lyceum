from flask import Flask, request, url_for, render_template


app = Flask(__name__)


@app.route("/")
@app.route("/index/<substitution>")
def index(substitution=None):
    context = {
        "substitution": substitution,
    }
    
    return render_template("index.html", **context)


@app.route("/list_prof/<list_type>")
def prof_list(list_type):
    prof_lst = ("инженер-исследователь", "пилот", "строитель", "экзобиолог", "врач", "инженер по терраформироаванию", "климатолог", "специалист по радиационной защите", "астрогеолог", "гляциолог", "инженер жизнеобеспечения", "метеоролог", "оператор марсохода", "киберинженер", "штурман", "пилот дронов")
    context = {
        "professions": prof_lst,
        "list_type": list_type
    }
    
    return render_template("list_prof.html", **context)



if __name__ == "__main__":
    app.run(port=8000, host='127.0.0.1')