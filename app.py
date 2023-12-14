from flask import Flask, render_template, request, redirect, url_for
from IndividualGraphs import getManCityData, getArsenalData, getBrightonData, getNewcastleData
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
        return render_template('plot_template.html', plotly_figure=result)
    if(dataset_index == '1'):    
        result = getArsenalData( int(index))
        return render_template('plot_template.html', plotly_figure=result)
    if(dataset_index == '2'):    
        result = getBrightonData( int(index))
        return render_template('plot_template.html', plotly_figure=result)
    if(dataset_index == '3'):    
        result = getNewcastleData( int(index))
        return render_template('plot_template.html', plotly_figure=result)
    return redirect(url_for('home'))
if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)