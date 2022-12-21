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

    data = [usa_annual_revenues,idn_annual_revenues]
    return data

def monthly_revenues_line_chart_data():
    usa_monthly_revenues = usa_instance.patient_admissions_by_country()
    idn_monthly_revenues = idn_instance.patient_admissions_by_country()

    usa_monthly_revenues = usa_instance.patient_admissions_revenues_per_month(df=usa_monthly_revenues)
    idn_monthly_revenues = idn_instance.patient_admissions_revenues_per_month(df=idn_monthly_revenues)

    data = [usa_monthly_revenues,idn_monthly_revenues]
    return data

def quarterly_revenues_line_chart_data():
    usa_quarter_revenues = usa_instance.patient_admissions_by_country()
    idn_quarter_revenues = idn_instance.patient_admissions_by_country()

    usa_quarter_revenues = usa_instance.patient_admissions_revenues_per_quarter(df=usa_quarter_revenues)
    idn_quarter_revenues = idn_instance.patient_admissions_revenues_per_quarter(df=idn_quarter_revenues)

    data = [usa_quarter_revenues,idn_quarter_revenues]
    return data

def annual_admitted_patients_bar_chart_data():
    usa_patient_admitted = usa_instance.patient_admissions_by_country()
    idn_patient_admitted = idn_instance.patient_admissions_by_country()

    usa_annum_count = usa_instance.patient_admissions_per_annum(df = usa_patient_admitted)
    idn_annum_count = idn_instance.patient_admissions_per_annum(df = idn_patient_admitted)
    output = []
    for n,year in enumerate(usa_annum_count['year']):
        peryear = {"year" : str(i),
                    "USA": usa_annum_count['total_admitted_patients'][n],
                    "USAColor" : "hsl(128,70%,50%)",
                    "IDN": idn_annum_count['total_admitted_patients'][n],
                    "IDNColor": "hsl(169,70%,50%)"}
        output.append(peryear)
    return output

def annual_revenues_from_patient_admissions_by_state_table_data():
    usa_patient_admitted_by_state = usa_instance.patient_admissions_by_state()
    idn_patient_admitted_by_state = idn_instance.patient_admissions_by_state()

    usa_revenue_by_state = usa.instance.revenues_by_state_per_annum(df = usa_patient_admitted_by_state)
    idn_revenue_by_state = idn.instance.revenues_by_state_per_annum(df = idn_patient_admitted_by_state)

    output = [usa_revenue_by_state,idn_revenue_by_state]
    return output

def annual_admissions_by_state_table_data():
    usa_patient_admitted_by_state = usa_instance.patient_admissions_by_state()
    idn_patient_admitted_by_state = idn_instance.patient_admissions_by_state()

    usa_count_by_state = usa.instance.patient_admission_by_state_per_year(df = usa_patient_admitted_by_state)
    idn_count_by_state = idn.instance.patient_admission_by_state_per_year(df = idn_patient_admitted_by_state)

    output = [usa_count_by_state,idn_count_by_state]

    return output

def beds_availability_by_current_date_table_data():
    usa_beds = usa_instance.beds()
    idn_beds = idn_instance.beds()
    
    usa_admission = usa_instance.patient_admissions_by_country()
    idn_admission = idn_instance.patient_admissions_by_country()
    
    
    usa_count_by_state = usa.instance.beds_status_per_current_date(df_beds = usa_beds, df_patient = usa_admission)
    idn_count_by_state = idn.instance.beds_status_per_current_date(df_beds = idn_beds, df_patient=idn_admission)

    output = [usa_count_by_state,idn_count_by_state]

    return output
