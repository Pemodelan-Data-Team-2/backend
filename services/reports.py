import sys
sys.path.append('../')

import repositories.beds as beds_repo
import repositories.carecenters as carecenters_repo
import repositories.patient_admissions as patient_admissions_repo
import repositories.patients as patients_repo
import repositories.rooms as rooms_repo

import pandas as pd
import numpy as np

class CountryReports(object):
    def __init__(self, country):
        self.country = country

    def rooms_by_carecenter(self, care_center_id=None):
        df = rooms_repo.rooms_by_carecenter(country=self.country, care_center_id=care_center_id)
        return df

    def beds_by_room(self, room_id=None):
        df = beds_repo.beds_by_room(country=self.country,room_id=room_id)
        return df

    def carecenters_by_city(self, city=None):
        df = carecenters_repo.carecenters_by_city(country=self.country, city=city)
        return df

    def carecenters_by_state(self, state=None):
        df = carecenters_repo.carecenters_by_state(country=self.country, state=state)
        return df

    def carecenters_by_country(self):
        df = carecenters_repo.carecenters_by_country(country=self.country)
        return df

    def patient_admissions_by_carecenter(self, care_center_id=None):
        df = patient_admissions_repo.patient_admissions_by_carecenter(country=self.country, care_center_id=care_center_id)
        return df

    def patient_admissions_by_room(self, room_id=None):
        df = patient_admissions_repo.patient_admissions_by_room(country=self.country, room_id=room_id)
        return df

    def patient_admissions_by_city(self, city=None):
        df = patient_admissions_repo.patient_admissions_by_city(country=self.country, city=city)
        return df

    def patient_admissions_by_state(self, state=None):
        df = patient_admissions_repo.patient_admissions_by_state(country=self.country, state=state)
        return df

    def patient_admissions_by_country(self):
        df = patient_admissions_repo.patient_admissions_by_country(country=self.country)
        return df

    ## PATIENT ADMISSIONS REVENUES REPORTS

    def format_json_linechart(self,df):
        """
        fungsi ini digunakan untuk mengconvert format dataframe menjadi format
        inputan javascript untuk plot linechart
        """
        output = {"id" : self.country}
        data = []
        column = list(df.columns)
        for i in range(len(df)):
            data.append({"x":str(df[column[0]][i]),
                          "y":df[column[1]][i]})
        output["data"] = data
        return output

    def patient_admissions_revenues_per_annum(self, df):
        """
        Function to generate annual report
        Args:
        - df: pandas.DataFrame -> queried data (prefix: patient_admissions_by_....).
            E.g., patient_admissions_by_country, patient_admissions_by_state, etc.
        """
        df['admitted_date'] = pd.to_datetime(df['admitted_date'])
        df['year'] = df['admitted_date'].dt.year
        agg = df.groupby('year',as_index = False)[['room_rate_total']].sum()
        agg = agg.rename(columns={'room_rate_total':'total_revenues'})
        return self.format_json_linechart(agg)

    def patient_admissions_revenues_per_month(self, df, year):
        """
        Function to generate monthly report
        Args:
        - df: pandas.DataFrame -> queried data (prefix: patient_admissions_by_....).
            E.g., patient_admissions_by_country, patient_admissions_by_state, etc.
        - year: int -> year of interest
        """
        df['admitted_date'] = pd.to_datetime(df['admitted_date'])
        df = df[df['admitted_date'].dt.year==year]
        df['month'] = df['admitted_date'].dt.month
        agg = df.groupby('month',as_index = False)[['room_rate_total']].sum()
        agg = agg.rename(columns={'room_rate_total':'total_revenues'})
        return self.format_json_linechart(agg)

    def patient_admissions_revenues_per_quarter(self, df, year):
        """
        Function to generate quarterly report
        Args:
        - df: pandas.DataFrame -> queried data (prefix: patient_admissions_by_....).
            E.g., patient_admissions_by_country, patient_admissions_by_state, etc.
        - year: int -> year of interest
        """
        df['admitted_date'] = pd.to_datetime(df['admitted_date'])
        df = df[df['admitted_date'].dt.year==year]
        df['quarter'] = df['admitted_date'].dt.quarter
        agg = df.groupby('quarter',as_index = False)[['room_rate_total']].sum()
        agg = agg.rename(columns={'room_rate_total':'total_revenues'})
        return self.format_json_linechart(agg)

    ## PATIENT ADMISSIONS REPORT

    def patient_admissions_per_annum(self, df):
        """
        Function to generate annual report
        Args:
        - df: pandas.DataFrame -> queried data (prefix: patient_admissions_by_....).
            E.g., patient_admissions_by_country, patient_admissions_by_state, etc.
        """
        df['admitted_date'] = pd.to_datetime(df['admitted_date'])
        df['year'] = df['admitted_date'].dt.year
        agg = df.groupby('year',as_index = False)[['admission_id']].count()
        agg = agg.rename(columns={'admission_id':'total_admitted_patients'})
        return agg

    def patient_admissions_per_month(self, df, year):
        """
        Function to generate monthly report
        Args:
        - df: pandas.DataFrame -> queried data (prefix: patient_admissions_by_....).
            E.g., patient_admissions_by_country, patient_admissions_by_state, etc.
        - year: int -> year of interest
        """
        df['admitted_date'] = pd.to_datetime(df['admitted_date'])
        df = df[df['admitted_date'].dt.year==year]
        df['month'] = df['admitted_date'].dt.month
        agg = df.groupby('year',as_index = False)[['admission_id']].count()
        agg = agg.rename(columns={'admission_id':'total_admitted_patients'})
        return agg

    def patient_admissions_per_quarter(self, df, year):
        """
        Function to generate quarterly report
        Args:
        - df: pandas.DataFrame -> queried data (prefix: patient_admissions_by_....).
            E.g., patient_admissions_by_country, patient_admissions_by_state, etc.
        - year: int -> year of interest
        """
        df['admitted_date'] = pd.to_datetime(df['admitted_date'])
        df = df[df['admitted_date'].dt.year==year]
        df['quarter'] = df['admitted_date'].dt.quarter
        agg = df.groupby('year',as_index = False)[['admission_id']].count()
        agg = agg.rename(columns={'admission_id':'total_admitted_patients'})
        return agg

    def revenues_by_state_per_annum(self,df):
        """
        function to generate report revenue per year by state
        """
        df['admitted_date'] = pd.to_datetime(df['admitted_date'])
        df['year'] = df['admitted_date'].dt.year
        agg = df.groupby(['year','state'],as_index = False)[['room_rate_total']].sum()
        agg = agg.rename(columns={'room_rate_total':'total_revenues'})
        return self.format_json_table(agg)

    def patient_admission_by_state_per_year(self,df):
        df['admitted_date'] = pd.to_datetime(df['admitted_date'])
        df['year'] = df['admitted_date'].dt.year
        agg = df.groupby(['year','state'],as_index = False)[['admission_id']].count()
        agg = agg.rename(columns={'admission_id':'total_admitted_patients'})
        return self.format_json_table(agg)

    #untuk tampilan tabel
    def format_json_table(self,df):
        """
        format_json fangsi digunakna untuk mengubah format dataframe ke bentuk inputan
        javascript.
        """
        output = []
        df["Country"] = self.country
        columns = list(df.columns)
        for i in range(len(df)):
            output.append(df.iloc[i].to_dict())
        return output

    ## DEPRECATED

    # def revenues_from_patient_admissions_per_annum(self):
    #     df = self.patient_admissions_by_country()
    #     df['admitted_date'] = pd.to_datetime(df['admitted_date'])
    #     df['year'] = df['admitted_date'].dt.year
    #     agg = df.groupby('year')[['room_rate_total']].sum()
    #     agg.rename(columns={'room_rate_total':'total_revenues'})
    #     return agg

    # def revenues_from_patient_admissions_per_month(self, year):
    #     df = self.patient_admissions_by_country()
    #     df['admitted_date'] = pd.to_datetime(df['admitted_date'])
    #     df = df[df['admitted_date'].dt.year==year]
    #     df['month'] = df['admitted_date'].dt.month
    #     agg = df.groupby('month')[['room_rate_total']].sum()
    #     agg.rename(columns={'room_rate_total':'total_revenues'})
    #     return agg

    # def revenues_from_patient_admissions_per_quarter(self, year):
    #     df = self.patient_admissions_by_country()
    #     df['admitted_date'] = pd.to_datetime(df['admitted_date'])
    #     df = df[df['admitted_date'].dt.year==year]
    #     df['quarter'] = df['admitted_date'].dt.quarter
    #     agg = df.groupby('quarter')[['room_rate_total']].sum()
    #     agg.rename(columns={'room_rate_total':'total_revenues'})
    #     return agg

    # def admitted_patients_per_annum(self):
    #     df = self.patient_admissions_by_country()
    #     df['admitted_date'] = pd.to_datetime(df['admitted_date'])
    #     df['year'] = df['admitted_date'].dt.year
    #     agg = df.groupby('year')[['admission_id']].count()
    #     agg.rename(columns={'admission_id':'total_admitted_patients'})
    #     return agg

    # def admitted_patients_per_month(self, year):
    #     df = self.patient_admissions_by_country()
    #     df['admitted_date'] = pd.to_datetime(df['admitted_date'])
    #     df = df[df['admitted_date'].dt.year==year]
    #     df['month'] = df['admitted_date'].dt.month
    #     agg = df.groupby('month')[['admission_id']].count()
    #     agg.rename(columns={'admission_id':'total_admitted_patients'})
    #     return agg

    # def admitted_patients_per_quarter(self, year):
    #     df = self.patient_admissions_by_country()
    #     df['admitted_date'] = pd.to_datetime(df['admitted_date'])
    #     df = df[df['admitted_date'].dt.year==year]
    #     df['quarter'] = df['admitted_date'].dt.quarter
    #     agg = df.groupby('quarter')[['admission_id']].count()
    #     agg.rename(columns={'admission_id':'total_admitted_patients'})
    #     return agg
