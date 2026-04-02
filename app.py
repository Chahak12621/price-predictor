
import streamlit as st
import requests

st.title("Airbnb Dynamic Pricing")

st.write("Enter details to predict price")

# INPUTS
latitude = st.number_input("Latitude", value=40.7128)
longitude = st.number_input("Longitude", value=-74.0060)
minimum_nights = st.number_input("Minimum Nights", value=2)
number_of_reviews = st.number_input("Number of Reviews", value=50)
reviews_per_month = st.number_input("Reviews per Month", value=1.5)
calculated_host_listings_count = st.number_input("Host Listings Count", value=2)
availability_365 = st.number_input("Availability", value=100)
number_of_reviews_ltm = st.number_input("Reviews last 12 months", value=10)
rating = st.number_input("Rating", value=4.5)
bedrooms = st.number_input("Bedrooms", value=2)
beds = st.number_input("Beds", value=2)
baths = st.number_input("Baths", value=1)

# SIMPLE SELECTIONS
room_type = st.selectbox("Room Type", ["Entire home/apt", "Private room", "Shared room", "Hotel room"])
location = st.selectbox("Location", ["Manhattan", "Brooklyn", "Queens", "Bronx", "Staten Island"])

# ENCODING LOGIC
room_private = 1 if room_type == "Private room" else 0
room_shared = 1 if room_type == "Shared room" else 0
room_hotel = 1 if room_type == "Hotel room" else 0

brooklyn = 1 if location == "Brooklyn" else 0
manhattan = 1 if location == "Manhattan" else 0
queens = 1 if location == "Queens" else 0
staten = 1 if location == "Staten Island" else 0

# BUTTON
if st.button("Predict Price"):

    data = {
        "latitude": latitude,
        "longitude": longitude,
        "minimum_nights": minimum_nights,
        "number_of_reviews": number_of_reviews,
        "reviews_per_month": reviews_per_month,
        "calculated_host_listings_count": calculated_host_listings_count,
        "availability_365": availability_365,
        "number_of_reviews_ltm": number_of_reviews_ltm,
        "rating": rating,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "room_type_Private_room": room_private,
        "room_type_Shared_room": room_shared,
        "room_type_Hotel_room": room_hotel,
        "neighbourhood_group_Brooklyn": brooklyn,
        "neighbourhood_group_Manhattan": manhattan,
        "neighbourhood_group_Queens": queens,
        "neighbourhood_group_Staten_Island": staten
    }

    response = requests.post("https://price-predictor-68m2.onrender.com/predict", json=data)

    if response.status_code == 200:
        result = response.json()
        if "predicted_price" in result:
            st.success(f"💰 Predicted Price: ${result['predicted_price']:.2f}")
        else:
            st.error(f"API returned unexpected JSON: {result}")
    else:
        st.error(f"API Error! Status code: {response.status_code}, Response: {response.text}")
