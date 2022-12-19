import sys
sys.path.append('../')
import pandas as pd

from repositories.create_session_v2 import create_session

def get_patient_admission_by_id(id, created_session):
    """
    Function to get patient admission info by its id
    """
    dc = 'usa'
    if 'usa' in id:
        dc = 'usa'
    elif 'idn' in id:
        dc = 'idn'
    session = created_session
    row = session.execute(f"""
        SELECT * FROM patient_admissions WHERE admission_id='{id}' ALLOW FILTERING;
    """)
    df = pd.DataFrame(row)
    return df

def patient_admissions_by_room(room_id, created_session):
    session = created_session

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

def patient_admissions_by_carecenter(created_session, care_center_id=None):
    """
    Function to get patient admissions by carecenter
    """
    session = created_session

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

def patient_admissions_by_city(created_session, city=None):
    """
    Function to get patient admissions by city
    """
    session = created_session

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

def patient_admissions_by_state(created_session, state=None):
    """
    Function to get patient admissions by state
    """
    session = created_session

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

def patient_admissions_by_country(created_session):
    """
    Function to get patient admissions by country
    """
    session = created_session
    row = session.execute(f"""
        SELECT * FROM patient_admissions_by_country;
    """)

    df = pd.DataFrame(row)
    return df
