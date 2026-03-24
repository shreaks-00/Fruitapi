from fastapi import FastAPI, HTTPException

app = FastAPI()

# Our "Database" of fruits
fruits_db = [
    {"id": 1, "name": "Apple", "color": "Red", "emoji": "🍎"},
    {"id": 2, "name": "Banana", "color": "Yellow", "emoji": "🍌"},
    {"id": 3, "name": "Orange", "color": "Orange", "emoji": "🍊"},
    {"id": 4, "name": "Strawberry", "color": "Red", "emoji": "🍓"},
    {"id": 5, "name": "Grapes", "color": "Purple", "emoji": "🍇"},
    {"id": 6, "name": "Watermelon", "color": "Green", "emoji": "🍉"},
    {"id": 7, "name": "Cherry", "color": "Red", "emoji": "🍒"},
    {"id": 8, "name": "Mango", "color": "Orange", "emoji": "🥭"},
    {"id": 9, "name": "Pineapple", "color": "Yellow", "emoji": "🍍"},
    {"id": 10, "name": "Peach", "color": "Pink", "emoji": "🍑"},
    {"id": 11, "name": "Pear", "color": "Green", "emoji": "🍐"},
    {"id": 12, "name": "Kiwi", "color": "Brown", "emoji": "🥝"},
    {"id": 13, "name": "Blueberry", "color": "Blue", "emoji": "🫐"},
    {"id": 14, "name": "Lemon", "color": "Yellow", "emoji": "🍋"},
    {"id": 15, "name": "Lime", "color": "Green", "emoji": "🍋‍🟩"},
    {"id": 16, "name": "Coconut", "color": "Brown", "emoji": "🥥"},
    {"id": 17, "name": "Melon", "color": "Green", "emoji": "🍈"},
    {"id": 18, "name": "Green Apple", "color": "Green", "emoji": "🍏"},
    {"id": 19, "name": "Tangerine", "color": "Orange", "emoji": "🍊"},
    {"id": 20, "name": "Tomato", "color": "Red", "emoji": "🍅"},
    {"id": 21, "name": "Eggplant", "color": "Purple", "emoji": "🍆"},
    {"id": 22, "name": "Avocado", "color": "Green", "emoji": "🥑"},
    {"id": 23, "name": "Pomegranate", "color": "Red", "emoji": "🍎"},
    {"id": 24, "name": "Apricot", "color": "Orange", "emoji": "🍑"},
    {"id": 25, "name": "Plum", "color": "Purple", "emoji": "🫐"},
    {"id": 26, "name": "Dragonfruit", "color": "Pink", "emoji": "🌵"},
    {"id": 27, "name": "Fig", "color": "Purple", "emoji": "🟣"},
    {"id": 28, "name": "Guava", "color": "Green", "emoji": "🍐"},
    {"id": 29, "name": "Lychee", "color": "Red", "emoji": "🔴"},
    {"id": 30, "name": "Papaya", "color": "Orange", "emoji": "🥭"},
    {"id": 31, "name": "Passionfruit", "color": "Purple", "emoji": "🟣"},
    {"id": 32, "name": "Raspberry", "color": "Red", "emoji": "🍓"},
    {"id": 33, "name": "Blackberry", "color": "Black", "emoji": "🫐"},
    {"id": 34, "name": "Cranberry", "color": "Red", "emoji": "🍒"},
    {"id": 35, "name": "Elderberry", "color": "Purple", "emoji": "🍇"},
    {"id": 36, "name": "Grapefruit", "color": "Pink", "emoji": "🍊"},
    {"id": 37, "name": "Kumquat", "color": "Orange", "emoji": "🟠"},
    {"id": 38, "name": "Starfruit", "color": "Yellow", "emoji": "⭐"},
    {"id": 39, "name": "Durian", "color": "Green", "emoji": "🍈"},
    {"id": 40, "name": "Jackfruit", "color": "Yellow", "emoji": "🍍"},
    {"id": 41, "name": "Persimmon", "color": "Orange", "emoji": "🍅"},
    {"id": 42, "name": "Cantaloupe", "color": "Orange", "emoji": "🍈"},
    {"id": 43, "name": "Honeydew", "color": "Green", "emoji": "🍏"},
    {"id": 44, "name": "Plantain", "color": "Yellow", "emoji": "🍌"},
    {"id": 45, "name": "Gooseberry", "color": "Green", "emoji": "🟢"},
    {"id": 46, "name": "Mulberry", "color": "Purple", "emoji": "🍇"},
    {"id": 47, "name": "Olive", "color": "Green", "emoji": "🫒"},
    {"id": 48, "name": "Dates", "color": "Brown", "emoji": "🌴"},
    {"id": 49, "name": "Currant", "color": "Red", "emoji": "🍒"},
    {"id": 50, "name": "Quince", "color": "Yellow", "emoji": "🍏"},
    {"id": 51, "name": "Cactus Fruit", "color": "Pink", "emoji": "🌵"}
]

@app.get("/")
def home():
    return {"message": "Welcome to the Fruit API! Go to /fruits to see the list."}

@app.get("/fruits")
def get_all_fruits():
    return fruits_db

@app.get("/fruits/{fruit_id}")
def get_fruit(fruit_id: int):
    for fruit in fruits_db:
        if fruit["id"] == fruit_id:
            return fruit
    # If not found, return a 404 error
    raise HTTPException(status_code=404, detail="Fruit not found")
