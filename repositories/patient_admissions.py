import sys
sys.path.append('../')
import pandas as pd

from repositories.create_session_v2 import create_session

def get_patient_admission_by_id(id):
    """
    Function to get patient admission info by its id
    """
    dc = 'usa'
    if 'usa' in id:
        dc = 'usa'
    elif 'idn' in id:
        dc = 'idn'
    session = create_session(dc=dc)
    row = session.execute(f"""
        SELECT * FROM patient_admissions WHERE admission_id='{id}' ALLOW FILTERING;
    """)
    df = pd.DataFrame(row)
    return df

def patient_admissions_by_room(country, room_id):
    dc = 'usa'
    if country.lower() == 'usa':
        dc = 'usa'
    elif country.lower() == 'idn':
        dc = 'idn'
    session = create_session(dc=dc)

    if room_id == None:
        row = session.execute(f"""
            SELECT * FROM patient_admissions_by_room;
        """)
    else:
        row = session.execute(f"""
            SELECT * FROM patient_admissions_by_carecenter WHERE room_id='{room_id}' ALLOW FILTERING;
        """)

    df = pd.DataFrame(row)
    return df

def patient_admissions_by_carecenter(country, care_center_id=None):
    """
    Function to get patient admissions by carecenter
    """
    dc = 'usa'
    if country.lower() == 'usa':
        dc = 'usa'
    elif country.lower() == 'idn':
        dc = 'idn'
    session = create_session(dc=dc)

    if care_center_id == None:
        row = session.execute(f"""
            SELECT * FROM patient_admissions_by_carecenter;
        """)
    else:
        row = session.execute(f"""
            SELECT * FROM patient_admissions_by_carecenter WHERE care_center_id='{care_center_id}' ALLOW FILTERING;
        """)

    df = pd.DataFrame(row)
    return df

def patient_admissions_by_city(country, city=None):
    """
    Function to get patient admissions by city
    """
    dc = 'usa'
    if country.lower() == 'usa':
        dc = 'usa'
    elif country.lower() == 'idn':
        dc = 'idn'
    session = create_session(dc=dc)

    if city == None:
        row = session.execute(f"""
            SELECT * FROM patient_admissions_by_city;
        """)
    else:
        row = session.execute(f"""
            SELECT * FROM patient_admissions_by_city WHERE city='{city}' ALLOW FILTERING;
        """)

    df = pd.DataFrame(row)
    return df

def patient_admissions_by_state(country, state=None):
    """
    Function to get patient admissions by state
    """
    dc = 'usa'
    if country.lower() == 'usa':
        dc = 'usa'
    elif country.lower() == 'idn':
        dc = 'idn'
    session = create_session(dc=dc)

    if state == None:
        row = session.execute(f"""
            SELECT * FROM patient_admissions_by_state;
        """)
    else:
        row = session.execute(f"""
            SELECT * FROM patient_admissions_by_state WHERE state='{state}' ALLOW FILTERING;
        """)

    df = pd.DataFrame(row)
    return df

def patient_admissions_by_country(country=None):
    """
    Function to get patient admissions by country
    """
    if country == None:
        session1 = create_session(dc='usa')
        row1 = session1.execute(f"""
            SELECT * FROM patient_admissions_by_country;
        """)

        session2 = create_session(dc='idn')
        row2 = session2.execute(f"""
            SELECT * FROM patient_admissions_by_country;
        """)

        df_usa = pd.DataFrame(row1)
        df_idn = pd.DataFrame(row2)
        df = pd.concat([df_usa, df_idn])
        return df
    else:
        dc = 'usa'
        if country.lower() == 'usa':
            dc = 'usa'
        elif country.lower() == 'idn':
            dc = 'idn'
        session = create_session(dc=dc)
        row = session.execute(f"""
            SELECT * FROM patient_admissions_by_country;
        """)

        df = pd.DataFrame(row)
        return df
