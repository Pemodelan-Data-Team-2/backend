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

def patient_admission_count_by_care_center():
    data1 = usa_instance.patient_admissions_by_country()
    data2 = usa_instance.patient_admissions_per_annum_by_cc(data1)

    data3 = idn_instance.patient_admissions_by_country()
    data4 = usa_instance.patient_admissions_per_annum_by_cc(data3)

    output = []
    n = 1
    for i,j in zip(data2.iterrows(),data4.iterrows()) :
        per_year_usa = {'id' : n,
                    'year' : str(i[1][0]),
                    'care_center_id':i[1][1],
                    'total_admitted_patients':i[1][2],
                    'country' :i[1][1][3:6]}
        output.append(per_year_usa)
        per_year_idn = {'id' : n+1,
                'year' : str(j[1][0]),
                'care_center_id':j[1][1],
                'total_admitted_patients':j[1][2],
                'country' :j[1][1][3:6]}
        output.append(per_year_idn)
        n+=2
    return output

def rooms_count_by_care_center():
    usa_rooms_by_cc = usa_instance.rooms_by_carecenter()
    idn_rooms_by_cc = idn_instance.rooms_by_carecenter()

    gb_count_by_cc_usa = usa_rooms_by_cc.groupby('care_center_id',as_index = False).count()
    gb_count_by_cc_idn = idn_rooms_by_cc.groupby('care_center_id',as_index = False).count()

    output = [{
        'care_center_id' : 'cc-usa-1',
        'care_center_name': 'Global Health MVCH',
        'country' :'USA',
        'num_of_rooms' : int(gb_count_by_cc_usa['room_id'][0])
    },
    {
        'care_center_id' : 'cc-usa-2',
        'care_center_name': 'MedStar MVCH',
        'country' :'USA',
        'num_of_rooms' : int(gb_count_by_cc_usa['room_id'][1])

    },
    {
        'care_center_id' : 'cc-idn-1',
        'care_center_name': 'Medistra MVCH',
        'country' :'IDN',
        'num_of_rooms' : int(gb_count_by_cc_idn['room_id'][0])
    },
    {
        'care_center_id' : 'cc-idn-1',
        'care_center_name': 'Rumah Sakit Mitra Keluarga MVCH',
        'country' :'IDN',
        'num_of_rooms' : int(gb_count_by_cc_idn['room_id'][1])
    }]

    return output

def annual_admitted_patients_bar_chart_data():
    usa_patient_admitted = usa_instance.patient_admissions_by_country()
    idn_patient_admitted = idn_instance.patient_admissions_by_country()

    usa_annum_count = usa_instance.patient_admissions_per_annum(df = usa_patient_admitted)
    idn_annum_count = idn_instance.patient_admissions_per_annum(df = idn_patient_admitted)
    output = []
    for n,year in enumerate(usa_annum_count['year']):
        peryear = {"year" : str(year),
                    "USA": usa_annum_count['total_admitted_patients'][n],
                    "USAColor" : "hsl(128,70%,50%)",
                    "IDN": idn_annum_count['total_admitted_patients'][n],
                    "IDNColor": "hsl(169,70%,50%)"}
        output.append(peryear)
    return output

def care_centers_table():
    usa_cc_by_country = usa_instance.carecenters_by_country()
    idn_cc_by_country = idn_instance.carecenters_by_country()
    df_concat = pd.concat([usa_cc_by_country,idn_cc_by_country])
    output = []
    n = 0
    for i in df_concat.iterrows():
        cc_table = {'id': n+1,
            'country': i[1][0],
            'care_center_id': i[1][1],
            'care_center_name': i[1][3],
            'address': i[1][2][0]}
        output.append(cc_table)
        n+=1
    return output

def patient_admisson_count_by_room_type():
    usa_patient_admitted = usa_instance.patient_admissions_by_country()
    idn_patient_admitted = idn_instance.patient_admissions_by_country()

    usa_patient_admitted = usa_instance.get_room_type(usa_patient_admitted)
    idn_patient_admitted = usa_instance.get_room_type(idn_patient_admitted)

    usa_annum_count = usa_instance.patient_admissions_per_annum_by_room_type(df = usa_patient_admitted)
    idn_annum_count = idn_instance.patient_admissions_per_annum_by_room_type(df = idn_patient_admitted)

    output = []
    n = 1
    for year in (usa_annum_count['year'].unique()):
        df_peryear_usa =  usa_annum_count[usa_annum_count['year'] == year]
        df_peryear_idn = idn_annum_count[idn_annum_count['year'] == year]
        peryear_usa = { "id" : 0,
                    "country" : "USA",
                    "year": str(year),
                    "Class I" : 0,
                    "Class II" : 0,
                    "Class III" : 0 ,
                    "VIP" : 0,
                    "VVIP" : 0}
        peryear_idn = peryear_usa.copy()

        for room in df_peryear_idn['room_type']:
            peryear_idn[room] = int(df_peryear_usa[df_peryear_usa['room_type'] == room]['total_admitted_patients'])
            peryear_usa[room] = int(df_peryear_idn[df_peryear_idn['room_type'] == room]['total_admitted_patients'])
            peryear_idn['country'] = 'IDN'

        peryear_usa['id'] = n
        peryear_idn['id'] = n+1
        output.append(peryear_usa)
        output.append(peryear_idn)
        n+=2

    return output

def patient_admissions_table():
    usa_patient_admitted = usa_instance.patient_admissions_by_country()
    idn_patient_admitted = idn_instance.patient_admissions_by_country()

    df_concat = pd.concat([usa_patient_admitted,idn_patient_admitted])
    output = []
    n = 1
    for i in df_concat.iterrows():
        patient_table = {
                        'id': n,
                        'admission_id': i[1][1],
                        'country': i[1][0],
                        'patient_id': i[1][7],
                        'bed_id': i[1][4],
                        'room_id': i[1][8],
                        'care_center_id': i[1][5],
                        'admitted_date': str(i[1][3]),
                        'discharged_date': str(i[1][6]),
                        'admitted_causes': i[1][2],
                        'room_rate_per_night': float(i[1][9]),
                        'room_rate_total': float(i[1][10])
                        }
        output.append(patient_table)
        n+=1

    return output

def care_centers_table():
    usa_cc_by_country = usa_instance.carecenters_by_country()
    idn_cc_by_country = idn_instance.carecenters_by_country()
    df_concat = pd.concat([usa_cc_by_country,idn_cc_by_country])
    output = []
    n = 0
    for i in df_concat.iterrows():
        cc_table = {'id': n+1,
            'country': i[1][0],
            'care_center_id': i[1][1],
            'care_center_name': i[1][3],
            'address': f"{i[1][2][0]}, {i[1][2][1]}, {i[1][2][2]}, {i[1][2][3]}, {i[1][2][4]}"}
        output.append(cc_table)
        n+=1
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

def annual_admitted_patients_by_room_type():
    usa_patient_admitted = usa_instance.patient_admissions_by_country()
    idn_patient_admitted = idn_instance.patient_admissions_by_country()

    usa_patient_admitted = usa_instance.get_room_type(usa_patient_admitted)
    idn_patient_admitted = usa_instance.get_room_type(idn_patient_admitted)

    usa_annum_count = usa_instance.patient_admissions_per_annum_by_room_type(df = usa_patient_admitted)
    idn_annum_count = idn_instance.patient_admissions_per_annum_by_room_type(df = idn_patient_admitted)

    output = []
    for year in (usa_annum_count['year'].unique()):
        df_peryear_usa =  usa_annum_count[usa_annum_count['year'] == year]
        df_peryear_idn = idn_annum_count[idn_annum_count['year'] == year]
        peryear = {"year": str(year),
                    "Class I" : 0,
                    "Class IColor" : 'hsl(128,70%,50%)',
                    "Class II" : 0,
                    "Class IIColor" : 'hsl(130,20%,10%)',
                    "Class III" : 0 ,
                    "Class IIIColor" : 'hsl(122,40%,80%)',
                    "VIP" : 0,
                    "VIPColor" : 'hsl(100,20%,20%)',
                    "VVIP" : 0,
                    "VVIPColor" : 'hsl(70,60%,90%)'}

        for room in df_peryear_idn['room_type']:
            sum_count = int(df_peryear_usa[df_peryear_usa['room_type'] == room]['total_admitted_patients']) + int(df_peryear_idn[df_peryear_idn['room_type'] == room]['total_admitted_patients'])
            peryear[room] = sum_count
        output.append(peryear)

    return output
