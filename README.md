# Retail Price Optimization

## Introduction
This project aims to optimize retail prices for various products using machine learning techniques. By analyzing historical transaction data and considering various features such as product characteristics, competitor information, and market trends, we aim to predict the optimal price for each product in order to maximize profitability and customer satisfaction.

## Problem Statement
Retail businesses face the challenge of setting appropriate prices for their products in order to maximize revenue while remaining competitive in the market. Traditional methods of pricing often rely on manual analysis and intuition, which can be time-consuming and may not always yield optimal results. Additionally, factors such as seasonality, competitor pricing, and customer preferences further complicate the pricing decision process.

## Solution
We propose a machine learning-based approach to optimize retail prices by leveraging historical transaction data and relevant features. Our solution involves the following steps:

1. **Data Collection**: Gather historical transaction data including product details, prices, quantities sold, and other relevant features.
2. **Feature Engineering**: Preprocess the data and extract relevant features such as product characteristics, competitor information, and market trends. This may involve data cleaning, transformation, and feature selection.
3. **Model Training**: Utilize the XGBoost algorithm to train a machine learning model on the prepared dataset. XGBoost is a powerful algorithm known for its efficiency and accuracy in handling structured data.
4. **Model Evaluation**: Evaluate the trained model using appropriate metrics to assess its performance and generalization capability.
5. **Price Prediction**: Use the trained model to predict optimal prices for new products based on their features and market conditions.
6. **Deployment**: Dockerize the project and deploy it using Flask, allowing for easy integration with existing systems or APIs.

## Features Used
- `product_id`: A unique identifier for each product.
- `product_category_name`: The category to which the product belongs.
- `month_year`: The month and year of the transaction.
- `qty`: The quantity of the product sold.
- `total_price`: The total price of the product.
- `freight_price`: The shipping cost associated with the product.
- `unit_price`: The price of a single unit of the product.
- `product_name_length`: The length of the product name.
- `product_description_length`: The length of the product description.
- `product_photos_qty`: The number of photos available for the product.
- `product_weight_g`: The weight of the product.
- `product_score`: A score or rating associated with the product.
- `customers`: The number of customers who purchased the product.
- `weekday`: The day of the week of the transaction.
- `weekend`: A binary flag indicating whether the transaction occurred on a weekend.
- `holiday`: A binary flag indicating whether the transaction occurred on a holiday.
- `month`: The month of the transaction.
- `year`: The year of the transaction.
- `s`: The effect of seasonality.
- `comp_1`, `comp_2`, `comp_3`: Competitor information or variables.
- `ps1`, `ps2`, `ps3`: Product score associated with competitors’ products.
- `fp1`, `fp2`, `fp3`: Freight cost associated with competitors’ products.

## Tech Stack
- **ML Framework**: XGBoost
- **Containerization**: Docker
- **Web Framework**: Flask
- **Experimentation Tracking**: MLflow

## Usage
To reproduce the project's results, follow these steps:

1. Clone the repository.
2. Set up the MLflow tracking URI using the provided credentials.
3. Run the script `script.py` to train the model and track the experiments.
4. Dockerize the project using the provided Dockerfile.
5. Push the Docker image to Docker Hub for deployment.

## Experimentation Tracking
Experimentation tracking for this project is available on Dagshub. You can view detailed experiment logs, metrics, and visualizations to understand the model's performance.

## Docker Image
The Dockerized project has been pushed to Docker Hub and is available at `nrithvik19461/prize_opt:latest`.

## Contributors
[Your Name/Team Name]

## License
This project is licensed under the MIT License.
