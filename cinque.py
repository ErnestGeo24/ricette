from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def ricette():
  return render_template("ricette2.html")

@app.route('/pasta_carbonara')
def pastacarbo():
  return render_template("ricettacarbonare.html")

@app.route('/lasagne_bolognesi')
def lasagne_bolognesi():
  return render_template("ricettalasagne.html")

@app.route('/Pasta_alla_norma')
def pastanorma():
  return render_template("ricettapastanorma.html")

@app.route('/Pizza')
def pizza():
  return render_template("ricettapizza.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)