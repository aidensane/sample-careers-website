from flask import Flask, render_template

app = Flask(__name__)

pieces = [
    {
        'name':'Punk Earings',
        'type': 'Earings',
        'price': '$$$',
        'color': 'Silver'
    },
    {
        'name':'Chained Heart Ring',
        'type': 'Ring',
        'price': '$$$',
        'color': 'Silver'
    },
    {
        'name':'Amorphous Ring',
        'type': 'Ring',
        'price': '$$$',
        'color': 'Silver'
    },
    {
        'name':'Spiked Necklace',
        'type': 'Necklace',
        'price': '$$$',
        'color': 'Silver'
    }
]

@app.route("/")
def index():
    return render_template("home.html", pieces= pieces, company_name= "Vane")

if __name__ == "__main__":
    app.run(debug=True)