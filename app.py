from flask import Flask, render_template, url_for, redirect, request
from werkzeug.serving import run_simple
from backend import StockExchangeData


app = Flask(__name__)
stockExData = None

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route('/')
def index():
    try:
        stockExData = StockExchangeData()
        indices_list = stockExData.get_index_list()
        output_as_table = stockExData.fetch_details()
        # print(output_as_table)
    except Exception as e:
        print(f"Error during fetching: {str(e)}")
    return render_template('index.html', table=output_as_table, indices=indices_list)


@app.route('/index-data/<indexName>')
def fetch_index_data(indexName):
    try:
        stockExData = StockExchangeData()
        output_as_table = stockExData.fetch_details(index=indexName)
        return output_as_table
    except Exception as err:
        print(f"Error fetching data: {str(err)}")
        return err


if __name__ == '__main__':
    run_simple('0.0.0.0', 5000, app, use_debugger=True, use_reloader=True)