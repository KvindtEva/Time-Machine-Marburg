import pandas as pd
import requests
import re
import numpy as np
import os


def download_image(url, save_path):
    try:
        # Check if the image already exists
        if os.path.exists(save_path):
            return ('Exists', 0)
        
        response = requests.get(url)
        
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            return ('Downloaded', response.status_code)
        else:
            return ('Failed', response.status_code)
    except Exception as e:
        print(f"An error occurred: {e}")
        return ('Error', response.status_code)


def create_folder(folder_name):
    # Check if the folder exists
    if not os.path.exists(folder_name):
        # Create the folder if it doesn't exist
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created.")
    else:
        print(f"Folder '{folder_name}' already exists.")


def filename_to_object(df, file_name):

    object_index, file_index = None, None
    file_type, id_persistent, id_link = file_name.split('-')

    if file_type == 'scn':
        column = 'microfiche_links'
    else:
        column = 'image_links'

    # Search for an object by link if id_persistent is 'NO_ID_PERSISTENT'
    if id_persistent == 'NO_ID_PERSISTENT':
        for j, links in enumerate(df[df.id_persistent == 'NO_ID_PERSISTENT'][column]):
            for link in links:
                if re.findall(r'.*/([^/]*)$', link)[0] == id_link:
                    object_index = df[df.id_persistent == 'NO_ID_PERSISTENT'].index[0]
                    file_index = j
                    return object_index, column, file_index

    # Search for an object by id_persistent
    for i, id in enumerate(df.id_persistent):        
        if id == 'NO_ID_PERSISTENT':
            continue
        if re.findall(r'.*/([^/]*)$', id)[0] == id_persistent:
            # Search for file_index among links of object
            for j, link in enumerate(df.iloc[i][column]):
                if re.findall(r'.*/([^/]*)$', df.iloc[i][column][j])[0] == id_link:
                    object_index, file_index = i, j
                    return object_index, column, file_index
    
    return None, None, None

def link_to_filename(id_persistent, link, file_type):

    if id_persistent != 'NO_ID_PERSISTENT':
        id_persistent = re.findall(r'.*/([^/]*)$', id_persistent)[0]
    
    file_name = file_type + '-' + id_persistent + '-' + re.findall(r'.*/([^/]*)$', link)[0]
    return file_name

def object_to_filenames(df, id):

    id_persistent = df.iloc[id].id_persistent

    file_names = {'Images': [], 'Scans': []}
    
    for link in df.iloc[id].image_links:
        file_name = link_to_filename(id_persistent, link, 'img')
        file_names['Images'].append(file_name)
    for link in df.iloc[id].microfiche_links:
        file_name = link_to_filename(id_persistent, link, 'scn')
        file_names['Scans'].append(file_name)
    
    return file_names
        