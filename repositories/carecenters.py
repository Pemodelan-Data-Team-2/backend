import pandas as pd

from create_session import create_session

def get_carecenters_by_id(id):
    """
    Function to get a care center by its id
    """
    dc = 'usa'
    if 'usa' in id:
        dc = 'usa'
    elif 'idn' in id:
        dc = 'idn'
    session = create_session(dc=dc)
    row = session.execute(f"""
        SELECT * FROM carecenters WHERE care_center_id='{id}';
    """)
    df = pd.DataFrame(row)
    return df

def carecenters_by_city(city, country):
    """
    Function to get carecenters that are located in given city
    """
    dc = 'usa'
    if country.lower() == 'usa':
        dc = 'usa'
    elif country.lower() == 'idn':
        dc = 'idn'
    session = create_session(dc=dc)
    row = session.execute(f"""
        SELECT * FROM carecenters_by_city WHERE city='{city}';
    """)
    df = pd.DataFrame(row)
    return df

def carecenters_by_state(state, country):
    pass

def carecenters_by_country(country):
    pass


test = get_carecenters_by_id('cc-usa-1')
print(test)