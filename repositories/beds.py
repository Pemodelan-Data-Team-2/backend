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
        SELECT * FROM beds WHERE bed_id='{id}';
    """)
    df = pd.DataFrame(row)
    return df

def available_beds_by_room(country, room_id=None):
    dc = 'usa'
    if country.lower() == 'usa':
        dc = 'usa'
    elif country.lower() == 'idn':
        dc = 'idn'
    session = create_session(dc=dc)
    if room_id == None:
        row = session.execute(f"""
            SELECT * FROM available_beds_by_room WHERE is_occupied=false;
        """)
    else:
        row = session.execute(f"""
            SELECT * FROM available_beds_by_room WHERE is_occupied=false AND room_id='{room_id}';
        """)
    df = pd.DataFrame(row)
    return df