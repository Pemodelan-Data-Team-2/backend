import sys
sys.path.append('../')
import pandas as pd

from repositories.create_session_v2 import create_session

def get_carecenters_by_id(id, created_session):
    """
    Function to get a care center by its id
    """
    session = created_session
    row = session.execute(f"""
        SELECT * FROM carecenters WHERE care_center_id='{id}' ALLOW FILTERING;
    """)
    df = pd.DataFrame(row)
    return df

def carecenters_by_city(created_session, city=None):
    """
    Function to get carecenters that are located in given city
    """
    session = created_session

    if city == None:
        row = session.execute(f"""
            SELECT * FROM carecenters_by_city;
        """)
    else:
        row = session.execute(f"""
            SELECT * FROM carecenters_by_city WHERE city='{city}' ALLOW FILTERING;
        """)

    df = pd.DataFrame(row)
    return df

def carecenters_by_state(created_session, state=None):
    """
    Function to get carecenters that are located in given state
    """
    session = created_session

    if state == None:
        row = session.execute(f"""
            SELECT * FROM carecenters_by_state;
        """)
    else:
        row = session.execute(f"""
            SELECT * FROM carecenters_by_state WHERE state='{state}' ALLOW FILTERING;
        """)
    df = pd.DataFrame(row)
    return df

def carecenters_by_country(created_session):
    """
    Function to get carecenters
    """
    session = created_session
    row = session.execute(f"""
        SELECT * FROM carecenters_by_country;
    """)
    df = pd.DataFrame(row)
    return df


# test = get_carecenters_by_id('cc-usa-1')
# print(test)
# test = carecenters_by_city('idn', city='Badung')
# print(test)