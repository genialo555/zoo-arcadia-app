from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
csv_file_path = "zoo-dashboard"

app = Flask(__name__)
CORS(app)

animals = []

def load_animals_from_csv():
    global animals
    df = pd.read_csv('animals.csv')
    animals = df.to_dict(orient='records')
    df= pd.read_csv('feuille-de-soin')
    df= pd.read_csv('vaccins)')

@app.route('/load_animals', methods=['GET'])
def load_animals():
    load_animals_from_csv()
    load_feuille de Soin
    load_vaccins
    
    return jsonify({'status': 'Animals,feuille de soin,vaccins loaded from CSV', 'animals': animals,feuile-de-soin,vaccins})
    

@app.route('/add_animal', methods=['POST'])
def add_animal():
    animal = request.json
    animal['id'] = len(animals) + 1
    animals.append(animal)
    return jsonify({'status': 'Animal added', 'animal': animal})

@app.route('/get_animals', methods=['GET'])
def get_animals():
    return jsonify({'animals': animals})

@app.route('/update_animal/<int:animal_id>', methods=['POST'])
def update_animal(animal_id):
    data = request.json
    for animal in animals:
        if animal['id'] == animal_id:
            animal.update(data)
            return jsonify({'status': 'Animal updated', 'animal': animal})
    return jsonify({'status': 'Animal not found'}), 404

if __name__ == '__main__':
    load_animals_from_csv()
    app.run(debug=True)
import csv

data = [
    {"id": 1, "name": "Lion", "health": "OK", "food": "OK", "medicine": "OK"},
    {"id": 2, "name": "Tiger", "health": "OK", "food": "N/A", "medicine": "OK"},
    {"id": 3, "name": "Bear", "health": "N/A", "food": "OK", "medicine": "OK"},
    {"id": 4, "name": "Elephant", "health": "OK", "food": "OK", "medicine": "N/A"},
    {"id": 5, "name": "Zebra", "health": "N/A", "food": "N/A", "medicine": "N/A"},
    {"id": 6, "name": "Giraffe", "health": "OK", "food": "OK", "medicine": "OK"},
    {"id": 7, "name": "Kangaroo", "health": "N/A", "food": "OK", "medicine": "N/A"},
    {"id": 8, "name": "Panda", "health": "OK", "food": "N/A", "medicine": "OK"},
    {"id": 9, "name": "Koala", "health": "N/A", "food": "N/A", "medicine": "OK"},
    {"id": 10, "name": "Rhinoceros", "health": "OK", "food": "OK", "medicine": "OK"},
    {"id": 11, "name": "Hippopotamus", "health": "N/A", "food": "OK", "medicine": "OK"},
    {"id": 12, "name": "Leopard", "health": "OK", "food": "OK", "medicine": "N/A"},
    {"id": 13, "name": "Cheetah", "health": "N/A", "food": "N/A", "medicine": "N/A"},
    {"id": 14, "name": "Camel", "health": "OK", "food": "OK", "medicine": "OK"},
    {"id": 15, "name": "Gazelle", "health": "N/A", "food": "N/A", "medicine": "OK"},
    {"id": 16, "name": "Bison", "health": "OK", "food": "OK", "medicine": "N/A"},
    {"id": 17, "name": "Antelope", "health": "N/A", "food": "OK", "medicine": "N/A"},
    {"id": 18, "name": "Baboon", "health": "OK", "food": "N/A", "medicine": "OK"},
    {"id": 19, "name": "Orangutan", "health": "N/A", "food": "OK", "medicine": "OK"},
    {"id": 20, "name": "Chimpanzee", "health": "OK", "food": "OK", "medicine": "OK"},
    {"id": 21, "name": "Gorilla", "health": "N/A", "food": "N/A", "medicine": "OK"},
    {"id": 22, "name": "Jaguar", "health": "OK", "food": "OK", "medicine": "N/A"},
    {"id": 23, "name": "Wolf", "health": "N/A", "food": "OK", "medicine": "N/A"},
    {"id": 24, "name": "Fox", "health": "OK", "food": "N/A", "medicine": "OK"},
    {"id": 25, "name": "Raccoon", "health": "N/A", "food": "OK", "medicine": "OK"},
    {"id": 26, "name": "Owl", "health": "OK", "food": "OK", "medicine": "OK"},
    {"id": 27, "name": "Eagle", "health": "N/A", "food": "N/A", "medicine": "OK"},
    {"id": 28, "name": "Falcon", "health": "OK", "food": "OK", "medicine": "N/A"},
    {"id": 29, "name": "Penguin", "health": "N/A", "food": "OK", "medicine": "N/A"},
    {"id": 30, "name": "Seal", "health": "OK", "food": "N/A", "medicine": "OK"},
    {"id": 31, "name": "Whale", "health": "N/A", "food": "OK", "medicine": "OK"},
    {"id": 32, "name": "Dolphin", "health": "OK", "food": "OK", "medicine": "OK"},
    {"id": 33, "name": "Shark", "health": "N/A", "food": "N/A", "medicine": "OK"},
    {"id": 34, "name": "Crocodile", "health": "OK", "food": "OK", "medicine": "N/A"},
    {"id": 35, "name": "Alligator", "health": "N/A", "food": "OK", "medicine": "N/A"},
    {"id": 36, "name": "Tortoise", "health": "OK", "food": "N/A", "medicine": "OK"},
    {"id": 37, "name": "Turtle", "health": "N/A", "food": "OK", "medicine": "OK"},
    {"id": 38, "name": "Frog", "health": "OK", "food": "OK", "medicine": "OK"},
    {"id": 39, "name": "Toad", "health": "N/A", "food": "N/A", "medicine": "OK"},
    {"id": 40, "name": "Snake", "health": "OK", "food": "OK", "medicine": "N/A"},
    {"id": 41, "name": "Lizard", "health": "N/A", "food": "OK", "medicine": "N/A"},
    {"id": 42, "name": "Gecko", "health": "OK", "food": "N/A", "medicine": "OK"},
    {"id": 43, "name": "Iguana", "health": "N/A", "food": "OK", "medicine": "OK"},
    {"id": 44, "name": "Chameleon", "health": "OK", "food": "OK", "medicine": "OK"},
    {"id": 45, "name": "Dragon", "health": "N/A", "food": "N/A", "medicine": "OK"}
]