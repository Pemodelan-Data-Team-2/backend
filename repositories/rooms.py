import sys
sys.path.append('../')
import pandas as pd

from repositories.create_session_v2 import create_session

def get_room_by_id(id, created_session):
    session = created_session
    row = session.execute(f"""
        SELECT * FROM rooms WHERE room_id='{id}' ALLOW FILTERING;
    """)
    df = pd.DataFrame(row)
    return df

def rooms_by_carecenter(created_session, care_center_id=None):
    session = created_session

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
