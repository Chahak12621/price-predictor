from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="Airbnb Dynamic Pricing API")

# Load your trained model
model = joblib.load("price_model.pkl")

# Define input schema
class PriceInput(BaseModel):
    latitude: float
    longitude: float
    minimum_nights: int
    number_of_reviews: int
    reviews_per_month: float
    calculated_host_listings_count: int
    availability_365: int
    number_of_reviews_ltm: int
    rating: float
    bedrooms: float
    beds: int
    baths: float
    room_type_Private_room: int
    room_type_Shared_room: int
    room_type_Hotel_room: int
    neighbourhood_group_Brooklyn: int
    neighbourhood_group_Manhattan: int
    neighbourhood_group_Queens: int
    neighbourhood_group_Staten_Island: int

@app.get("/")
def home():
    return {"message": "Dynamic Pricing API is running"}

@app.post("/predict")
def predict_price(data: PriceInput):
    # Convert input to array
    input_data = np.array([[
        data.latitude, data.longitude, data.minimum_nights,
        data.number_of_reviews, data.reviews_per_month,
        data.calculated_host_listings_count, data.availability_365,
        data.number_of_reviews_ltm, data.rating, data.bedrooms,
        data.beds, data.baths,
        data.room_type_Private_room, data.room_type_Shared_room, data.room_type_Hotel_room,
        data.neighbourhood_group_Brooklyn, data.neighbourhood_group_Manhattan,
        data.neighbourhood_group_Queens, data.neighbourhood_group_Staten_Island
    ]])

    prediction = model.predict(input_data)
    return {"predicted_price": float(prediction[0])}