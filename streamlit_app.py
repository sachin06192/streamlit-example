import pymongo
import streamlit as st

# Connect to MongoDB Atlas
client = pymongo.MongoClient("mongodb+srv://sachintest:JZHyLgBIIFngFHcP@cluster0.wmki6co.mongodb.net/")

# Access a specific database
db = client["Cluster0"]

# Access a specific collection
collection = db["streamlit.sample-data"]

# Example: Query data from MongoDB and display it in your Streamlit app
cursor = collection.find({"name":"Jane Doe"})
if cursor.count_documents({"name":"Jane Doe"}) == 0:
    st.write("No documents found.")
else:
    data = list(cursor)
    for document in data:
        st.write(document)

