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

def carecenters_by_city(country, city=None):
    """
    Function to get carecenters that are located in given city
    """
    dc = 'usa'
    if country.lower() == 'usa':
        dc = 'usa'
    elif country.lower() == 'idn':
        dc = 'idn'
    session = create_session(dc=dc)

    if city == None:
        row = session.execute(f"""
            SELECT * FROM carecenters_by_city;
        """)
    else:
        row = session.execute(f"""
            SELECT * FROM carecenters_by_city WHERE city='{city}';
        """)

    df = pd.DataFrame(row)
    return df

def carecenters_by_state(country, state=None):
    """
    Function to get carecenters that are located in given state
    """
    dc = 'usa'
    if country.lower() == 'usa':
        dc = 'usa'
    elif country.lower() == 'idn':
        dc = 'idn'
    session = create_session(dc=dc)

    if state == None:
        row = session.execute(f"""
            SELECT * FROM carecenters_by_state;
        """)
    else:
        row = session.execute(f"""
            SELECT * FROM carecenters_by_state WHERE state='{state}';
        """)
    df = pd.DataFrame(row)
    return df

def carecenters_by_country(country=None):
    """
    Function to get carecenters
    """
    if country == None:
        session1 = create_session(dc='usa')
        row1 = session1.execute(f"""
            SELECT * FROM carecenters_by_country;
        """)

        session2 = create_session(dc='idn')
        row2 = session2.execute(f"""
            SELECT * FROM carecenters_by_country;
        """)
        df_usa = pd.DataFrame(row1)
        df_idn = pd.DataFrame(row2)
        df = pd.concat([df_usa, df_idn])
        return df
    else:
        session = create_session(dc=country)
        row = session.execute(f"""
            SELECT * FROM carecenters_by_country;
        """)
        df = pd.DataFrame(row)


# test = get_carecenters_by_id('cc-usa-1')
# print(test)
test = carecenters_by_city('idn', city='Badung')
print(test)