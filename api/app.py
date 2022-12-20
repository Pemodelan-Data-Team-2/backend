import sys
sys.path.append('../')

from flask import Flask

from services.reports import CountryReports
import api.create_reports as create_reports

app = Flask(__name__)

@app.route('/dashboard/data', methods=['GET'])
def get_dashboard_data():
    """
    Function to get dictionary of all formatted data for Dashboard page in frontend
    """
    pass

@app.route('/statistics/pa-counts-by-carecenter', methods=['GET'])
def get_pa_counts_by_cc():
    """
    Function to get formatted data for Statistics page in frontend
    """
    pass

@app.route('/statistics/pa-counts-by-room-type', methods=['GET'])
def get_pa_counts_by_room_type():
    """
    Function to get formatted data for Statistics page in frontend
    """
    pass

@app.route('/data/carecenters', methods=['GET'])
def get_carecenters():
    """
    Function to get formatted data for Data page in frontend
    """
    pass

@app.route('/data/patient-admissions-by-country', methods=['GET'])
def get_patient_admissions_by_country():
    """
    Function to get formatted data for Data page in frontend
    """
    pass

if __name__ == '__main__':
    app.run(debug=True)