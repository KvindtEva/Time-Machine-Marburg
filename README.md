# Time-Machine-Marburg 🏛️
"Time Machine Marburg" is multimodal historical data structuring project that aims to analyze and organize a complex dataset from the photo archive of Marburg, consisting of historical images, objects, landscapes, maps, portraits, texts and more. Particularly, it involves Natural Language Processing, Computer Vision, and Web Metadata Extraction, transforming a raw archive into a structured dataset as well as separating university-related buildings images for further use by another team, which will create historical storytelling to the anniversary of the university.

**Authors:** [Eva Kvindt](www.linkedin.com/in/eva-kvindt), Hamidreza Khoshvaghti, Soroush Daftarian  
**More information:** [Project Documentation](https://zenodo.org/records/15427716?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6ImJiN2YyM2E2LTNmMmEtNDg3NS1iNjliLTFhYTZhN2VjYmM1YSIsImRhdGEiOnt9LCJyYW5kb20iOiI4NzBkOTdiYTQ3ZTFkMDU0OTkwY2M1ZmQ0NjJkNjAxZiJ9.1KtO70OIetgZX_Q2k7_fouTeI-R-efhNVc-JrhMEaiKBoL5rKALWmA_u8aNQEM29pEchoHCadWhKkOzuW3lA2A)

![cover](https://github.com/KvindtEva/Time-Machine-Marburg/blob/main/config/pics/git_overview_pic.png?raw=true)



## 🛠️ Reproducing Project Workflow
**Run the complete data processing pipeline**
Follow our notebooks and code to reproduce the full workflow—from downloading raw data and cleaning labels to clustering images and generating structured outputs. All notebooks in hierarchical order you can find in `notebooks/` folder.

## 📦 Access the Ready-Made Data
**Use the delievered dataset directly**
If you're only interested in using the cleaned and classified data (e.g., for storytelling, visualization, or research), you can explore the final outputs without running the full pipeline. All datasets and their logic described you can find in `datasets/delivery` folder.



## Repository Structure

```
Time-Machine-Marburg/
├── datasets/
│   ├── raw/                 # Original, unprocessed datasets and those created while cleaning data
│   │   ├── dataset_ORIG.csv # Original, first dataset
│   │   └── ...              
│   ├── delivery/            # Delivery datasets for further research
│   │   └── ...              
│   └── production/          # Datasets used in production and there 'time stamps'
|       ├── compressed_rotated/     # Folder with compressed and rotated images for ResNET
│       ├── dataset_CLEAN.csv
│       ├── dataset_MVP.csv
│       ├── dataset_labels.csv
│       └── ...
│
├── notebooks/               # Jupyter notebooks for data processing pipeline
│   ├── 01_dataset_cleaning.ipynb          # Initial data cleaning and preprocessing
│   ├── 02_exploratory_data_analysis.ipynb # Data exploration and analysis
│   ├── 02_image_downloading.ipynb         # Code for image downloading from links
│   ├── 03_delivery_format_creation.ipynb  # Final dataset format preparation
|   ├── 04_Dataset_Compressed_and_RotateFix.ipynb  # Compressing and rotating images for clustering and 
|   |                                        classification model
│   ├── 05_baseline_image_model.ipynb      # Experiments with image modesls
│   ├── 06_taxonomy_fisrt_clustering.ipynb # Extraxting clustering taxonomy
│   ├── 07_obtaining_building_list.ipynb   # Building information extraction from Wiki
│   ├── 08_metadata.ipynb                  # Metadata scrapping
│   └── 09_explore_textual_classification.ipynb # Exploting textual data
│
├── config/                # Configuration files and utilities (e.g. picttures, functions, graphs)
│   ├── functions/         # Some functions, used in notebooks
│   ├── pics/    
|   |   └──  clustering_visualisation/          # Visualization of clusters for each case 
|   |                                           # (Clustering in 20, 50 and 100 clusters)
│   └── ...                # Configuration files
│
├── requirements.txt        # Python dependencies (for all notebooks!)
└── imagenet-classes.txt    # ImageNet class labels for classification
```
