import streamlit as st  
import pandas as pd  
import os  
from io import BytesIO  

# App setup  
st.set_page_config(page_title="🚀Growth Mindset Challenge🎨🔥", layout='wide')  

# Sidebar setup  
st.sidebar.title("Shama Naz")  
resume_link = "https://milestone-5-nine.vercel.app/"  

# Define Gradient Pulse Button CSS  
button_style = """  
    <style>  
        @keyframes pulse {  
            0% { box-shadow: 0 0 10px rgba(255, 87, 34, 0.7); }  
            50% { box-shadow: 0 0 20px rgba(255, 87, 34, 1); }  
            100% { box-shadow: 0 0 10px rgba(255, 87, 34, 0.7); }  
        }  
        .pulse-button {  
            display: block;  
            width: 100%;  
            text-align: center;  
            background: linear-gradient(45deg, #FF5722, #FFC107);  
            color: white;  
            font-size: 18px;  
            font-weight: bold;  
            padding: 12px;  
            margin: 10px 0;  
            border-radius: 8px;  
            text-decoration: none;  
            transition: all 0.3s ease-in-out;  
            animation: pulse 1.5s infinite;  
        }  
    </style>  
"""  
# Inject CSS into the app  
st.sidebar.markdown(button_style, unsafe_allow_html=True)  

# Create the pulse effect button  
st.sidebar.markdown(f'<a href="{resume_link}" target="_blank" class="pulse-button">📝 View Resume</a>', unsafe_allow_html=True)  

# Main content  
st.title("🚀 Growth Mindset Challenge")  
st.write("🛠 Transform your files between CSV & Excel formats with built-in data cleaning & visualization!")  

# File uploader  
uploaded_file = st.file_uploader("📂 Upload your CSV or Excel file", type=["csv", "xlsx"])  

if uploaded_file is not None:  
    file_extension = os.path.splitext(uploaded_file.name)[-1].lower()  

    # Read file  
    if file_extension == ".csv":  
        df = pd.read_csv(uploaded_file)  
    elif file_extension == ".xlsx":  
        df = pd.read_excel(uploaded_file, engine="openpyxl")  
    else:  
        st.error("❌ Unsupported file format!")  
        st.stop()  

    # Display Data  
    st.subheader("📊 Preview of Uploaded File:")  
    st.dataframe(df)  

    # Convert file format  
    st.subheader("🔄 Convert File Format")  
    if file_extension == ".csv":  
        converted_file = BytesIO()  
        df.to_excel(converted_file, index=False, engine="openpyxl")  
        converted_file.seek(0)  
        st.download_button("⬇️ Download as Excel", data=converted_file, file_name="converted_file.xlsx")  

    elif file_extension == ".xlsx":  
        converted_file = BytesIO()  
        df.to_csv(converted_file, index=False)  
        converted_file.seek(0)  
        st.download_button("⬇️ Download as CSV", data=converted_file, file_name="converted_file.csv")  

    # Data Cleaning  
    st.subheader("🧹 Data Cleaning")  
    if st.button("🗑 Remove Duplicates"):  
        df = df.drop_duplicates()  
        st.dataframe(df)  

    if st.button("🚀 Fill Missing Values"):  
        df = df.fillna("N/A")  
        st.dataframe(df)  

    # Summary Stats  
    st.subheader("📈 Data Statistics")  
    st.write(df.describe())  
