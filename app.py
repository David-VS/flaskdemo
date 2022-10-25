from flask import Flask, request

app = Flask(__name__)

shopping_list = ["melk", "bloem"]

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/shopping')
def get_shopping_list():
    return shopping_list

@app.route('/shopping/<int:index>') #path variabele, altijd 1
def get_from_shopping_list_by_index(index):
    return shopping_list[index]

#http://127.0.0.1:5000/shopping/add?i=suiker #query parameters, kunnen meerdere zijn
@app.route('/shopping/add')
def add_to_shopping_list():
    item = request.args.get("i")
    shopping_list.append(item)
    return "gelukt"

#http://127.0.0.1:5000/shopping/add data in een formulier #query parameters, kunnen meerdere zijn
#gevoelige data altijd in form, niet over GET sturen
@app.route('/shopping/add2', methods=["POST"])
def add_to_shopping_list():
    item = request.form["i"]
    shopping_list.append(item)
    return "gelukt"

if __name__ == '__main__':
    app.run()
