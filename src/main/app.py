import tensorflow as tf
import pandas as pd
import numpy as np

# Dummy data for properties and user preferences
properties = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "name": ["Beach House", "Mountain Cabin", "City Apartment", "Lake Villa", "Desert Retreat"],
    "price": [300, 200, 150, 400, 250],
    "category": ["beach", "mountain", "city", "lake", "desert"]
})

user_preferences = {"beach": 0.8, "mountain": 0.6, "city": 0.7, "lake": 0.9, "desert": 0.5}

# Recommendation model function
def recommend_properties(user_preferences, properties):
    # Normalize user preferences
    user_vector = np.array([user_preferences[cat] for cat in properties['category']])
    property_vector = np.eye(len(properties['category']))

    # Compute recommendations using a dummy neural network
    model = tf.keras.Sequential([
        tf.keras.layers.InputLayer(input_shape=(len(user_vector),)),
        tf.keras.layers.Dense(5, activation='relu'),
        tf.keras.layers.Dense(len(properties), activation='softmax')
    ])

    model.compile(optimizer='adam', loss='categorical_crossentropy')
    model.fit(property_vector, user_vector, epochs=10, verbose=0)

    # Generate scores
    scores = model.predict(property_vector)
    properties['score'] = scores.flatten()
    return properties.sort_values(by='score', ascending=False)

# Flask API to expose recommendations
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    user_prefs = request.json.get("preferences", user_preferences)
    recommendations = recommend_properties(user_prefs, properties)
    return jsonify(recommendations.head(3).to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
