import pymongo
import streamlit as st

# Connect to MongoDB Atlas
#client = pymongo.MongoClient("mongodb+srv://sachintest:JZHyLgBIIFngFHcP@cluster0.wmki6co.mongodb.net/")

try:
    # Attempt to establish a connection
    client = pymongo.MongoClient("mongodb+srv://sachintest:JZHyLgBIIFngFHcP@cluster0.wmki6co.mongodb.net/")
    st.write("MongoDB connection established successfully.")
    # Access a specific database
    db = client["testdb"]
    # Access a specific collection
    collection = db["testcollection"]

    cursor = collection.find({"name":"sachin"})
    data = list(cursor)
    for document in data:
        st.write(document)
except pymongo.errors.ConnectionFailure as e:
    # Handle connection failure
    st.error(f"MongoDB connection error: {e}")

