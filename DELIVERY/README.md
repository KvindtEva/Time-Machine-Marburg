# Folder description

## Important notes
- Files uses (semicolon) as the separator instead of a comma.
- Encoding 'utf-8'

## Datasets

### `objects.csv`
The `objects.csv` file contains detailed information about individual objects (e.g. sculpture, book, art, building) in archive of Marburg, their identifiers, links to images and archives, and additional metadata like type of the object, location, and dating.

- **id_record** | URL to the detailed record page of the object (not unique)
- **id_persistent** | Persistent ID (linked data) for the object (unique).
- **label_id** | ID referencing a title of object from `labels.csv`
- **image_links** | List of URLs linking to images of the object.
- **archive_links** | List of URLs linking to archives where the object is referenced.
- **microfiche_links** | List of URLs to microfiche images of the object (usually scans of the image_links).
- **microfiche_archive_links** | List of URLs to microfiche versions in the archive.
- **obj_type** | Object type or category (e.g., Photography, Applied Art) in German.
- **location** | The address associated with the object.
- **dated** | Date or estimated period associated with the object.
- **location_additional** | Additional location details (if any) (e.g. purpose of the building).


### `images.csv`
The `images.csv` file contains data about images related to university buildings. Labels typically describe locations, objects, or events. Each row represents one image and includes the following fields:

- **link** - Direct URL to the image file
- **id_objects** - List of object IDs associated with the image.
- **labels** - List of title IDs assigned to the object of this image.
- **file_name** - Local filename under which the image is saved.
- **id** - Unique identifier of the image (extracted from the filename).
- **cluster** - Cluster number assigned to the image (not 100% correctness).
- **cluster_type** - Type of cluster (e.g., notype if not categorized).


### `buildings_dict.json`
The `buildings.json` file contains information about university buildings obtained from https://www.wikidata.org/wiki/Wikidata:WikiProject_Philipps-Universit%C3%A4t_Marburg . The data is organized as a nested structure:

- **First level**: Name of the region or area (e.g., "Lahntal").
- **Second level**: Street name within that region (e.g., "Biegenstraße").
- **Third level**: A list of building objects located on that street, each described with the following fields:
- - **name**: Full name of the building with the purpose and address 
- - **id_link**: Unique identifier (e.g., Q130467645).
- - **address_code**: Internal address code (e.g. B|02).
- - **address**: Official street address
- - **gebnum**: University-specific building number (e.g. 2434)

### `labels.csv`
The `labels.csv` file maps title IDs to their corresponding descriptive titles. Each row contains a unique identifier and the title text.
- **id** - Unique numeric identifier for the title.
- **label** - Descriptive text or name associated with the label

### `clusters.csv`
The `clusters.csv` file contains metadata about image clusters (obtained with our clustering in 100 clusters; for details see related Notebooks and documentation). Each cluster groups together images based on shared visual or thematic characteristics, and is described by its name, relevant keywords, and a detailed description.
- **cluster_id**	Unique identifier for the cluster (integer) in [0-99].
- **name**	Short name describing the main theme of the cluster.
- **keywords**	List of keywords capturing key visual or conceptual elements in the cluster.
- **description**	Detailed narrative description of the cluster’s content, typical features, deviations, and general style.
Note: This taxonomy for clusters is created with ChatGPT