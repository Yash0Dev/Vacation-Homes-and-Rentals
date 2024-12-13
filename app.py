import tensorflow as tf
import pandas as pd
import numpy as np
from flask_cors import CORS
from flask import Flask, jsonify, request

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
    # Normalize user preferences and properties
    user_vector = np.array([user_preferences[cat] for cat in properties['category']])
    
    # Generate property vectors (one-hot encoding of categories)
    property_vector = pd.get_dummies(properties['category']).values
    
    # Ensure user_vector is 2D for compatibility
    user_vector = user_vector.reshape(-1, 1)  # Shape (5, 1)

    # Define model
    model = tf.keras.Sequential([
        tf.keras.layers.InputLayer(input_shape=(1,)),  # Input layer should match user_vector
        tf.keras.layers.Dense(5, activation='relu'),
        tf.keras.layers.Dense(1, activation='linear')  # Single output: recommendation score for each property
    ])

    model.compile(optimizer='adam', loss='mse')  # Using Mean Squared Error for regression-based scoring
    
    # Fit the model to the user preferences
    model.fit(user_vector, property_vector, epochs=10, verbose=0)

    # Generate recommendations by predicting scores
    scores = model.predict(user_vector)

    # Add the scores to the properties DataFrame
    properties['score'] = scores.flatten()

    # Sort properties by score and return the top 3 recommendations
    return properties.sort_values(by='score', ascending=False)

# Flask API to expose recommendations
app = Flask(__name__)
CORS(app)

@app.route('/recommend', methods=['POST'])
def recommend():
    user_prefs = request.json.get("preferences", user_preferences)
    recommendations = recommend_properties(user_prefs, properties)
    return jsonify(recommendations.head(3).to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
