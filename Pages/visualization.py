import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


class Visualization:
    def __init__(self):
        '''
        init method have 
        call the uploade method to return the data
        4 expander
        '''

        st.set_page_config(page_title = "Visualization" , page_icon = "📊")
        self.path = 'F:\SalaryApp\Data\ds_salaries.csv'
        self.df = self.uploadeData()
        
        self.numerical = self.df.select_dtypes(include = np.number).columns.to_list()
        self.categorical = self.df.select_dtypes(exclude = np.number).columns.to_list()

        self.showScatterExpander()
        self.showHistogramExpander()
        self.showBarExpander()
        self.showPieExpander()



    @st.cache_data
    def uploadeData(_self):
        '''
        This method is return the data for increase the performance
        '''
        return pd.read_csv(_self.path)
    



    def showScatterExpander(self):
        '''
        have the expander of scatter plot
        '''
        
        with st.expander('Scatter Configuration'):
            self.configureScatter()
    



    def configureScatter(self):
        '''
        This method is about scatter plot
        You have the freedom to choose the row and the column
        and can comparing with each column
        '''

        self.col1 , self.col2 , self.col3 = st.columns(3)
        with self.col1:
            self.xAxis = st.selectbox("Select the x axis : " , self.numerical ,index = 0)
        with self.col2:
            self.yAxis = st.selectbox("Select the y axis : " , self.numerical , index = 2)
        with self.col3:
            self.color = st.selectbox("Select color : " , self.df.columns , index = 1)

        self.fig = px.scatter(self.df , self.xAxis , self.yAxis , color = self.color)
        st.plotly_chart(self.fig , theme = 'streamlit' , use_container_width = True)




    def showHistogramExpander(self):
        '''
        have the expander of Histogram plot
        '''

        with st.expander("Histogram Configuration"):
            self.configureHistogram()



    def configureHistogram(self):
        '''
        This method is about histogram plot
        You have the freedom to choose the x axis
        '''

        self.color = '#9467bd'
        self.x_axis = st.selectbox("Select the x-axis:", self.df.columns, index = 6)

        self.fig = px.histogram(self.df, x = self.x_axis , color_discrete_sequence = [self.color])
        st.plotly_chart(self.fig,theme = 'streamlit' ,use_container_width = True)



        
    def showBarExpander(self):
        '''
        have the expander of Bar plot
        '''

        with st.expander('Bar Configuration'):
            self.configureBar()




    def configureBar(self):
        '''
        This method is about bar plot
        You have the freedom to choose the row and the column
        and can comparing with each column
        '''

        self.col1 , self.col2 , self.col3 = st.columns(3)
        with self.col1:
            self.x_axis = st.selectbox("Choose X axis : " , self.df.columns ,index = 0)
        with self.col2:
            self.y_axis = st.selectbox("Choose Y axis : " , self.df.columns , index = 4)
        with self.col3:
            self.colors = st.selectbox("Choose Color : " , self.df.columns , index = 1)

        self.fig = px.bar(self.df , x = self.x_axis , y = self.y_axis , color = self.colors , barmode = 'group')
        st.plotly_chart(self.fig , theme = 'streamlit' , use_container_width = True)




    def showPieExpander(self):
        '''
        have the expander of Pie plot
        '''

        with st.expander('Pie Configuration'):
            self.configurePie()




    def configurePie(self):
        '''
        This method is about pie plot
        You have the freedom to choose the row and the column
        and can comparing with each column
        '''

        self.col1 , self.col2 , self.col3 = st.columns(3)
        with self.col1:
            self.name = st.selectbox("Select Name : " , self.categorical ,index = 0)
        with self.col2:
            self.value = st.selectbox("Select Value : " , self.numerical , index = 2)

        self.fig = px.pie(self.df , names = self.name , values = self.value )
        st.plotly_chart(self.fig , theme = 'streamlit' , use_container_width = True)



Visualization()