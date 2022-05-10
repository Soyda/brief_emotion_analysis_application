import streamlit as st
import pandas as pd
from data_methods import Data

#DATA A MODIFIER AVEC SQLITE/POSTGRE
data = pd.read_csv('emotion_kaggle.csv')

#MASKS
mask_year = mask_month = mask_day = pd.Series(True, index=data.index)
choice_year = choice_month = choice_day = False


class Patient():

    def __init__(self, username):
        self.username = username

    def add_text(self):

        content = st.text_input("Racontez succintement votre journée...")


    def modify_text(self):

        #Montrer ce qui a été enregistré

        #Ouvrir un nouveau text_input en dessous :

        content = st.text_input("Remplacez le texte original par celui-ci...")
    
    def read_text(self):

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

        #BOUTTON DE RECHERCHE
        if st.button('Recherche !'):
            # Récupérer le content avec le current user_id
            # data = Data.get_content(user_id=current_user_id)

            #Pour tester en attendant...
            result_reading = data[mask_year & mask_month & mask_day]

            def reading():
                st.success("RESULTAT - Voici le texte concerné :")
                for text in result_reading['Text']:
                    st.write(f"{text}")

            reading()
    
    def page(self):

        #---OPTIONS PATIENT---

        if st.checkbox('Ecrire dans votre journal intime'):
            self.add_text()

        if st.checkbox('Modifier du contenu'):
            self.modify_text()

        if st.checkbox('Lire certains de vos écrits'):
            self.read_text()
        








