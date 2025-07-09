import tensorflow as tf
from tensorflow.keras.models import load_model
import streamlit as st
import numpy as np
import base64

# Page config normal layout (not wide)
st.set_page_config(page_title="🍓 Fruit & Veggie Classifier", page_icon="🍉", layout="centered")

# Load background image as base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

image_path = 'c:/Users/DELL/Downloads/mixed fruit.jpg'  # Your local image path
img_base64 = get_base64_of_bin_file(image_path)

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Comfortaa:wght@500;700&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Comfortaa', cursive;
        margin: 0;
        padding: 0;
        height: 100vh;  /* Full viewport height */
        overflow: hidden; /* Disable page scroll */
    }}

    body::before {{
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: url("data:image/jpg;base64,{img_base64}") no-repeat center center fixed;
        background-size: cover;
        filter: blur(8px);
        opacity: 1;
        z-index: -1;
    }}

    .stApp {{
        background: rgba(135, 206, 235, 0.85);
        backdrop-filter: blur(6px);
        border-radius: 20px;
        padding: 1rem 1.5rem 1.5rem 1.5rem;  /* less top padding */
        margin: 0 auto;  /* Remove vertical margin */
        max-width: 750px;
        height: 100vh;  /* full viewport height */
        overflow-y: auto; /* allow scroll inside container if needed */
        box-shadow: 0 10px 40px rgba(0,0,0,0.3);
    }}

    h1 {{
        text-align: center;
        font-size: 2.4rem;
        font-weight: 700;
        color: #ffffff;
        text-shadow: 2px 2px 6px #00000088;
        margin: 0 0 0.8rem 0;  /* zero top margin, smaller bottom */
        line-height: 1.1;
        padding-top: 0.4rem;
    }}

    .stFileUploader, .stButton, .stTextInput {{
        background-color: #ffffffdd !important;
        color: #000 !important;
        border-radius: 10px !important;
        font-weight: bold;
        margin-bottom: 0.8rem;
    }}

    .stImage img {{
        border-radius: 15px;
        border: 4px solid #fff;
        box-shadow: 0 0 20px rgba(0,0,0,0.4);
        margin-top: 0.8rem;
        max-height: 250px;
        object-fit: contain;
    }}

    .prediction-box {{
        background-color: #ffffff33;
        padding: 1.3rem;
        border-radius: 20px;
        margin-top: 1rem;
        text-align: center;
        box-shadow: 0 4px 25px rgba(0,0,0,0.4);
    }}

   .prediction-box h3 {{
    font-size: 2.8rem;           /* bigger font size */
    font-weight: 800;
    color: #064e03;              /* rich dark green */
    margin-bottom: 0.4rem;
    line-height: 1.1;
    text-shadow: none;           /* remove text shadow for clarity */
   }}

   .confidence {{
    color: #004b8d;              /* deep dark blue */
    font-size: 1.8rem;           /* bigger font */
    font-weight: 700;
    text-shadow: none;           /* remove text shadow */
    }}

    /* Footer fixed at bottom inside container */
    footer {{
        position: sticky;
        bottom: 0;
        text-align: center;
        padding: 0.7rem 0;
        font-size: 1.6rem;
        color: blue;
        font-weight: bold;
        background: rgba(255, 255, 255, 0.2);
        border-top: 1px solid #ccc;
        margin-top: 1rem;
        border-radius: 0 0 20px 20px;
        backdrop-filter: blur(6px);
    }}

    header {{visibility: hidden;}}
    </style>
""", unsafe_allow_html=True)


# Title
st.markdown("<h1>🍇 Fruit & Veggie Classifier</h1>", unsafe_allow_html=True)

# Load model
model = load_model(r'C:\Users\DELL\Desktop\python\image_classification\image_class_model.keras')

data_cat = ['apple', 'banana', 'beetroot', 'bell pepper', 'cabbage', 'capsicum',
 'carrot', 'cauliflower', 'chilli pepper', 'corn', 'cucumber', 'eggplant',
 'garlic', 'ginger', 'grapes', 'jalepeno', 'kiwi', 'lemon', 'lettuce',
 'mango', 'onion', 'orange', 'paprika', 'pear', 'peas', 'pineapple',
 'pomegranate', 'potato', 'raddish', 'soy beans', 'spinach', 'sweetcorn',
 'sweetpotato', 'tomato', 'turnip', 'watermelon']

uploaded_file = st.file_uploader("📤 Upload a fruit or vegetable image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img_height, img_width = 180, 180
    image = tf.keras.utils.load_img(uploaded_file, target_size=(img_height, img_width))
    img_array = tf.keras.utils.img_to_array(image)
    img_batched = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_batched)
    score = tf.nn.softmax(predictions[0])
    predicted_label = data_cat[np.argmax(score)]
    confidence = np.max(score) * 100

    st.image(image, caption="🖼️ Uploaded Image", width=300)

    st.markdown(f"""
    <div class="prediction-box">
        <h3>🔍 Predicted: {predicted_label.title()}</h3>
        <p class="confidence">Confidence: {confidence:.2f}%</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <hr style="margin-top: 2rem; border: none; height: 1px; background-color: #ccc;" />
    <div style='text-align: center; padding: 1rem; font-size: 1.8rem; color: blue; font-weight: bold;'>
        🌱 Made with ❤️ by <strong>Bishop Roy</strong>
    </div>
""", unsafe_allow_html=True)
