from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')

def home():
    return render_template('index.html')

@app.route('/<name>')
def about(name):
    aboutus=['Ceo','Company','aboutus']
    return render_template('aboutus.html',about=aboutus, my_name=name)

@app.route('/<name>/<int:age>')
def favanimes(name,age):
    animes=['Death Note','One Piece','Atack On Titan']
    return render_template('anime.html',lists=animes,my_name1=name,my_age=age)


if __name__=='__main__':
    app.run(debug=True)
