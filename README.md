# Time-Machine-Marburg

## Description of repository

- **datasets_benchmark/** - Folder with benchmark for clustering testing. Inside are folders for different physical objects (e.g. Elisabethkirche or Kliniken) 
- **datasets/** - Folder with all datasets versions, which are described in related README.md file inside folder. dataset_CLEANED_ver2.csv should be used for all further work (objects are structured, missing values are filled)
- **emails/** - Some copies of Prof.Bell's and  Max Grüntgens' emails are here, so they are available for all of us
- **images/** - Folder with image files 
- **config/** - Folder for functions and illustrations in notebooks
    - **columns_converter.py** - function for converting lists of strings into lists of links (are used inside Notebooks)
    - **img_downloader.py** - functions for donwloading images (are used inside Notebooks)


- **dataset_cleaning.ipynb** - (don't touch it) Code preproccessing of original dataset (datasets/dataset_ORIG.csv)
- **image_downloading.ipynb** - Code for downloading images from dataset_CLEAN.csv on your computer
- **baseline_image_model.ipynb** - Code for trying out different image models for image clustering
- **ground_truth.ipynb** - Code for creating ground truth DataFrame from files on
- **EDA.ipynb** - Code for exploratory data analysis (EDA) of dataset_CLEAN.csv 
- **DataSetEntityClustering.ipynb** - Code for textual analysis in order to try clusterisation on buildings labels

- **imagenet-classes.txt** - lables for RESNET

## 1 Data cleaning
First step was to prepare original dataset (DATASETS_DONT_TOUCH/dataset_ORIG.csv) for furhter work, because it was dirty with zero entries, wrong separators etc. Detailed description of cleaning process is described in Dataset_Cleaning.ipynb file  
So dataset_CLEAN.csv (DATASETS_DONT_TOUCH/dataset_CLEAN.csv) is ready for further analysis, clusterisation, classification and so on

## 2 Textual analysis
In file **DataSetEntityClustering.ipynb** textual analysis and furhter clusterisation is performed.
