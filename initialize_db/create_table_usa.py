from cassandra.cluster import Cluster

"""
USA IPs:
- 34.102.10.24
- 34.102.10.99
- 34.102.10.14
"""
cluster = Cluster(['34.102.10.24'])
session = cluster.connect()

"""
carecenters          carecenters_by_country  rooms
carecenters_by_city  carecenters_by_state

ARE ALREADY CREATED

Replication strategy => SimpleStragy (WILL BE CHANGED)
"""

# session.execute(
#     """
#     CREATE TABLE hospital_occupancy.available_rooms_by_carecenter_date (
#     care_center_id TEXT,
#     date_oi date,
#     room_id TEXT,
#     room_type TEXT,
#     occupancy_status TEXT,
#     rate DOUBLE,
#     PRIMARY KEY ((care_center_id), date_oi, room_id))
#     WITH COMMENT = 'Find available rooms by care center and date';
#     """
# )

# session.execute(
#     """
#     CREATE TABLE hospital_occupancy.beds (
#     bed_id TEXT PRIMARY KEY, 
#     room_id TEXT, 
#     care_center_id TEXT, 
#     is_occupied BOOLEAN) 
#     WITH COMMENT = 'Find information about a bed';
#     """
# )

# session.execute(
#     """
#     CREATE TABLE hospital_occupancy.available_beds_by_room (
#     room_id TEXT,
#     bed_id TEXT,
#     care_center_id TEXT,
#     is_occupied BOOLEAN,
#     PRIMARY KEY ((room_id), bed_id))
#     WITH COMMENT = 'Find available beds by room'
#     AND CLUSTERING ORDER BY (bed_id ASC);
#     """
# )

# session.execute(
#     """
#     CREATE TABLE hospital_occupancy.patients (
#     patient_id TEXT PRIMARY KEY,
#     mrn TEXT,
#     first_name TEXT,
#     last_name TEXT,
#     contact TEXT,
#     dob date,
#     address frozen<address>,
#     is_resident_patient BOOLEAN)
#     WITH COMMENT = 'Find information about a patient';
#     """
# )

# session.execute(
#     """
#     CREATE TABLE hospital_occupancy.patient_admissions (
#     admission_id TEXT PRIMARY KEY,
#     patient_id TEXT,
#     bed_id TEXT,
#     room_id TEXT,
#     care_center_id TEXT,
#     admitted_date date,
#     discharged_date date,
#     admitted_causes TEXT,
#     room_rate_per_night DOUBLE,
#     room_rate_total DOUBLE)
#     WITH COMMENT = 'Find information about a patient admission';
#     """
# )

# session.execute(
#     """
#     CREATE TABLE hospital_occupancy.patient_admissions_by_carecenter_period (
#     care_center_id TEXT,
#     period_start date,
#     period_end date,
#     admission_id TEXT,
#     patient_id TEXT,
#     bed_id TEXT,
#     room_id TEXT,
#     admitted_date date,
#     discharged_date date,
#     admitted_causes TEXT,
#     room_rate_per_night DOUBLE,
#     room_rate_total DOUBLE,
#     PRIMARY KEY ((care_center_id), period_start, period_end, admission_id))
#     WITH COMMENT = 'Find patient admissions by care center and period';
#     """
# )

# session.execute(
#     """
#     CREATE TABLE hospital_occupancy.patient_admissions_by_city_period (
#     city TEXT,
#     period_start date,
#     period_end date,
#     admission_id TEXT,
#     patient_id TEXT,
#     bed_id TEXT,
#     room_id TEXT,
#     care_center_id TEXT,
#     admitted_date date,
#     discharged_date date,
#     admitted_causes TEXT,
#     room_rate_per_night DOUBLE,
#     room_rate_total DOUBLE,
#     PRIMARY KEY ((city), period_start, period_end, admission_id))
#     WITH COMMENT = 'Find patient admissions by city and period';
#     """
# )

# session.execute(
#     """
#     CREATE TABLE hospital_occupancy.patient_admissions_by_state_period (
#     state TEXT,
#     period_start date,
#     period_end date,
#     admission_id TEXT,
#     patient_id TEXT,
#     bed_id TEXT,
#     room_id TEXT,
#     care_center_id TEXT,
#     admitted_date date,
#     discharged_date date,
#     admitted_causes TEXT,
#     room_rate_per_night DOUBLE,
#     room_rate_total DOUBLE,
#     PRIMARY KEY ((state), period_start, period_end, admission_id))
#     WITH COMMENT = 'Find patient admissions by state and period';
#     """
# )

# session.execute(
#     """
#     CREATE TABLE hospital_occupancy.patient_admissions_by_country_period (
#     country TEXT,
#     period_start date,
#     period_end date,
#     admission_id TEXT,
#     patient_id TEXT,
#     bed_id TEXT,
#     room_id TEXT,
#     care_center_id TEXT,
#     admitted_date date,
#     discharged_date date,
#     admitted_causes TEXT,
#     room_rate_per_night DOUBLE,
#     room_rate_total DOUBLE,
#     PRIMARY KEY ((country), period_start, period_end, admission_id))
#     WITH COMMENT = 'Find patient admissions by country and period';
#     """
# )

tables = session.execute(
        """describe tables;"""
    )

for idx, table in enumerate(tables):
    print(table)

"""
OUTPUT:

Row(keyspace_name='hospital_occupancy', type='table', name='available_beds_by_room')
Row(keyspace_name='hospital_occupancy', type='table', name='available_rooms_by_carecenter_date')
Row(keyspace_name='hospital_occupancy', type='table', name='beds')
Row(keyspace_name='hospital_occupancy', type='table', name='carecenters')
Row(keyspace_name='hospital_occupancy', type='table', name='carecenters_by_city')
Row(keyspace_name='hospital_occupancy', type='table', name='carecenters_by_country')
Row(keyspace_name='hospital_occupancy', type='table', name='carecenters_by_state')
Row(keyspace_name='hospital_occupancy', type='table', name='patient_admissions')
Row(keyspace_name='hospital_occupancy', type='table', name='patient_admissions_by_carecenter_period')
Row(keyspace_name='hospital_occupancy', type='table', name='patient_admissions_by_city_period')
Row(keyspace_name='hospital_occupancy', type='table', name='patient_admissions_by_country_period')
Row(keyspace_name='hospital_occupancy', type='table', name='patient_admissions_by_state_period')
Row(keyspace_name='hospital_occupancy', type='table', name='patients')
Row(keyspace_name='hospital_occupancy', type='table', name='rooms')
"""