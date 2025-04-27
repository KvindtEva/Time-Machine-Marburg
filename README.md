# Time-Machine-Marburg

## Description of repository


- **DELIVERY/** - Folder with the most relevant datasets for future teams. It contains all linked dataset and some additional delivered models and pictures
- **datasets_benchmark/** - Folder with benchmark for clustering testing. Inside are folders for different physical objects (e.g. Elisabethkirche or Kliniken) 
- **datasets/** - Folder with all datasets versions, which are described in related README.md file inside folder. dataset_CLEANED_ver2.csv should be used for all further work (objects are structured, missing values are filled)
- **emails/** - Some copies of Prof.Bell's and  Max Grüntgens' emails are here, so they are available for all of us
- **config/** - Folder for functions and illustrations in notebooks. Also include some errors, which arise while working (for future considering see Documentation)
    - **fucntions/columns_converter.py** - function for converting lists of strings into lists of links (are used inside Notebooks)
    - **fucntions/img_downloader.py** - functions for donwloading images (are used inside Notebooks)


- **dataset_cleaning.ipynb** - Code preproccessing of original dataset (datasets/dataset_ORIG.csv)
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

For more detailed description of our project see Documentation: LINK
