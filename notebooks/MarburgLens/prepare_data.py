# prepare_data.py

import os
import random
from pathlib import Path
from shutil import copy2
from torchvision import transforms
from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder

# ----------------------
# CONFIGURATION
# ----------------------
DATA_DIR = Path(r'C:\Users\sOrOush\SoroushProjects\15_MarburgLens\data\TMM')  # original unstructured data
OUTPUT_DIR = Path('processed_data')    # structured into train/val/test
TRAIN_RATIO = 0.7
VAL_RATIO = 0.2
TEST_RATIO = 0.1
SEED = 42

# ----------------------
# STEP 1: Split Data
# ----------------------
def split_dataset():
    random.seed(SEED)

    classes = [d.name for d in DATA_DIR.iterdir() if d.is_dir()]
    print(f"Found {len(classes)} classes: {classes}")

    for cls in classes:
        images = list((DATA_DIR / cls).glob('*'))
        random.shuffle(images)

        n_total = len(images)
        n_train = int(n_total * TRAIN_RATIO)
        n_val = int(n_total * VAL_RATIO)

        splits = {
            'train': images[:n_train],
            'val': images[n_train:n_train + n_val],
            'test': images[n_train + n_val:]
        }

        for split, imgs in splits.items():
            split_dir = OUTPUT_DIR / split / cls
            split_dir.mkdir(parents=True, exist_ok=True)
            for img in imgs:
                copy2(img, split_dir)

    print(f"Data split and copied to {OUTPUT_DIR}/!")

# ----------------------
# STEP 2: Define Transforms
# ----------------------

def get_transforms():
    train_transform = transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(15),
        transforms.ColorJitter(brightness=0.3, contrast=0.3, saturation=0.3, hue=0.05),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225]),
    ])

    val_transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225]),
    ])

    return train_transform, val_transform

# ----------------------
# STEP 3: Create Datasets and Loaders
# ----------------------

def create_dataloaders(batch_size=32):
    train_transform, val_transform = get_transforms()

    train_dataset = ImageFolder(root=OUTPUT_DIR / 'train', transform=train_transform)
    val_dataset = ImageFolder(root=OUTPUT_DIR / 'val', transform=val_transform)
    test_dataset = ImageFolder(root=OUTPUT_DIR / 'test', transform=val_transform)

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=4)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=4)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, num_workers=4)

    print(f"Datasets ready: {len(train_dataset)} train, {len(val_dataset)} val, {len(test_dataset)} test samples.")
    return train_loader, val_loader, test_loader

# ----------------------
# STEP 4: Check Folder Stats
# ----------------------

def print_folder_stats(base_dir=DATA_DIR):
    print(f"\nFolder stats for {base_dir}:")
    for cls_dir in sorted(base_dir.glob('*')):
        if cls_dir.is_dir():
            num_images = len(list(cls_dir.glob('*')))
            print(f"- {cls_dir.name}: {num_images} images")

# ----------------------
# MAIN
# ----------------------
if __name__ == '__main__':
    #split_dataset()
    print_folder_stats(OUTPUT_DIR / 'train')
    print_folder_stats(OUTPUT_DIR / 'val')
    print_folder_stats(OUTPUT_DIR / 'test')
    # After splitting, you can call create_dataloaders() inside your train.py!
