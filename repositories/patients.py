import sys
sys.path.append('../')
import pandas as pd

from repositories.create_session_v2 import create_session

def get_patient_by_id(id, created_session):
    """
    Function to get patient info by its id
    """
    dc = 'usa'
    if 'usa' in id:
        dc = 'usa'
    elif 'idn' in id:
        dc = 'idn'
    session = created_session
    row = session.execute(f"""
        SELECT * FROM patients WHERE patient_id='{id}' ALLOW FILTERING;
    """)
    df = pd.DataFrame(row)
    return df