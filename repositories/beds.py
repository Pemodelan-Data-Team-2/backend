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

def available_beds_by_room(room_id):
    dc = 'usa'
    if 'usa' in room_id:
        dc = 'usa'
    elif 'idn' in room_id:
        dc = 'idn'
    session = create_session(dc=dc)
    row = session.execute(f"""
        SELECT * FROM available_beds_by_room WHERE room_id='{room_id} AND is_occupied=false;
    """)
    df = pd.DataFrame(row)
    return df