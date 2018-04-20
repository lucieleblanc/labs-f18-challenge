from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/pokemon/<int:query>')
def getNameByID(query):
	return getPokemonInfo(query, 0)
	
@app.route('/pokemon/<string:query>')
def getIDByName(query):
	return getPokemonInfo(query, 1)
 
# since the API call is the same,
# why write the same code twice?
def getPokemonInfo(requestString, type):
	pokeInfo = requests.get('http://pokeapi.co/api/v2/pokemon/%s' % requestString)
	pokeInfo = pokeInfo.json()
	print (pokeInfo["id"], pokeInfo["name"])
	return render_template('pokemon.html', id=pokeInfo["id"], name=pokeInfo["name"], type=type)

if __name__ == '__main__':
    app.run()
