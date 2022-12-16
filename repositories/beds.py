import sys
sys.path.append('../')
import pandas as pd

from repositories.create_session_v2 import create_session

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

def beds_by_room(country, room_id=None):
    dc = 'usa'
    if country.lower() == 'usa':
        dc = 'usa'
    elif country.lower() == 'idn':
        dc = 'idn'
    session = create_session(dc=dc)

    if room_id == None:
        row = session.execute(f"""
            SELECT * FROM beds_by_room;
        """)
    else:
        row = session.execute(f"""
            SELECT * FROM beds_by_room WHERE room_id='{room_id}' ALLOW FILTERING;
        """)
    df = pd.DataFrame(row)
    return df