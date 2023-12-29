
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

EDAMAM_APP_ID = '3b3bc1eb'
EDAMAM_APP_KEY = '9dad6a5a8b77ddab994547ed6ffb0987'

@app.route('/', methods=['GET', 'POST'])
def home():
    recipes = []
    if request.method == 'POST':
        query = request.form.get('recipe_query')
        recipes = get_recipes_from_edamam(query)
    return render_template('index.html', recipes=recipes)

def get_recipes_from_edamam(query):
    base_url = 'https://api.edamam.com/search'
    params = {
        'q': query,
        'app_id': EDAMAM_APP_ID,
        'app_key': EDAMAM_APP_KEY,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        print(data)  # Print API response for debugging
        return data.get('hits', [])
    except requests.exceptions.RequestException as e:
        print(f'Error: {str(e)}')
        return []

if __name__ == '__main__':
    app.run()
