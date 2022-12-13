from cassandra.cluster import Cluster
import pandas as pd

"""
USA External IPs:
35.236.63.14
34.102.10.24
34.94.196.99

IDN External IPs:
34.101.68.46
34.101.181.96
34.101.169.91
"""

def create_session(dc):
    """
    Function to create session to the corresponding data center
    """
    if dc.lower()=='usa':
        try:
            cluster = Cluster(['35.236.63.14'])
            session = cluster.connect('hospital_occupancy')
            return session
        except:
            pass

        try:
            cluster = Cluster(['34.102.10.24'])
            session = cluster.connect('hospital_occupancy')
            return session
        except:
            pass

        try:
            cluster = Cluster(['34.94.196.99'])
            session = cluster.connect('hospital_occupancy')
            return session
        except:
            print(f'Failed to create connection to data center in {dc}')

    elif dc.lower()=='idn':
        try:
            cluster = Cluster(['34.101.68.46'])
            session = cluster.connect('hospital_occupancy')
            return session
        except:
            pass

        try:
            cluster = Cluster(['34.101.181.96'])
            session = cluster.connect('hospital_occupancy')
            return session
        except:
            pass

        try:
            cluster = Cluster(['34.101.169.91'])
            session = cluster.connect('hospital_occupancy')
            return session
        except:
            print(f'Failed to create connection to data center in {dc}')

    else:
        raise ValueError('Invalid data center')
