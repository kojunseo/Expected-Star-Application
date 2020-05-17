
from flask import Flask, render_template, request, redirect, send_file
import scrapper
import find_exp
app = Flask("SuperScrapper")

db = {}
data_pd ={}
not_first = False
@app.route("/")
def home():
    return render_template("main_board.html")


@app.route("/expected_star")
def expected_star():
    return render_template("expected.html")


@app.route("/expected_star/result")
def expected_star_result():
    id_ = request.args.get("ID")
    star = find_exp.get_expected(id_)

    return render_template("expected_result.html", star = star, contents = id_)


@app.route("/export")
def export():
    return send_file("data_analize.csv")




app.run(host = "0.0.0.0")