
from fastapi import FastAPI
import joblib
import numpy as np

# Load model
model = joblib.load("price_model.pkl")

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Dynamic Pricing API is running"}

# Prediction API
@app.post("/predict")
def predict(
    latitude: float,
    longitude: float,
    minimum_nights: int,
    number_of_reviews: int,
    reviews_per_month: float,
    calculated_host_listings_count: int,
    availability_365: int,
    number_of_reviews_ltm: int,
    rating: float,
    bedrooms: float,
    beds: int,
    baths: int,
    room_type_Private_room: int,
    room_type_Shared_room: int,
    room_type_Hotel_room: int,
    neighbourhood_group_Brooklyn: int,
    neighbourhood_group_Manhattan: int,
    neighbourhood_group_Queens: int,
    neighbourhood_group_Staten_Island: int
):
    
    input_data = np.array([[ 
        latitude, longitude, minimum_nights, number_of_reviews,
        reviews_per_month, calculated_host_listings_count,
        availability_365, number_of_reviews_ltm, rating,
        bedrooms, beds, baths,
        room_type_Private_room,
        room_type_Shared_room,
        room_type_Hotel_room,
        neighbourhood_group_Brooklyn,
        neighbourhood_group_Manhattan,
        neighbourhood_group_Queens,
        neighbourhood_group_Staten_Island
    ]])

    prediction = model.predict(input_data)

    # reverse log transform
    prediction = np.expm1(prediction)

    return {"predicted_price": float(prediction[0])}

