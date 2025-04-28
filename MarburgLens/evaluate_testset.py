# evaluate_testset.py

import torch
import torch.nn as nn
from torchvision import models
from prepare_data import create_dataloaders
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
import argparse

# ----------------------
# CONFIGURATION
# ----------------------
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
MODEL_PATH = 'resnet50_marburglens.pth'  # Default model path
NUM_CLASSES = 29
BATCH_SIZE = 32

# ----------------------
# FUNCTION: Load Model
# ----------------------
def load_model(model_path):
    model = models.resnet50(weights=None)
    model.fc = nn.Linear(model.fc.in_features, NUM_CLASSES)
    model.load_state_dict(torch.load(model_path, map_location=DEVICE))
    model.to(DEVICE)
    model.eval()
    return model

# ----------------------
# FUNCTION: Evaluate on Test Set
# ----------------------
def evaluate_testset(model):
    _, _, test_loader = create_dataloaders(batch_size=BATCH_SIZE)
    criterion = nn.CrossEntropyLoss()

    running_loss = 0.0
    correct = 0
    total = 0

    all_labels = []
    all_preds = []

    with torch.no_grad():
        for inputs, labels in test_loader:
            inputs, labels = inputs.to(DEVICE), labels.to(DEVICE)
            outputs = model(inputs)
            loss = criterion(outputs, labels)

            running_loss += loss.item() * inputs.size(0)
            _, preds = torch.max(outputs, 1)

            total += labels.size(0)
            correct += preds.eq(labels).sum().item()

            all_labels.extend(labels.cpu().numpy())
            all_preds.extend(preds.cpu().numpy())

    test_loss = running_loss / total
    test_acc = 100. * correct / total

    print(f"\n🎯 Final Test Accuracy: {test_acc:.2f}% (Loss: {test_loss:.4f})\n")

    return all_labels, all_preds

# ----------------------
# FUNCTION: Plot Confusion Matrix
# ----------------------
def plot_confusion_matrix(y_true, y_pred, class_names):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(12,10))
    sns.heatmap(cm, annot=False, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.xticks(rotation=90)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.show()

# ----------------------
# MAIN
# ----------------------
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Evaluate model on test set')
    parser.add_argument('--model', type=str, default=MODEL_PATH, help='Path to the trained model')
    args = parser.parse_args()

    model = load_model(args.model)
    y_true, y_pred = evaluate_testset(model)

    # Load class names from dataset
    _, _, test_loader = create_dataloaders(batch_size=BATCH_SIZE)
    class_names = test_loader.dataset.classes

    # Print Classification Report
    print("Classification Report:\n")
    print(classification_report(y_true, y_pred, target_names=class_names, digits=3))

    # Plot Confusion Matrix
    plot_confusion_matrix(y_true, y_pred, class_names)

