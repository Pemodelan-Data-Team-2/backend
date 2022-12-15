import pandas as pd

from create_session import create_session

def get_room_by_id(id):
    dc = 'usa'
    if 'usa' in id:
        dc = 'usa'
    elif 'idn' in id:
        dc = 'idn'
    session = create_session(dc=dc)
    row = session.execute(f"""
        SELECT * FROM rooms WHERE room_id='{id}' ALLOW FILTERING;
    """)
    df = pd.DataFrame(row)
    return df

def rooms_by_carecenter(country, care_center_id=None):
    dc = 'usa'
    if country.lower() == 'usa':
        dc = 'usa'
    elif country.lower() == 'idn':
        dc = 'idn'
    session = create_session(dc=dc)

    if care_center_id == None:
        row = session.execute(f"""
            SELECT * FROM rooms_by_carecenter;
        """)
    else:
        row = session.execute(f"""
            SELECT * FROM rooms_by_carecenter WHERE care_center_id='{care_center_id}' ALLOW FILTERING;
        """)
    df = pd.DataFrame(row)
    return df
