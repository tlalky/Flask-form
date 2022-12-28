from flask import Flask, render_template, request
import csv

app = Flask(__name__)


@app.route("/")
def index():
    #name = request.args.get("name", "world")  # get provided name from URL # default == world
    return render_template("index.html")  #, name=name


@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("name") or not request.form.get("sex") or not request.form.get('phone_number') or not request.form.get('bdaymonth'):
        return render_template("failure.html")

    with open('registered.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow((request.form.get('name'), request.form.get('sex'), request.form.get('phone_number'), request.form.get('bdaymonth')))
    return render_template("success.html")


@app.route("/registered")
def registered():
    with open('registered.csv', 'r') as file:
        reader = csv.reader(file)
        people = list(reader)
    return render_template('registered.html', people=people)



"""name = request.form.get("name")  # method="get" => args
    sex = request.form.get("sex")  # method="post" => form
    if not name or not sex:
        return render_template("failure.html")
    return render_template("success.html")"""
