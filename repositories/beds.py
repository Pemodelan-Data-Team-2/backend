import sys
sys.path.append('../')
import pandas as pd

from repositories.create_session_v2 import create_session

def get_bed_by_id(id, created_session):
    session = created_session
    row = session.execute(f"""
        SELECT * FROM beds WHERE bed_id='{id}' ALLOW FILTERING;
    """)
    df = pd.DataFrame(row)
    return df

def beds_by_room(created_session, room_id=None):
    session = created_session

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

def beds(created_session):
    session = created_session

    row = session.execute(f"""
        SELECT * FROM beds;
    """)
    df = pd.DataFrame(row)
    return df

# #test
# from create_session_v2 import create_session

# session = create_session('usa')
# df = beds(session)
# print(df)
    