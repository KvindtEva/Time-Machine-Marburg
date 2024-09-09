# Time-Machine-Marburg

## Description of repository

- **DATASETS_GROUND_TRUTH** - Folder with preparation for ground truth dataset for testing
- **DATASETS_DONT_TOUCH** - Folder with all datasets versions, which are described in related README.md file inside folder. dataset_CLEANED.csv should be used for all further work
- **email_by_Prof_Bell** - Some copies of Prof.Bell's emails are here, so they are available for all of us
- **Dataset_Cleaning.ipynb** - (don't touch it) Code preproccessing steps of original dataset (DATASETS_DONT_TOUCH/dataset_ORIG.csv)
- **Image_Downloading.ipynb** - Code for downloading images from dataset_CLEAN.csv on your computer
- **DataSetEntityClustering.ipynb** - Code for textual analysis in order to try clusterisation on buildings labels

## 1 Data cleaning
First step was to prepare original dataset (DATASETS_DONT_TOUCH/dataset_ORIG.csv) for furhter work, because it was dirty with zero entries, wrong separators etc. Detailed description of cleaning process is described in Dataset_Cleaning.ipynb file  
So dataset_CLEAN.csv (DATASETS_DONT_TOUCH/dataset_CLEAN.csv) is ready for further analysis, clusterisation, classification and so on

## 2 Textual analysis
In file **DataSetEntityClustering.ipynb** textual analysis and furhter clusterisation is performed.
