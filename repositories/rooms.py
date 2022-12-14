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

def available_rooms_by_carecenter(country, care_center_id=None, available=True):
    # available: if occupancy_status = 'PartiallyOccupied' or 'NotOccupied'
    dc = 'usa'
    if 'usa' in id:
        dc = 'usa'
    elif 'idn' in id:
        dc = 'idn'
    session = create_session(dc=dc)

    if care_center_id == None:
        row = session.execute(f"""
            SELECT * FROM available_rooms_by_carecenter;
        """)
    else:
        if not available:
            row = session.execute(f"""
                SELECT * FROM available_rooms_by_carecenter WHERE care_center_id='{care_center_id}' ALLOW FILTERING;
            """)
        else:
            row = session.execute(f"""
                SELECT * FROM available_rooms_by_carecenter WHERE care_center_id='{care_center_id}' AND occupancy_status!='FullyOccupied' ALLOW FILTERING;
            """)
    df = pd.DataFrame(row)
    return df
