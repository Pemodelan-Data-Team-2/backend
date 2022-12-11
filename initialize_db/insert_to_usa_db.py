from cassandra.cluster import Cluster
import pandas as pd

"""
USA IPs:
- 34.102.10.24
- 34.102.10.99
- 34.102.10.14
"""
cluster = Cluster(['34.102.10.24'])
session = cluster.connect('hospital_occupancy')

def insert_carecenters():
    carecenters = pd.read_csv('./data/carecenters.csv', sep=';')

    for idx, row in carecenters.iterrows():
        session.execute(f"""
            INSERT INTO carecenters (care_center_id, care_center_name, address) 
            VALUES('{row['care_center_id']}', '{row['care_center_name']}', {row['address']})
        """)

insert_carecenters()

