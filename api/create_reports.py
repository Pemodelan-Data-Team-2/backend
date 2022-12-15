import sys
sys.path.append('../')

from services.reports import CountryReports

usa_instance = CountryReports(country='usa')
idn_instance = CountryReports(country='idn')

def annual_revenues_line_chart_data():
    usa_annual_revenues = usa_instance.patient_admissions_by_country()
    idn_annual_revenues = idn_instance.patient_admissions_by_country()

    usa_annual_revenues = usa_instance.patient_admissions_revenues_per_annum(df=usa_annual_revenues)
    idn_annual_revenues = idn_instance.patient_admissions_revenues_per_annum(df=idn_annual_revenues)

    data = []
    data.append(usa_annual_revenues)
    data.append(idn_annual_revenues)

    return data

def monthly_revenues_line_chart_data():
    pass

def quarterly_revenues_line_chart_data():
    pass

def annual_admitted_patients_bar_chart_data():
    pass

def annual_revenues_from_patient_admissions_by_state_table_data():
    pass



