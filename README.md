# Crypto DAU Top 10 Simplistic Web App

## Project Overview

This project aims to create a simple web application that displays the Daily Active User (DAU) counts for the top 10 cryptocurrencies. The DAU data is fetched from the CoinGecko API, and the information is presented in the form of a line graph for easy visualization.

## Features

- Displays DAU counts for the top 10 cryptocurrencies.
- Utilizes the CoinGecko API to fetch historical DAU data.
- Presents the data in a line graph using Plotly.
- Customizes the web app appearance with CSS for a modern and clean design.

## Project Structure

- `app.py`: The main Flask application that serves the web page and handles requests.
- `templates/index.html`: The HTML template for the web page.
- `static/style.css`: The CSS file for customizing the web app's appearance.
- `your_script.py`: The Python script that fetches data and generates the Plotly graph (replace with your actual script).
- `crypto_dau_plot.html`: The HTML file where the Plotly graph is saved (generated by your script).

## Usage

1. Make sure you have Python, Flask, Plotly, and other necessary libraries installed.

2. Run the Flask application by executing `app.py`:

   ```shell
   python app.py
