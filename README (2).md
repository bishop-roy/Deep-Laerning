
# 🍇 Fruit & Vegetable Classifier
A Deep Learning Web App to Predict Fruits & Vegetables from Images





## Description

This project uses a Convolutional Neural Network (CNN) model built with TensorFlow to classify 36 types of fruits and vegetables. It provides a user-friendly interface using Streamlit, allowing users to upload an image and receive a prediction with confidence score.

🔄 How the Project Works
This project allows users to identify fruits and vegetables from uploaded images using a deep learning model trained with Convolutional Neural Networks (CNN). Here is the complete working process:

1. Data Collection & Preprocessing

The dataset includes 36 classes of fruits and vegetables (e.g., apple, banana, eggplant, carrot, etc.)

Images are resized to 180x180 pixels and normalized to improve model performance.

Data is split into training and validation sets.

2. Model Building & Training

A CNN model is built using TensorFlow/Keras with layers like:

Conv2D, MaxPooling2D, Dropout, Flatten, and Dense

The model is compiled using:

Loss function: categorical_crossentropy

Optimizer: adam

The model is trained over multiple epochs to learn features from images.

3. Model Saving

The trained model is saved as a .keras file using:
model.save("image_class_model.keras")

4. Streamlit Web App Development
A frontend interface is developed using Streamlit, which includes:

File uploader for user input

Image preview

Predicted class display

Confidence percentage

Stylish UI with background and rounded containers

5. Prediction Process
When a user uploads an image:

The image is resized and converted to a numpy array

The model predicts probabilities for all classes

The class with the highest probability is selected

The prediction and confidence score are displayed in the app

6. Deployment
The project is deployed on a local server using:

python -m streamlit run app.py

🧩 Example Flow
plaintext
Copy
Edit
User uploads image → Image resized → Model predicts class → Output shown on screen

📂 Included in Repository

app.py: Streamlit web app code

image_class_model.keras: Trained deep learning model

image_class_model.ipynb: Jupyter notebook with training code

README.md: Project documentation

Project_Proposal.pdf: Proposal document

Presentation.pptx: Final presentation

Flowchart.png: System workflow

demo_video.mp4: App demonstration

dataset/: (Hosted on Google Drive due to size limit)


## Demo

▶️ Watch the short demo video here: [Demo Video](https://drive.google.com/file/d/15iZ5hknfyuJNtstQqsqqb1ZU0HqE8flY/view?usp=drive_link)

## Features

- Upload fruit or vegetable image
- Predict the item name using a trained CNN
- Get confidence percentage
- Clean and styled Streamlit web interface

##  Screenshot

https://drive.google.com/file/d/1H9q25-OVXjkcyWl7NjKmJXFGcXXVh487/view?usp=drive_link
##  Dataset

The dataset includes 36 categories of fruits and vegetables with thousands of labeled images.

📁 Download the dataset from:  
[Google Drive Dataset Link](https://drive.google.com/file/d/1gYVqHA9sLvj0Ha_XXvLs5ErYMBPVt6eq/view?usp=drive_link)

## Installation

1. Clone the repository:

git clone : https://github.com/bishop-roy/Deep-Laerning


2. Install dependencies:

pip install -r requirements.txt


3. Run the app:

python -m streamlit run app.py
##  Dependencies

- Python 3.x
- TensorFlow
- Streamlit
- NumPy
- Pillow

##  Dependencies

- Python 3.x
- TensorFlow
- Streamlit
- NumPy
- Pillow

## Contributors (Team)

- 👨‍🎓 Bishop Roy  
- 👨‍🎓 Abid Khan
##  License

This project is for academic purposes only.

## Download trained model

https://drive.google.com/file/d/19FhySo-j3deDzyhGK8BojK1b1Qncdyoj/view?usp=drive_link
## Description

This project uses a Convolutional Neural Network (CNN) model built with TensorFlow to classify 36 types of fruits and vegetables. It provides a user-friendly interface using Streamlit, allowing users to upload an image and receive a prediction with confidence score.

🔄 How the Project Works
This project allows users to identify fruits and vegetables from uploaded images using a deep learning model trained with Convolutional Neural Networks (CNN). Here is the complete working process:

1. Data Collection & Preprocessing

The dataset includes 36 classes of fruits and vegetables (e.g., apple, banana, eggplant, carrot, etc.)

Images are resized to 180x180 pixels and normalized to improve model performance.

Data is split into training and validation sets.

2. Model Building & Training

A CNN model is built using TensorFlow/Keras with layers like:

Conv2D, MaxPooling2D, Dropout, Flatten, and Dense

The model is compiled using:

Loss function: categorical_crossentropy

Optimizer: adam

The model is trained over multiple epochs to learn features from images.

3. Model Saving

The trained model is saved as a .keras file using:
model.save("image_class_model.keras")

4. Streamlit Web App Development
A frontend interface is developed using Streamlit, which includes:

File uploader for user input

Image preview

Predicted class display

Confidence percentage

Stylish UI with background and rounded containers

5. Prediction Process
When a user uploads an image:

The image is resized and converted to a numpy array

The model predicts probabilities for all classes

The class with the highest probability is selected

The prediction and confidence score are displayed in the app

6. Deployment
The project is deployed on a local server using:

python -m streamlit run app.py

🧩 Example Flow
plaintext
Copy
Edit
User uploads image → Image resized → Model predicts class → Output shown on screen

📂 Included in Repository

app.py: Streamlit web app code

image_class_model.keras: Trained deep learning model

image_class_model.ipynb: Jupyter notebook with training code

README.md: Project documentation

Project_Proposal.pdf: Proposal document

Presentation.pptx: Final presentation

Flowchart.png: System workflow

demo_video.mp4: App demonstration

dataset/: (Hosted on Google Drive due to size limit)

