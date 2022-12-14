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
        usa_IPs = ['35.236.63.14', '34.102.10.24', '34.94.196.99']
        try:
            cluster = Cluster([usa_IPs[0]])
            session = cluster.connect('hospital_occupancy')
            print(f"Accessing DC: {dc}. External IP {usa_IPs[0]}")
            return session
        except:
            pass

        try:
            cluster = Cluster([usa_IPs[1]])
            session = cluster.connect('hospital_occupancy')
            print(f"Accessing DC: {dc}. External IP {usa_IPs[1]}")
            return session
        except:
            pass

        try:
            cluster = Cluster([usa_IPs[2]])
            session = cluster.connect('hospital_occupancy')
            print(f"Accessing DC: {dc}. External IP {usa_IPs[2]}")
            return session
        except:
            print(f'Failed to create connection to data center in {dc}')

    elif dc.lower()=='idn':
        idn_IPs = ['34.101.68.46', '34.101.181.96', '34.101.169.91']
        try:
            cluster = Cluster([idn_IPs[0]])
            session = cluster.connect('hospital_occupancy')
            print(f"Accessing DC: {dc}. External IP {idn_IPs[0]}")
            return session
        except:
            pass

        try:
            cluster = Cluster([idn_IPs[1]])
            session = cluster.connect('hospital_occupancy')
            print(f"Accessing DC: {dc}. External IP {idn_IPs[0]}")
            return session
        except:
            pass

        try:
            cluster = Cluster([idn_IPs[2]])
            session = cluster.connect('hospital_occupancy')
            print(f"Accessing DC: {dc}. External IP {idn_IPs[0]}")
            return session
        except:
            print(f'Failed to create connection to data center in {dc}')

    else:
        raise ValueError('Invalid data center')
