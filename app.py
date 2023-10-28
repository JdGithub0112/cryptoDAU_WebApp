from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    plotly_file = "crypto_dau_plot.html"  # The path to the saved plot HTML
    return render_template('index.html', plotly_file=plotly_file)

if __name__ == '__main__':
    app.run(debug=True)
