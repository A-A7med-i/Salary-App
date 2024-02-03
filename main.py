import streamlit as st


class Main:
    def __init__(self):
        '''
        init method have the title and icon of the main page 
        sidebar to access the another page
        '''
        
        self.url = 'https://th.bing.com/th/id/R.9b10375327b01187d506b3e5b190c7e3?rik=FnHOlPBNq0ug5w&pid=ImgRaw&r=0'
        self.width = 680
        self.mess = 'Select The Page'


        st.set_page_config(page_title="Salary App" , page_icon="🌐")
        st.balloons()
        st.image(self.url , width = self.width )
        st.sidebar.success(self.mess)        



if __name__ == '__main__':
    Main()