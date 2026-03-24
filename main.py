from fastapi import FastAPI

app = FastAPI()

# Our "Database" of fruits
fruits_db = [
    {"id": 1, "name": "Apple", "color": "Red", "emoji": "🍎"},
    {"id": 2, "name": "Banana", "color": "Yellow", "emoji": "🍌"},
    {"id": 3, "name": "Blueberry", "color": "Blue", "emoji": "🫐"},
    {"id": 4, "name": "Mango", "color": "Orange", "emoji": "🥭"},
    {"id": 5, "name": "Strawberry", "color": "Red", "emoji": "🍓"},
    {"id": 6, "name": "Pineapple", "color": "Yellow", "emoji": "🍍"}
]

@app.get("/")
def home():
    return {"message": "Welcome to the Fruit API! Go to /fruits to see the list."}

# Endpoint to get the whole list
@app.get("/fruits")
def get_all_fruits():
    return fruits_db

# Endpoint to get just one fruit by its ID
@app.get("/fruits/{fruit_id}")
def get_fruit(fruit_id: int):
    for fruit in fruits_db:
        if fruit["id"] == fruit_id:
            return fruit
    return {"error": "Fruit not found"}
