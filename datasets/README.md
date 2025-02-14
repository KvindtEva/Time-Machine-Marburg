# Repository description

## Dataset for the work
- `dataset_CLEAN_ver2.csv` - Cleaned dataset, which **should be used for further analysis, classification, clusterisation etc.**
- `dataset_benchmark.csv` - Benchmark for clusterisation (url, label)

## Original dataset and cleaning
- `dataset_ORIG.csv` - Original dataset, which Prof.Bell sent us in the beginning
- `dataset_UNICODE.txt` - Original dataset in tabular unicode format; it is necessary for the correct cleaning of the dataset
- `dataset_RIGHT_SEPARATORS.csv` - A dataset with correctly preproccesed separators, but without some rows, which were cut during preprocessing; it is necessary for the correct cleaning of the dataset
- `data_rest.xlsx` - Excel file, which was used during preprocessing
- `sample9060.txt` and `sample23104.txt` - Text file with two samples from original dataset, which were cut and paste back, because of wrong separators in the beginning
- `buildings_dict.json` - dictionary / json file with information about all uni building obtained from Wiki (area, name, id, address etc.)
- `dataset_MVP.csv` - MVP dataset with all the information about image files (link, id of related object, id of label, name of the file in repository, id of file)
- `dataset_MVP_clustered.csv` - same, but with column cluster_id added
- `dataset_labels.csv` - (part of `dataset_MVP.csv`) column: label id, textual label
- `instances_no_images.csv` - objects from `dataset_CLEAN_ver2.csv` which don't have images under their URL
- `outdoor_images.csv` - part of `dataset_MVP_clustered.csv` with outdoor images only
