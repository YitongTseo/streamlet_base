import streamlit as st
import torch
from torchvision import transforms
from PIL import Image
import urllib.request as request 
from inference.model import PneumoniaCNN

# Function to load your trained model
def load_model():
    model = PneumoniaCNN()
    model.load_state_dict(torch.load('inference/pneumonia_model.pth'))
    model.eval()
    return model


# Function to predict the image
def predict(image, model):
    # Transform the image to the format your model expects
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        # Add any other transformations your model requires
    ])
    image = transform(image)
    with torch.no_grad():
        output = model(image)
        # Convert output to desired format, e.g., class probabilities
        prediction = output[0][0].item()

    return prediction


def main():
    model = load_model()
    st.title('Pneumonia X-Ray Prediction App')

    # File uploader widget
    uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")

        if st.button('Predict'):
            prediction = predict(image, model)
            # Display the prediction
            st.write('Prediction: ', prediction, " (0.0-0.5 Healthy, 0.5-1.0 Pneumonia)")


try:
    main()
except request.URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """
        % e.reason
    )