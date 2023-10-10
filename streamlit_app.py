import pymongo
import streamlit as st

# Connect to MongoDB Atlas
client = pymongo.MongoClient("mongodb+srv://sachintest:JZHyLgBIIFngFHcP@cluster0.wmki6co.mongodb.net/")

if client.server_info():
    print("MongoDB connection established successfully.")

# Access a specific database
db = client["Cluster0"]

# Access a specific collection
collection = db["streamlit.sample-data"]

