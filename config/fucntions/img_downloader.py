import pandas as pd
import requests
import re
import numpy as np
import os


def download_image(url: str, save_path: str) -> str:

    """
    Download image to folder from given link

    Parameters:
    url (str): Link to the image
    save_path (str): Path to save the image

    Returns:
    str: Status of the download
    """

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


def create_folder(folder_name: str) -> str:
    
    """
    Create folder with given name

    Parameters:
    folder_name (str): Name of the folder

    Returns:
    str: Status of the folder creation
    """

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        return f"Folder '{folder_name}' created."
    else:
        return f"Folder '{folder_name}' already exists."


def filename_to_objects(df_mvp: pd.DataFrame, file_name: str) -> list:

    """
    Return a list of indexes of objects in df_CLEAN, which are related
    to the given file name (Version 2)

    Parameters:
    df_mvp (pd.DataFrame): Dataframe with the metadata
    file_name (str): Name of the file in folder

    Returns:
    list: List of indexes of objects in df_CLEAN
    """

    return [int(idx) for idx in df_mvp[df_mvp.file_name == file_name]['id_objects'].iloc[0]]

    

                ### VERSION 1 ###
    # object_index, file_index = None, None
    # file_type, id_persistent, id_link = file_name.split('-')

    # if file_type == 'scn':
    #     column = 'microfiche_links'
    # else:
    #     column = 'image_links'

    # # Search for an object by link if id_persistent is 'NO_ID_PERSISTENT'
    # if id_persistent == 'NO_ID_PERSISTENT':
    #     for j, links in enumerate(df[df.id_persistent == 'NO_ID_PERSISTENT'][column]):
    #         for link in links:
    #             if re.findall(r'.*/([^/]*)$', link)[0] == id_link:
    #                 object_index = df[df.id_persistent == 'NO_ID_PERSISTENT'].index[0]
    #                 file_index = j
    #                 return object_index, column, file_index

    # # Search for an object by id_persistent
    # for i, id in enumerate(df.id_persistent):        
    #     if id == 'NO_ID_PERSISTENT':
    #         continue
    #     if re.findall(r'.*/([^/]*)$', id)[0] == id_persistent:
    #         # Search for file_index among links of object
    #         for j, link in enumerate(df.iloc[i][column]):
    #             if re.findall(r'.*/([^/]*)$', df.iloc[i][column][j])[0] == id_link:
    #                 object_index, file_index = i, j
    #                 return object_index, column, file_index
    
    # return None, None, None

def filename_to_link(file_name: str) -> str:
    """
    Return a link, realted to this file name (Version 2)
    
    Parameters:
    file_name (str): Name of the file in folder

    Returns:
    str: Link to the image
    """
    return 'http://www.bildindex.de/bilder/d/'+file_name.split('-')[1]


def link_to_filename(id_persistent: str, link: str, file_type: str) -> str:

    """
    Return a filename in folder, which relates to the given link to download

    Parameters:
    id_persistent (str): Persistent ID of the object
    link (str): Link to the image
    file_type (str): Type of the file (img or scn)

    Returns:
    str: Name of the file
    """

    # if id_persistent != 'NO_ID_PERSISTENT':
    #     id_persistent = re.findall(r'.*/([^/]*)$', id_persistent)[0]
    
    # file_name = file_type + '-' + id_persistent + '-' + re.findall(r'.*/([^/]*)$', link)[0]
    # return file_name

def object_to_filenames(df: pd.DataFrame, id_object: int)  -> dict:

    """
    Return a dictionary with filenames in folder, which relates to the given object to download,
    sorted in Images and Scans

    Parameters:
    df (pd.DataFrame): Dataframe with the metadata
    id (int): Index of the object in the dataframe

    Returns:
    dict: Dictionary with filenames (related Images and Scans)
    """

    id_persistent = df.iloc[id_object].id_persistent

    file_names = {'Images': [], 'Scans': []}

    for link in df.iloc[id_object].image_links:
        file_name = 'img' + '-' + re.findall(r'.*/([^/]*)$', link)[0]
        file_names['Images'].append(file_name)
    for link in df.iloc[id_object].microfiche_links:
        file_name = 'scn' + '-' + re.findall(r'.*/([^/]*)$', link)[0]
        file_names['Scans'].append(file_name)

    return file_names

        ### VERSION 1 ###
    # id_persistent = df.iloc[id].id_persistent

    # file_names = {'Images': [], 'Scans': []}
    
    # for link in df.iloc[id].image_links:
    #     file_name = link_to_filename(id_persistent, link, 'img')
    #     file_names['Images'].append(file_name)
    # for link in df.iloc[id].microfiche_links:
    #     file_name = link_to_filename(id_persistent, link, 'scn')
    #     file_names['Scans'].append(file_name)
    
    # return file_names
        