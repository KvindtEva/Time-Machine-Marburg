# Time-Machine-Marburg 🏛️
"Time Machine Marburg" is multimodal historical data structuring project that aims to analyze and organize a complex dataset from the photo archive of Marburg, consisting of historical images, objects, landscapes, maps, portraits, texts and more. Particularly, it involves Natural Language Processing, Computer Vision, and Web Metadata Extraction, transforming a raw archive into a structured dataset as well as separating university-related buildings images for further use by another team, which will create historical storytelling to the anniversary of the university.

**Authors:** [Eva Kvindt](www.linkedin.com/in/eva-kvindt), Hamidreza Khoshvaghti, Soroush Daftarian  
**More information:** [Project Documentation](https://zenodo.org/records/15427716?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6ImJiN2YyM2E2LTNmMmEtNDg3NS1iNjliLTFhYTZhN2VjYmM1YSIsImRhdGEiOnt9LCJyYW5kb20iOiI4NzBkOTdiYTQ3ZTFkMDU0OTkwY2M1ZmQ0NjJkNjAxZiJ9.1KtO70OIetgZX_Q2k7_fouTeI-R-efhNVc-JrhMEaiKBoL5rKALWmA_u8aNQEM29pEchoHCadWhKkOzuW3lA2A)

![cover](https://github.com/KvindtEva/Time-Machine-Marburg/blob/main/config/pics/git_overview_pic.png?raw=true)




## 🛠️ Reproducing Project Workflow
**Run the complete data processing pipeline**
Follow our notebooks and code to reproduce the full workflow—from downloading raw data and cleaning labels to clustering images and generating structured outputs. Ideal for developers, students, or researchers who want to replicate, extend, or audit the methodology.

### 🖼 Computer Vision

#### Clustering
#### Classification

Run the model


### 📝 Natural Language Processing

### 🌐 Metadata Scrapping



## 📦 Access the Ready-Made Data
**Use the delievered dataset directly**
If you're only interested in using the cleaned and classified data (e.g., for storytelling, visualization, or research), you can explore the final outputs without running the full pipeline.



## Repository Structure

- **datasets_benchmark/** - Folder with benchmark for clustering testing. Inside are folders for different physical objects (e.g. Elisabethkirche or Kliniken) 
- **datasets/** - Folder with all datasets versions, which are described in related README.md file inside folder. dataset_CLEANED_ver2.csv should be used for all further work (objects are structured, missing values are filled)
- **emails/** - Some copies of Prof.Bell's and  Max Grüntgens' emails are here, so they are available for all of us
- **images/** - Folder with image files 
- **config/** - Folder for functions and illustrations in notebooks
    - **fucntions/columns_converter.py** - function for converting lists of strings into lists of links (are used inside Notebooks)
    - **fucntions/img_downloader.py** - functions for donwloading images (are used inside Notebooks)


- **dataset_cleaning.ipynb** - (don't touch it) Code preproccessing of original dataset (datasets/dataset_ORIG.csv)
- **image_downloading.ipynb** - Code for downloading images from dataset_CLEAN.csv on your computer. Option 2 is has to be used
- **baseline_image_model.ipynb** - Code for trying out different image models for image clustering
- **ground_truth.ipynb** - Code for creating ground truth DataFrame from files on
- **EDA.ipynb** - Code for exploratory data analysis (EDA) of dataset_CLEAN.csv
- **dataset_MVP.ipynb** - Creating an MVP dataset
- **obtaining_building_list.ipynb** - Code for extracting uni building info from Wiki and converting it to json
- **taxonomy_fisrt_clustering.ipynb** - Code for extracting ChatGPT's taxonomy and converting it into json; manual and code choice of outdoor cluster 
- **DataSetEntityClustering.ipynb** - Code for textual analysis in order to try clusterisation on buildings labels
- **TMM_baseline_image_model_latest.ipynb.ipynb** - Code for clustering images (30K) into 100 clusters (Hamid)
- **VectorizingAndPreparingBuildingsDictionarz.ipynb** - 
- **VectorizingAndPreparingTextualClusters.ipynb** - 
- **compress_rotate.ipynb** -  

- **imagenet-classes.txt** - lables for RESNET

## 1 Data cleaning
First step was to prepare original dataset (DATASETS_DONT_TOUCH/dataset_ORIG.csv) for furhter work, because it was dirty with zero entries, wrong separators etc. Detailed description of cleaning process is described in Dataset_Cleaning.ipynb file  
So dataset_CLEAN.csv (DATASETS_DONT_TOUCH/dataset_CLEAN.csv) is ready for further analysis, clusterisation, classification and so on

## 2 Textual analysis
In file **DataSetEntityClustering.ipynb** textual analysis and furhter clusterisation is performed.

## 3 Clustering

## 4 Classification
