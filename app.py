import streamlit as st
import os
import torch
from torchvision.transforms import transforms
from PIL import Image
from pathlib import Path
import torch.nn.functional as F
from Xray.constant.TrainingPipeline import *
from Xray.entity.artifact_entity import ModelTrainerArtifact


# this is for saving images and prediction
def save_image(uploaded_file):
    if uploaded_file is not None:
        os.makedirs("images", exist_ok=True)
        save_path = os.path.join("images", "input.jpeg")
        with open(save_path, "wb") as f:
            f.write(uploaded_file.read())
        st.success(f"Image saved to {save_path}")
        


        model = torch.load('model/model.pt', weights_only=False)


        trans = transforms.Compose([
            transforms.RandomHorizontalFlip(),
            transforms.Resize(224),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            ])
        

        image = Image.open(Path('images/input.jpeg'))

        input = trans(image)

        input = input.unsqueeze(0)  # adds batch dimension: [1, 3, 224, 224]


        output = model(input)
        
        prediction= F.softmax(output, dim=1)
        
        prediction = int(torch.max(output.data, 1)[1].numpy()[0])

        
        st.image(image, caption="This is a sample image", use_column_width=True)
        
        st.markdown(f"""
        <h3 style='color: green; font-weight: bold;'>
        Prediction: {PREDICTION_LABEL[prediction]}
        </h3>
        """, unsafe_allow_html=True)




if __name__ == "__main__":
    st.title("Plant Seedling Classification")
    st.write("Upload an image of a plant seedling to classify it.")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    save_image(uploaded_file)


    