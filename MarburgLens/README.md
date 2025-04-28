# Marburg Lens: University Building Classifier

## Overview

Marburg Lens is a machine learning project that automatically classifies photographs of university buildings in Marburg, Germany.

## Project Structure

```
MarburgLens/
├── processed_data/         # Train, validation, and test split images
├── results/
│   └── images/             # Classified results with folders per class
├── scripts/
│   ├── prepare_data.py     # Data splitting and augmentation setup
│   ├── 01_prep_data.ipynb  # Jupyter version of prepare_data
│   ├── 02_train.ipynb      # Model training notebook
│   ├── 03_test_model.ipynb # Single image prediction notebook
│   ├── TMM_images_classification.py # Batch prediction and organization
│   ├── evaluate_testset.py # Evaluation script
│   └── evaluate_notebook.ipynb # Jupyter version of evaluation
├── models/
│   └── resnet50_marburglens.pth # Trained model file
├── README.md
```

## Methods

- **Model**: ResNet50, pretrained on ImageNet, fine-tuned on the custom dataset.
- **Loss Function**: CrossEntropyLoss.
- **Optimizer**: Adam.
- **Learning Rate**: 1e-4.
- **Batch Size**: 32.
- **Data Augmentation**: Applied during training with random resized crops, flips, rotations, color jittering. {get_transforms()}
- **Thresholding**: Images with prediction confidence below 0.3 are moved to an 'unknown' folder.

## Dataset Details

- 29 building classes.
- Approximately 1752 total images.
- Split: 70% training, 20% validation, 10% testing.
- Data collected manually with similar camera conditions, leading to high intra-dataset homogeneity.

## Evaluation Results

- **Final Test Accuracy**: 97.56%
- **Final Test Loss**: 0.0788

Most classes achieve over 95% precision and recall. Slight performance drops occur in classes with very few test images.

## Scripts

### 1. prepare_data.py / 01_prep_data.ipynb
- Splits the dataset.
- Applies transformations.

### 2. 02_train.ipynb
- Fine-tunes ResNet50.
- Saves the trained model.

### 3. evaluate_testset.py / evaluate_notebook.ipynb
- Evaluates the model on the test set.
- Outputs confusion matrix, normalized confusion matrix, and per-class accuracy.

### 4. 03_test_model.ipynb
- Loads a single image and predicts its building class.

### 5. TMM_images_classification.py
- Loads a batch of images.
- Predicts and sorts images into class folders based on a confidence threshold.
- Images with low confidence are placed into an 'unknown' folder.

## Notes on Performance

High test accuracy is partly due to:
- Consistent image conditions (same device, lighting, time).
- Limited variance between training and test distributions.

## Requirements

- Python 3.9+
- PyTorch
- TorchVision
- scikit-learn
- Seaborn
- PIL (Pillow)
- Matplotlib

## License

Internal academic project, not for commercial distribution.

