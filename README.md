# wAIs: Wise Agricultural Insights for Sustainability

*wAIs* is an AI-powered deep learning smart grocery companion that empowers Filipino consumers to make smart shopping decisions and save on everyday staples. Based on reliable sources and sophisticated deep learning models, wAIs decides when and where to shop for optimal results—allowing users to enjoy healthy, affordable food on their tables without breaking the bank.
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Workflow](#workflow)
- [Architecture](#architecture)
- [Challenges & Future Improvements](#challenges--future-improvements)
- [Installation & Setup](#installation--setup)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview

wAIs hopes to make it more affordable for all Filipinos—especially those living in poor communities—to eat and manage their money better. With sustainability in mind, our app uses AI to predict the best times to shop.

---

## Problem Statement

- *Food Security:* Unstable market volatility and increasing prices threaten access to healthy, affordable food.
- *Financial Management:* Unpredictable expenses hinder families from having control over their money.

---

## Features

- *Price Prediction:* Indicates when to purchase provisions, like the rice hitting the 20 PHP price.
- *Smart Insights:* Provides advice on where to shop at lowest prices.
- *User-Friendly Interface:* Intuitive Vue-based front end for easy and swift inputs.
- *Data-Driven:* Based on hand-scraped and pre-processed data retrieved from da.gov.ph.
- *Community-Based:* In consideration of the needs of ordinary Filipinos, particularly those from marginal communities.

---

## Tech Stack

- *Frontend:* Vue.js  
- *Backend:* Django  
- *Machine Learning:* Keras (with dual LSTM layers and dropout)  
- *Database:* PostgreSQL  
- *External Services:* Clerk (for secure API integration)  
- *Collaboration:* GitHub and Figma

---

## Workflow

1. *Data Preparation:*  
   - Load CSV data from da.gov.ph.  
   - Cleanse the data (remove errors, convert dates, filter rows).

2. *Statistical Analysis:*  
   - Calculate key statistics (mean, variance) to normalize data.

3. *Neural Network Model:*  
   - Build and train a model using Keras (with two LSTM layers and dropout) to forecast trends.

4. *Prediction:*  
   - Process user inputs through the Django backend and return actionable predictions via the Vue front end.

5. *Output:*  
   - Display the best time and place to shop.

---

## Architecture

- *User Interface (UI):*  
  - A responsive Vue.js application where users enter their shopping needs.
  
- *Backend Processing:*  
  - Django handles API requests, selects the correct prediction model based on commodity and market, and processes the data.

- *Prediction Pipeline:*  
  - The deep learning model (built in Keras) uses historical data to forecast optimal shopping times, then returns the prediction to the user.

- *Data Flow:*  
  - *UI → Backend Request → Model Selection & Prediction → UI Output*

---

## Challenges & Future Improvements

*Challenges:*

- *Data Cleansing:* Handling inconsistencies and errors in raw data.
- *Modeling Complexity:* Building accurate predictive models.
- *Documentation:* Navigating outdated library documentation.

*Future Improvements:*

- Enhance the UI/UX for better user experience.
- Expand data sources to cover more markets and commodities.
- Optimize models for higher prediction accuracy.
- Continuous model training and real-time prediction updates.
- Make mobile application for ease-of-usage purposes.
