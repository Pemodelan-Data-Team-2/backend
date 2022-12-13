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
        SELECT * FROM rooms WHERE room_id='{id}';
    """)
    df = pd.DataFrame(row)
    return df

def available_rooms_by_carecenter_date(care_center_id, date):
    # available: if occupancy_status = 'PartiallyOccupied' or 'NotOccupied'
    pass