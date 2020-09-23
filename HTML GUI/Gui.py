from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/addTeilnehmer")
def teilnehmer_eintragen():
    return "Hallo Welt"
    
if __name__ == '__main__':
    app.run(port=5001, debug=True)
