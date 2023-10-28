# Crypto DAU Web Portal 🌄🔮🚀

![Crypto DAU Web Portal](header_cryptodau.jpg)
## Project Overview 📊

Welcome to the Crypto DAU Web Portal, where you can explore Daily Active User (DAU) counts for the top 10 cryptocurrencies. This project fetches historical DAU data from the CoinGecko API and presents it using Plotly, creating a user-friendly line graph.

## Key Features 🌟

- Explore DAU counts for the top 10 cryptocurrencies.
- Utilizes the CoinGecko API to retrieve historical DAU data.
- Presents the data in an interactive line graph created with Plotly.
- Customize the web app's appearance using CSS.

## Project Structure 📂

- `app.py`: The main Flask application that serves the web page and handles requests.
- `templates/index.html`: The HTML template for the web page.
- `static/style.css`: The CSS file for customizing the web app's appearance.
- `your_script.py`: The Python script responsible for fetching data and generating the Plotly graph (replace with your own script).
- `crypto_dau_plot.html`: The HTML file where the Plotly graph is saved (generated by your script).

## Usage Instructions 🚀

1. Ensure you have Python, Flask, Plotly, and other required libraries installed.

2. Run the Flask application by executing `app.py`:

   ```shell
   python app.py
