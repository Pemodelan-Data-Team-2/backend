import sys
sys.path.append('../')

from flask import Flask, request

from services.reports import CountryReports


app = Flask(__name__)

@app.route('/get-annual-reports/<country>', methods=['GET'])
def get_annual_reports_per_country(country):
    country_reports = CountryReports(country=country)
    revenues_data = country_reports.revenues_from_patient_admissions_per_annum()
    admitted_patients_data = country_reports.admitted_patients_per_annum()
    pass

@app.route('/get-annual-reports-all-countries', methods=['GET'])
def get_annual_reports_all_countries():
    pass

if __name__ == '__main__':
    app.run(debug=True)
