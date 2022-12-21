from flask import Flask

from services.reports import CountryReports
import create_reports 

app = Flask(__name__)

@app.route('/dashboard/data', methods=['GET'])
def get_dashboard_data():
    """
    Function to get dictionary of all formatted data for Dashboard page in frontend
    """
    return {
        'annualTotalAdmittedPatientsByRoomType': create_reports.annual_admitted_patients_by_room_type(),
        'annualTotalAdmittedPatientsByCountry': create_reports.annual_admitted_patients_bar_chart_data(),
        'annualRevenuesGeneratedFromPatientAdmissions': create_reports.annual_revenues_line_chart_data(),
        'roomsCountByCareCenter': create_reports.rooms_count_by_care_center(),
    }

@app.route('/statistics/pa-counts-by-carecenter', methods=['GET'])
def get_pa_counts_by_cc():
    """
    Function to get formatted data for Statistics page in frontend
    """
    return {'statistics': create_reports.patient_admission_count_by_care_center()}

@app.route('/statistics/pa-counts-by-room-type', methods=['GET'])
def get_pa_counts_by_room_type():
    """
    Function to get formatted data for Statistics page in frontend
    """
    return {'statistics': create_reports.patient_admisson_count_by_room_type()}

@app.route('/statistics/beds-availability', methods=['GET'])
def get_beds_availability_by_country():
    """
    Function to get formatted data for Statistics page in frontend
    """
    return {'statistics': create_reports.beds_availability_by_current_date_table_data()}

@app.route('/data/carecenters', methods=['GET'])
def get_carecenters():
    """
    Function to get formatted data for Data page in frontend
    """
    return {'data': create_reports.care_centers_table()}

@app.route('/data/patient-admissions-by-country', methods=['GET'])
def get_patient_admissions_by_country():
    """
    Function to get formatted data for Data page in frontend
    """
    return {'data': create_reports.patient_admissions_table()}

if __name__ == '__main__':
    app.run(debug=True)