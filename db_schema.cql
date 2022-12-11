CREATE KEYSPACE hospital_occupancy WITH REPLICATION = 
    {'class': 'SimpleStrategy', 'replication_factor': 3};

CREATE TYPE hospital_occupancy.address (
    street TEXT, 
    city TEXT, 
    state_or_province TEXT, 
    zip_code TEXT, 
    country TEXT);

CREATE TABLE hospital_occupancy.carecenters (
    care_center_id TEXT PRIMARY KEY, 
    care_center_name TEXT, 
    address frozen<address>) 
    WITH COMMENT = 'Find information about a care center';

CREATE TABLE hospital_occupancy.carecenters_by_city (
    city text, 
    care_center_id text, 
    care_center_name text, 
    address frozen<address>, 
    PRIMARY KEY ((city), care_center_id)) 
    WITH COMMENT = 'Find care centers by city'
    ADD CLUSTERING ORDER BY (care_center_id ASC);

CREATE TABLE hospital_occupancy.carecenters_by_state (
    state text, 
    care_center_id text, 
    care_center_name text, 
    address frozen<address>, 
    PRIMARY KEY ((city), care_center_id)) 
    WITH COMMENT = 'Find care centers by state'
    ADD CLUSTERING ORDER BY (care_center_id ASC);

CREATE TABLE hospital_occupancy.carecenters_by_country (
    country text, 
    care_center_id text, 
    care_center_name text, 
    address frozen<address>, 
    PRIMARY KEY ((city), care_center_id)) 
    WITH COMMENT = 'Find care centers by country'
    ADD CLUSTERING ORDER BY (care_center_id ASC);

CREATE TABLE hospital_occupancy.rooms (
    room_id text PRIMARY KEY,
    room_type TEXT,
    care_center_id TEXT,
    occupancy_status TEXT,
    rate DOUBLE)
    WITH COMMENT = 'Find information about a room';

CREATE TABLE hospital_occupancy.available_rooms_by_carecenter_date (
    care_center_id TEXT,
    date_oi date,
    room_id TEXT,
    room_type TEXT,
    occupancy_status TEXT,
    rate DOUBLE,
    PRIMARY KEY ((care_center_id), date_oi, room_id))
    WITH COMMENT = 'Find available rooms by care center and date';

CREATE TABLE hospital_occupancy.beds (
    bed_id TEXT PRIMARY KEY, 
    room_id TEXT, 
    care_center_id TEXT, 
    is_occupied BOOLEAN) 
    WITH COMMENT = 'Find information about a bed';

CREATE TABLE hospital_occupancy.available_beds_by_room (
    room_id TEXT,
    bed_id TEXT,
    care_center_id TEXT,
    is_occupied BOOLEAN,
    PRIMARY KEY ((room_id), bed_id))
    WITH COMMENT = 'Find available beds by room'
    ADD CLUSTERING ORDER BY (bed_id ASC);

CREATE TABLE hospital_occupancy.patients (
    patient_id TEXT PRIMARY KEY,
    mrn TEXT,
    first_name TEXT,
    last_name TEXT,
    contact TEXT,
    dob date,
    address frozen<address>,
    is_resident_patient BOOLEAN)
    WITH COMMENT = 'Find information about a patient';

CREATE TABLE hospital_occupancy.patient_admissions (
    admission_id TEXT PRIMARY KEY,
    patient_id TEXT,
    bed_id TEXT,
    room_id TEXT,
    care_center_id TEXT,
    admitted_date date,
    discharged_date date,
    admitted_causes TEXT,
    room_rate_per_night DOUBLE,
    room_rate_total DOUBLE)
    WITH COMMENT = 'Find information about a patient admission';

CREATE TABLE hospital_occupancy.patient_admissions_by_carecenter_period (
    care_center_id TEXT,
    period_start date,
    period_end date,
    admission_id TEXT,
    patient_id TEXT,
    bed_id TEXT,
    room_id TEXT,
    admitted_date date,
    discharged_date date,
    admitted_causes TEXT,
    room_rate_per_night DOUBLE,
    room_rate_total DOUBLE,
    PRIMARY KEY ((care_center_id), period_start, period_end, admission_id))
    WITH COMMENT = 'Find patient admissions by care center and period';

CREATE TABLE hospital_occupancy.patient_admissions_by_city_period (
    city TEXT,
    period_start date,
    period_end date,
    admission_id TEXT,
    patient_id TEXT,
    bed_id TEXT,
    room_id TEXT,
    care_center_id TEXT,
    admitted_date date,
    discharged_date date,
    admitted_causes TEXT,
    room_rate_per_night DOUBLE,
    room_rate_total DOUBLE,
    PRIMARY KEY ((city), period_start, period_end, admission_id))
    WITH COMMENT = 'Find patient admissions by city and period';

CREATE TABLE hospital_occupancy.patient_admissions_by_state_period (
    state TEXT,
    period_start date,
    period_end date,
    admission_id TEXT,
    patient_id TEXT,
    bed_id TEXT,
    room_id TEXT,
    care_center_id TEXT,
    admitted_date date,
    discharged_date date,
    admitted_causes TEXT,
    room_rate_per_night DOUBLE,
    room_rate_total DOUBLE,
    PRIMARY KEY ((state), period_start, period_end, admission_id))
    WITH COMMENT = 'Find patient admissions by state and period';

CREATE TABLE hospital_occupancy.patient_admissions_by_country_period (
    country TEXT,
    period_start date,
    period_end date,
    admission_id TEXT,
    patient_id TEXT,
    bed_id TEXT,
    room_id TEXT,
    care_center_id TEXT,
    admitted_date date,
    discharged_date date,
    admitted_causes TEXT,
    room_rate_per_night DOUBLE,
    room_rate_total DOUBLE,
    PRIMARY KEY ((country), period_start, period_end, admission_id))
    WITH COMMENT = 'Find patient admissions by country and period';
