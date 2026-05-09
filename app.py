"""
EUREKA! — College Lost & Found Platform
Flask backend — replaces the Node/Vite dev server.
Run:  python app.py
"""

import json
import os
import time
from datetime import datetime
from flask import Flask, jsonify, request, render_template, abort

app = Flask(__name__)

# ── Persistent storage ────────────────────────────────────────────────────────
DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")

MOCK_ITEMS = [
    {
        "id": 1, "title": 'MacBook Pro 14"',
        "description": "Silver MacBook Pro with a sticker of a mountain on the lid. Charger included.",
        "category": "Electronics", "location": "Library, 2nd Floor",
        "date": "2026-04-22", "status": "lost",
        "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400&q=80",
    },
    {
        "id": 2, "title": "Blue Water Bottle",
        "description": "Hydro Flask, blue, 32oz. Has initials A.K. on the bottom.",
        "category": "Accessories", "location": "Gym / Sports Complex",
        "date": "2026-04-21", "status": "lost",
        "image_url": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=400&q=80",
    },
    {
        "id": 3, "title": "AirPods Pro (Gen 2)",
        "description": 'White AirPods Pro in a white case. Engraved with "Riya" on the back.',
        "category": "Electronics", "location": "Cafeteria",
        "date": "2026-04-20", "status": "lost",
        "image_url": "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=400&q=80",
    },
    {
        "id": 4, "title": "Student ID Card",
        "description": "ID card for student Arjun Mehta, Dept. of Computer Science.",
        "category": "Documents", "location": "Main Gate",
        "date": "2026-04-19", "status": "lost",
        "image_url": "https://images.unsplash.com/photo-1544027993-37dbfe43562a?w=400&q=80",
    },
    {
        "id": 5, "title": "Prescription Glasses",
        "description": "Black-framed rectangular glasses in a brown leather case.",
        "category": "Accessories", "location": "Seminar Hall B",
        "date": "2026-04-18", "status": "lost",
        "image_url": "https://images.unsplash.com/photo-1574258495973-f010dfbb5371?w=400&q=80",
    },
    {
        "id": 6, "title": "Purple Backpack",
        "description": "Found a purple Wildcraft backpack with textbooks inside near Block C.",
        "category": "Bags", "location": "Block C, Near Staircase",
        "date": "2026-04-22", "status": "found",
        "image_url": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400&q=80",
    },
    {
        "id": 7, "title": "Calculator (Casio fx-991)",
        "description": "Scientific calculator found in Room 204 after a maths class.",
        "category": "Electronics", "location": "Room 204, Academic Block",
        "date": "2026-04-21", "status": "found",
        "image_url": "https://images.unsplash.com/photo-1611532736597-de2d4265fba3?w=400&q=80",
    },
    {
        "id": 8, "title": "Car Keys (Honda)",
        "description": "Honda car keys with a small elephant keychain found in the parking lot.",
        "category": "Keys", "location": "Parking Lot",
        "date": "2026-04-20", "status": "found",
        "image_url": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400&q=80",
    },
    {
        "id": 9, "title": "Notebook (Engineering Maths)",
        "description": 'Spiral-bound notebook filled with maths notes. Name "Priya" on first page.',
        "category": "Books", "location": "Reading Room",
        "date": "2026-04-19", "status": "found",
        "image_url": "https://images.unsplash.com/photo-1507842217343-583bb7270b66?w=400&q=80",
    },
    {
        "id": 10, "title": "Umbrella (Black, Large)",
        "description": "Large black umbrella with a wooden handle found near the bus stop.",
        "category": "Accessories", "location": "Bus Stop / Main Gate",
        "date": "2026-04-18", "status": "found",
        "image_url": "https://images.unsplash.com/photo-1558618047-f4e80c0d56e5?w=400&q=80",
    },
]


def load_items():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    # First run — seed with mock data
    save_items(MOCK_ITEMS)
    return list(MOCK_ITEMS)


def save_items(items):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)


# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


# GET /api/items  — list with optional query params
@app.route("/api/items", methods=["GET"])
def get_items():
    items = load_items()
    status   = request.args.get("status", "").strip()
    category = request.args.get("category", "").strip()
    location = request.args.get("location", "").strip()
    search   = request.args.get("search", "").strip().lower()
    date_from = request.args.get("dateFrom", "").strip()

    if status:
        items = [i for i in items if i.get("status") == status]
    if category:
        items = [i for i in items if i.get("category", "").lower() == category.lower()]
    if location:
        items = [i for i in items if location.lower() in i.get("location", "").lower()]
    if search:
        items = [i for i in items
                 if search in i.get("title", "").lower()
                 or search in i.get("description", "").lower()]
    if date_from:
        try:
            df = datetime.strptime(date_from, "%Y-%m-%d")
            items = [i for i in items
                     if datetime.strptime(i["date"], "%Y-%m-%d") >= df]
        except ValueError:
            pass

    items.sort(key=lambda i: i.get("date", ""), reverse=True)
    return jsonify(items)


# POST /api/items  — create a new item
@app.route("/api/items", methods=["POST"])
def create_item():
    body = request.get_json(silent=True) or {}
    required = ["title", "description", "category", "location", "date", "status"]
    for field in required:
        if not body.get(field, "").strip():
            return jsonify({"error": f"'{field}' is required."}), 400

    items = load_items()
    new_id = int(time.time() * 1000)
    new_item = {
        "id":          new_id,
        "title":       body["title"].strip(),
        "description": body["description"].strip(),
        "category":    body["category"].strip(),
        "location":    body["location"].strip(),
        "date":        body["date"].strip(),
        "status":      body["status"].strip(),
        "image_url":   body.get("image_url", "").strip() or None,
    }
    items.insert(0, new_item)
    save_items(items)
    return jsonify({"data": new_item}), 201


# POST /api/login  — mock authentication
@app.route("/api/login", methods=["POST"])
def login():
    body = request.get_json(silent=True) or {}
    email    = body.get("email", "").strip()
    password = body.get("password", "")
    if email and len(password) >= 6:
        return jsonify({"user": {"email": email, "id": f"user-{int(time.time()*1000)}"}}), 200
    return jsonify({"error": "Invalid email or password."}), 401


# POST /api/signup  — mock sign-up
@app.route("/api/signup", methods=["POST"])
def signup():
    body = request.get_json(silent=True) or {}
    email    = body.get("email", "").strip()
    password = body.get("password", "")
    if email and len(password) >= 6:
        return jsonify({"user": {"email": email, "id": f"user-{int(time.time()*1000)}"}}), 201
    return jsonify({"error": "Password must be at least 6 characters."}), 400


if __name__ == "__main__":
    print("EUREKA! running at http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
