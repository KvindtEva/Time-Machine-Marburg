# batch_classify_images.py

import os
from pathlib import Path
from shutil import copy2
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
from prepare_data import create_dataloaders

# ----------------------
# CONFIGURATION
# ----------------------
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
MODEL_PATH = 'resnet50_marburglens.pth'
INPUT_IMAGES_DIR = Path(r'C:/Users/sOrOush/SoroushProjects/00_scratchpad/images/images')
OUTPUT_DIR = Path('results2/images')
UNKNOWN_DIR = OUTPUT_DIR / 'unknown'
NUM_CLASSES = 29
CONFIDENCE_THRESHOLD = 0.70  # Adjust threshold as needed

# ----------------------
# FUNCTION: Load Model
# ----------------------

def load_model():
    model = models.resnet50(weights=None)
    model.fc = nn.Linear(model.fc.in_features, NUM_CLASSES)
    model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
    model = model.to(DEVICE)
    model.eval()
    return model

# ----------------------
# FUNCTION: Predict Single Image
# ----------------------

def predict_image(model, image_path, class_names):
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225]),
    ])

    image = Image.open(image_path).convert('RGB')
    input_tensor = transform(image).unsqueeze(0).to(DEVICE)

    with torch.no_grad():
        outputs = model(input_tensor)
        probs = torch.softmax(outputs, dim=1)
        confidence, preds = torch.max(probs, 1)

    predicted_class = class_names[preds.item()]
    return predicted_class, confidence.item()

# ----------------------
# MAIN: Classify all images and organize into folders
# ----------------------

if __name__ == '__main__':
    model = load_model()

    # Get class names from training loader
    train_loader, _, _ = create_dataloaders(batch_size=32)
    class_names = train_loader.dataset.classes

    # Create output directories
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    UNKNOWN_DIR.mkdir(parents=True, exist_ok=True)

    image_paths = list(INPUT_IMAGES_DIR.glob('*'))

    for img_path in image_paths:
        try:
            predicted_class, confidence = predict_image(model, img_path, class_names)
            if confidence < CONFIDENCE_THRESHOLD:
                # Low confidence, classify as unknown

                copy2(img_path, UNKNOWN_DIR / img_path.name)
                print(f"⚠️ {img_path.name} classified as UNKNOWN (confidence={confidence:.2f})")
            else:
                class_output_dir = OUTPUT_DIR / predicted_class
                class_output_dir.mkdir(parents=True, exist_ok=True)
                copy2(img_path, class_output_dir / img_path.name)
                print(f"✅ {img_path.name} classified as {predicted_class} (confidence={confidence:.2f})")
        except Exception as e:
            print(f"⚠️ Failed to process {img_path.name}: {e}")

    print("\n🎯 All images classified and organized!")
