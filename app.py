from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for multiple cities
city_data = {
    "madurai": {
        "city": "Madurai",
        "temperature": 32,
        "humidity": 58,
        "status": "Sunny",
        "air_quality": "Good"
    },
    "chennai": {
        "city": "Chennai",
        "temperature": 30,
        "humidity": 70,
        "status": "Cloudy",
        "air_quality": "Moderate"
    },
    "coimbatore": {
        "city": "Coimbatore",
        "temperature": 28,
        "humidity": 65,
        "status": "Partly Cloudy",
        "air_quality": "Good"
    },
    "trichy": {
        "city": "Trichy",
        "temperature": 34,
        "humidity": 60,
        "status": "Sunny",
        "air_quality": "Moderate"
    },
    "bangalore": {
        "city": "Bangalore",
        "temperature": 25,
        "humidity": 75,
        "status": "Rainy",
        "air_quality": "Good"
    }
}

# Homepage route
@app.route("/")
def home():
    return "Welcome! Try /get/<city_name> to get city info."

# Dynamic GET request based on city name
@app.route("/get/<city_name>")
def get_city(city_name):
    city_name = city_name.lower()
    if city_name in city_data:
        return jsonify(city_data[city_name])
    else:
        return jsonify({"error": "City not found"}), 404

# POST request - add new city
@app.route("/create-city", methods=['POST'])
def create_city():
    data = request.get_json()
    city_name = data.get("city", "").lower()
    if not city_name:
        return jsonify({"error": "City name is required"}), 400
    
    city_data[city_name] = data
    return jsonify({"message": "City data added successfully", "data": data}), 201

# PUT request - update existing city
@app.route("/update-city/<city_name>", methods=['PUT'])
def update_city(city_name):
    city_name = city_name.lower()
    if city_name not in city_data:
        return jsonify({"error": "City not found"}), 404

    data = request.get_json()
    city_data[city_name].update(data)  # update only provided fields
    return jsonify({"message": "City data updated successfully", "data": city_data[city_name]}), 200

# DELETE request - remove a city
@app.route("/delete-city/<city_name>", methods=['DELETE'])
def delete_city(city_name):
    city_name = city_name.lower()
    if city_name not in city_data:
        return jsonify({"error": "City not found"}), 404

    deleted_city = city_data.pop(city_name)
    return jsonify({"message": "City deleted successfully", "data": deleted_city}), 200


if __name__ == '__main__':
    app.run(debug=True)
