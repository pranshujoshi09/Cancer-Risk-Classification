# Cervical Cancer Risk Classification

This repository contains a machine learning model to predict the risk of cervical cancer based on various health factors. The model has been trained using the `cervical.csv` dataset and is implemented using Python. The prediction model is hosted on a web application built with Streamlit.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Files in the Repository](#files)

## Project Overview

The goal of this project is to predict the risk of cervical cancer in individuals based on various factors such as age, years of smoking, history of sexually transmitted diseases (STDs), use of hormonal contraceptives, and more.

The model uses a logistic regression algorithm trained on a dataset of cervical cancer risk factors. The prediction is binary, indicating either a high or low risk of cervical cancer.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/Cervical-Cancer-Risk-Classification.git
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit application:

    ```bash
    streamlit run prediction.py
    ```

## Usage

The Streamlit application allows users to input various health parameters and obtain a prediction of cervical cancer risk.

1. Open the application by running the Streamlit command above.
2. Fill in the required fields on the web interface.
3. Click the "Predict" button to get the risk assessment.

The application will return one of the following results:

- "Low risk of cervical cancer"
- "High risk of cervical cancer"

### Demo Image

![screenshot](/img/demo.png)

## Files

- `regression.pkl`: Pre-trained machine learning model used for cervical cancer risk prediction.
- `cervical.csv`: Dataset used for training the model.
- `prediction.py`: Script to test the model using a web interface built with Streamlit.
- `training.ipynb`: Jupyter notebook containing the code for training the model (uploaded separately).
- `requirements.txt`: List of Python dependencies required to run the project.

---

Readme made with 💖 using [README Generator by Chirag Joshi](https://github.com/chiragjoshi12/readme-generator)
