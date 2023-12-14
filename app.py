from flask import Flask, render_template, request, redirect, url_for, send_file
from IndividualGraphs import getManCityData, getArsenalData, getBrightonData, getNewcastleData
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import io
import plotly.io as pio
import base64
#Dataset from : https://www.kaggle.com/datasets/acothaha/epl-dataset-20222023-update-every-week
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('testPage.html')

@app.route('/run_python_script.html')
def run_python_script():
    dataset_index = request.args.get('datasetIndex')
    index = request.args.get('index') 
    if(dataset_index == '0'):    
        result = getManCityData( int(index))
        img_bytes = pio.to_image(result, format='png')
        img_base64 = base64.b64encode(img_bytes).decode('utf-8')
        html_content = f'<img src="data:image/png;base64,{img_base64}" alt="scatter_plot">'
        return render_template('plot_template.html', content=html_content)
    if(dataset_index == '1'):    
        result = getArsenalData( int(index))
        img_bytes = pio.to_image(result, format='png')
        img_base64 = base64.b64encode(img_bytes).decode('utf-8')
        html_content = f'<img src="data:image/png;base64,{img_base64}" alt="scatter_plot">'
        return render_template('plot_template.html', content=html_content)
    if(dataset_index == '2'):    
        result = getBrightonData( int(index))
        img_bytes = pio.to_image(result, format='png')
        img_base64 = base64.b64encode(img_bytes).decode('utf-8')
        html_content = f'<img src="data:image/png;base64,{img_base64}" alt="scatter_plot">'
        return render_template('plot_template.html', content=html_content)
    if(dataset_index == '3'):    
        result = getNewcastleData( int(index))
        img_bytes = pio.to_image(result, format='png')
        img_base64 = base64.b64encode(img_bytes).decode('utf-8')
        html_content = f'<img src="data:image/png;base64,{img_base64}" alt="scatter_plot">'
        return render_template('plot_template.html', content=html_content)
    return redirect(url_for('home'))
if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    #app.run(debug=True)