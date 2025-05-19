from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()


@app.route("/", methods=["GET", "POST"])
def translate():
    translated_text = ""

    if request.method == "POST":
        text = request.form.get("text")
        target_lang = request.form.get("target_lang")

        if text and target_lang:
            translated_text = translator.translate(text, dest=target_lang).text

    return render_template("index.html", translated_text=translated_text)


if __name__ == "__main__":
    app.run(debug=True)
