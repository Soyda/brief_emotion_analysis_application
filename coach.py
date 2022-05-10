import streamlit as st
import pandas as pd

#DATA A MODIFIER AVEC SQLITE/POSTGRE
data = pd.read_csv('emotion_kaggle.csv')

#MASKS
mask_year = mask_month = mask_day = pd.Series(True, index=data.index)
choice_year = choice_month = choice_day = False

class Coach():

    def __init__(self, username):
        self.username = username


    def manage_users(self):

        st.subheader("En cours...")


    def read_diary(self):

        
        #CRITERE ANNEE
        year_list = [2018,2019,2020,2021,2022]
        data_filtered = st.container()
        year_choosen = st.selectbox(
            'Année : ',
            (year_list)
            )
        with data_filtered :
            mask_year = data['Year'].str.contains(year_choosen)
            choice_year = True
        
        result_year = data[mask_year]

        #CRITERE MOIS

        month_list = ['Janvier', 'Février', 'Mars', 'Avril','Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
        data_filtered = st.container()
        month_choosen = st.selectbox(
                    'Mois : ',
                    (month_list),
                )
        with data_filtered :
            mask_month = data['Month'].str.contains(month_choosen)
            choice_month = True

        result_month = data[mask_month]


        #CRITERE JOUR
        day_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
        data_filtered = st.container()
        day_choosen = st.selectbox(
                    'Jour : ',
                    (day_list),
                )
        with data_filtered :
            mask_day = data['Day'].str.contains(day_choosen)
            choice_day = True

        result_day = data[mask_day]

    
    def see_feeling(self):

        
        #CRITERE ANNEE
        year_list = [2018,2019,2020,2021,2022]
        data_filtered = st.container()
        year_choosen = st.selectbox(
            'Année : ',
            (year_list)
            )
        with data_filtered :
            mask_year = data['Year'].str.contains(year_choosen)
            choice_year = True
        
        result_year = data[mask_year]

        #CRITERE MOIS

        month_list = ['Janvier', 'Février', 'Mars', 'Avril','Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
        data_filtered = st.container()
        month_choosen = st.selectbox(
                    'Mois : ',
                    (month_list),
                )
        with data_filtered :
            mask_month = data['Month'].str.contains(month_choosen)
            choice_month = True

        result_month = data[mask_month]


        #CRITERE JOUR
        day_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
        data_filtered = st.container()
        day_choosen = st.selectbox(
                    'Jour : ',
                    (day_list),
                )
        with data_filtered :
            mask_day = data['Day'].str.contains(day_choosen)
            choice_day = True

        result_day = data[mask_day]

    
    def page(self):

        #---OPTIONS COACH---
        if st.checkbox("GESTION DES PATIENTS"):
            self.manage_users()

        if st.checkbox("LIRE L'EXTRAIT DU JOURNAL INTIME D'UN PATIENT"):
            self.read_diary()

        if st.checkbox("VOIR LES EMOTIONS D'UN PATIENT"):
            self.see_feeling()
        