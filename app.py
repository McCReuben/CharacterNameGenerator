import os
import openai
from flask import Flask, request, redirect, render_template, url_for

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

def make_prompt(characteristic):
    return """Suggest 3 names for an rpg charater in a Fantasy.
Charater: Bard
Names: Malcius Thorsalan, Bevis Bardigan, Trelgath Fylar 
Charater: Hero
Names: Abby Angel, Raven the Brave, Remus Dwindlesword
Character: Villain
Names: Zephyr the Dark, Nictis Stingray, Hades Keeling
Charater: {}
Names:""".format(
        characteristic.capitalize()
    )



@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        charataristic = request.form["characteristic"]
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=make_prompt(charataristic),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    print(result)
    return render_template("index.html", result=result)






