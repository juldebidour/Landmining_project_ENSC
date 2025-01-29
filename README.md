# _Landmining_project_ENSC_

# Overview

This is the repository that contains the work for the AI project of our third year of engineer school.

This project focuses on detecting landmines using machine learning techniques applied to sensor data. The goal is to classify whether a detected object is a landmine or not based on features extracted from the data. The project involves data preprocessing, feature engineering, model training, and evaluation using various machine learning algorithms.

# Project structure

The project is organized into several key directories and files:

- **FirstDataset** : Contains the initial dataset used for training and testing.
  - **augmentation.ipynb**:  Jupyter notebook for data augmentation.
  - **Augmented_Mine_Dataset.csv** : CSV file containing the augmented mine dataset.
  - **augmentation2.ipynb** : Another Jupyter notebook for data augmentation.
  - **knn_random_forest.ipynb** : Jupyter notebook for training KNN and Random Forest models.
  - **landmining.ipynb** : Jupyter notebook for the main landmine detection model.
  - **info.jpg** : Image file with additional information.
  - **pyproject.toml** : Project configuration file.
  - **poetry.lock** : Lock file for dependency management.
    
- **SecondDataset** : Contains an additional dataset for further training and validation.
  
  - **FinalDatas** : Directory containing the final datasets and model results.
  - **Mine2.py** : Python script for the final model.
    
- **README.md** : This README file.
  
- **.gitignore**:  File specifying which files and directories to ignore in Git.

# Dataset

The dataset consists of sensor data collected from landmine detection equipment. It includes features such as sensor readings _(voltage)_, geographical coordinates _(position)_, and labels indicating whether a landmine is present or not. 
Each dataset is split into training and testing sets for model development and evaluation.

The first dataset used can be found here : [https://universe.roboflow.com/northumbria/landmines-detection-dataset/dataset/4](https://www.kaggle.com/datasets/parsapzadeh/land-mines).

The second dataset used for yolo can be found here : [https://universe.roboflow.com/northumbria/landmines-detection-dataset/dataset/4](https://universe.roboflow.com/northumbria/landmines-detection-dataset/dataset/4).

# Methodology

_--> Data Preprocessing : Cleaning and normalizing the sensor data to prepare it for analysis.

--> Feature Engineering : Extracting relevant features and reducing dimensionality to improve model performance.

--> Model Training : Training machine learning models, including Random Forest, Support Vector Machines (SVM), and Neural Networks.
  
--> Evaluation : Assessing model performance using metrics such as accuracy, precision, recall, and ROC-AUC._

# Results

The project achieved promising results in landmine detection, with the XG Boost performing particularly well. Detailed evaluation metrics and visualizations, such as ROC curves and confusion matrices, are provided in the Results/ directory.
