from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__) # с помощью этой переменной фреймворк определяет пути к корневому каталогу
menu = ["Домашняя страница", "Дневник программиста"]        # ----- создаю меню в шапке
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main_t4_dz.db" # ----- создаю базу данных
db = SQLAlchemy(app)
migrate = Migrate(app, db) # используется для все миграций


if __name__ == '__main__': #
    app.run(debug=True)

class Notes(db.Model):
    id = db.Column(db.Integer,  primary_key=True)
    title = db.Column(db.String(64), unique=True, nullable = False)
    subtitle = db.Column(db.String(60), unique=True, nullable = False)
    text = db.Column(db.String(120), unique=True, nullable = False)

@app.route('/', methods=["GET", "POST"])
def index():
    notes2 = Notes.query.all()  # получить все данные из таблицы Notes
    for notes1 in notes2:
        print(notes1.id, notes1.title, notes1.text, notes1.bugaga)
    return render_template ('home_f_t4.html', notes2=notes2)

#    if request.method == "POST":
#        title = request.form.get("title")
#        text = request.form.get("text")
#        if title and text:
#            data.append({"title": title, "text": text})
#    return render_template('home_f_t4.html', data=data, menu = menu)



data = []  # Список для хранения введенных данных
notes2 = []

@app.route("/dp", methods=["GET", "POST"])
def pd():
    if request.method == "POST":
        title = request.form.get("title")
        subtitle = request.form.get("subtitle")
        text = request.form.get("text")
        bugaga = request.form.get("bugaga")
        if title and text:
#            notes = Notes(title = title, text = text) # заносим данные в БД Notes
            notes = Notes(title = title, subtitle = subtitle, text = text, bugaga=bugaga) # заносим данные в БД Notes
            db.session.add(notes)
            db.session.commit()

    notes2 = Notes.query.all()  # получить все данные из таблицы Notes
    for notes1 in notes2:
        print(notes1.id, notes1.title, notes1.subtitle, notes1.text)


    return render_template("notes_f_t4.html", notes2=notes2)


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404
