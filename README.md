# Laptop Price Prediction

This repository contains a machine learning project aimed at predicting laptop prices based on various specifications. The project uses a dataset of laptop details and implements various machine learning algorithms to estimate the price of a laptop.

---

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Setup](#setup)

---

## Introduction
Laptop prices vary significantly based on specifications like brand, screen size, processor type, and RAM. This project aims to use these specifications to build a machine learning model that predicts laptop prices.

---

## Dataset

The dataset includes the following attributes:

| Attribute         | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `laptop_ID`       | Unique identifier for each laptop.                                         |
| `Company`         | The brand of the laptop (e.g., Dell, HP, Apple).                          |
| `Product`         | The model name or series of the laptop.                                    |
| `TypeName`        | The type of laptop (e.g., Notebook, Ultrabook, Gaming).                   |
| `Inches`          | The screen size of the laptop in inches.                                  |
| `ScreenResolution`| The resolution of the screen (e.g., 1920x1080).                           |
| `Cpu`             | The type and speed of the processor (e.g., Intel Core i7 2.3GHz).         |
| `Ram`             | The RAM size in GB.                                                       |
| `Memory`          | Storage type and size (e.g., 256GB SSD, 1TB HDD).                         |
| `Gpu`             | The graphics card model (e.g., NVIDIA GTX 1050, Intel UHD Graphics).      |
| `OpSys`           | The operating system installed (e.g., Windows, macOS, Linux).             |
| `Weight`          | The weight of the laptop in kilograms.                                    |
| `Price_euros`     | The price of the laptop in Euros (Target variable for prediction).         |

---

## Setup

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/damamrajeswari/LaptopPricePrediction.git
2. **Install the requirements**:
   ```bash
   pip install -r requirments.txt
3. **Run the command**:
   ```bash
   streamlit run app.py
4. **You can see the app in browser**
   



