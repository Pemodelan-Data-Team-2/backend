COPY hospital_occupancy.carecenters (care_center_id, care_center_name, address) FROM 'carecenters.csv'
    WITH DELIMITER=',' AND HEADER=TRUE;

COPY hospital_occupancy.carecenters_by_city (city, care_center_id, care_center_name, address) FROM 'carecenters_by_city.csv'
    WITH DELIMITER=',' AND HEADER=TRUE;

COPY hospital_occupancy.carecenters_by_state (state, care_center_id, care_center_name, address) FROM 'carecenters_by_state.csv'
    WITH DELIMITER=',' AND HEADER=TRUE;

COPY hospital_occupancy.carecenters_by_country (country, care_center_id, care_center_name, address) FROM 'carecenters_by_country.csv'
    WITH DELIMITER=',' AND HEADER=TRUE;

COPY hospital_occupancy.rooms (room_id, room_type, care_center_id, rate) FROM 'rooms.csv'
    WITH DELIMITER=',' AND HEADER=TRUE;

COPY hospital_occupancy.rooms_by_carecenter (care_center_id, room_id, room_type, rate) FROM 'rooms_by_carecenter.csv'
    WITH DELIMITER=',' AND HEADER=TRUE; # file rooms_by_carecenter GA ADA

COPY hospital_occupancy.rooms_by_carecenter (room_id, room_type, care_center_id, rate) FROM 'rooms.csv'
    WITH DELIMITER=',' AND HEADER=TRUE; # alt

COPY hospital_occupancy.beds (bed_id, care_center_id, room_id) FROM 'beds.csv' 
    WITH DELIMITER=',' AND HEADER=TRUE;

COPY hospital_occupancy.beds_by_room (room_id, bed_id, care_center_id) FROM 'beds_by_room.csv'
    WITH DELIMITER=',' AND HEADER=TRUE;

COPY hospital_occupancy.patients (patient_id, mrn, first_name, last_name, gender, contact, dob, address, is_resident_patient) FROM 'patients.csv'
    WITH DELIMITER=',' AND HEADER=TRUE;

COPY hospital_occupancy.patient_admissions (admission_id, patient_id, bed_id, room_id, care_center_id, admitted_date, discharged_date, admitted_causes, room_rate_per_night, room_rate_total) FROM 'patient_admissions.csv'
    WITH DELIMITER=',' AND HEADER=TRUE;

COPY hospital_occupancy.patient_admissions_by_room (room_id, admission_id, patient_id, bed_id, care_center_id, admitted_date, discharged_date, admitted_causes, room_rate_per_night, room_rate_total) FROM 'patient_admissions_by_room.csv'
    WITH DELIMITER=',' AND HEADER=TRUE;

COPY hospital_occupancy.patient_admissions_by_carecenter (care_center_id, admission_id, patient_id, bed_id, room_id, admitted_date, discharged_date, admitted_causes, room_rate_per_night, room_rate_total) FROM 'patient_admissions_by_carecenter.csv'
    WITH DELIMITER=',' AND HEADER=TRUE;

COPY hospital_occupancy.patient_admissions_by_city (city, admission_id, patient_id, bed_id, room_id, care_center_id, admitted_date, discharged_date, admitted_causes, room_rate_per_night, room_rate_total) FROM 'patient_admissions_by_city.csv'
    WITH DELIMITER=',' AND HEADER=TRUE;

COPY hospital_occupancy.patient_admissions_by_state (state, admission_id, patient_id, bed_id, room_id, care_center_id, admitted_date, discharged_date, admitted_causes, room_rate_per_night, room_rate_total) FROM 'patient_admissions_by_state.csv'
    WITH DELIMITER=',' AND HEADER=TRUE;

COPY hospital_occupancy.patient_admissions_by_country (country, admission_id, patient_id, bed_id, room_id, care_center_id, admitted_date, discharged_date, admitted_causes, room_rate_per_night, room_rate_total) FROM 'patient_admissions_by_country.csv'
    WITH DELIMITER=',' AND HEADER=TRUE;

