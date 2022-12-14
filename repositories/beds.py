import pandas as pd

from create_session import create_session

def get_bed_by_id(id):
    dc = 'usa'
    if 'usa' in id:
        dc = 'usa'
    elif 'idn' in id:
        dc = 'idn'
    session = create_session(dc=dc)
    row = session.execute(f"""
        SELECT * FROM beds WHERE bed_id='{id}' ALLOW FILTERING;
    """)
    df = pd.DataFrame(row)
    return df

def available_beds_by_room(country, room_id=None, is_available=True):
    dc = 'usa'
    if country.lower() == 'usa':
        dc = 'usa'
    elif country.lower() == 'idn':
        dc = 'idn'
    session = create_session(dc=dc)

    if room_id == None:
        row = session.execute(f"""
            SELECT * FROM available_beds_by_room WHERE is_occupied={is_available} ALLOW FILTERING;
        """)
    else:
        row = session.execute(f"""
            SELECT * FROM available_beds_by_room WHERE is_occupied={is_available} AND room_id='{room_id}' ALLOW FILTERING;
        """)
    df = pd.DataFrame(row)
    return df