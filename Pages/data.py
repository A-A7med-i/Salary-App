import streamlit as st
import pandas as pd


class DataFrame:
    def __init__(self):
        '''
        init method 
        call the uploaddata
        call form method
        '''

        self.path = 'F:\SalaryApp\Data\ds_salaries.csv'
        
        st.set_page_config(page_title="Data" , page_icon="📚")
        self.df = self.uploadeData()
        self.form()


    @st.cache_data
    def uploadeData(_self):
        '''
        This method is return the data for increase the performance
        '''

        return pd.read_csv(_self.path)
    
    def write(self):
        '''
        write the data on form
        '''
        
        st.write(self.df[:self.rows][self.col])


    def form(self):
        '''
        have form to allow you to choose the number of rows and the col want to show
        and submite button to apply the above
        '''

        with st.form('Layout'):
            self.rows = st.slider('Choose The Number Of Rows', min_value = 5 , max_value = len(self.df))
            self.col = st.multiselect('Choose The Columns' , self.df.columns.to_list() , default = ['work_year' , 'job_title' , 'salary_in_usd'])
            self.submitted = st.form_submit_button("Apply")
        
        if self.submitted:
            self.write()




    

DataFrame()