import streamlit as st
import streamlit_authenticator as stauth
from data_methods import Data
from patient import Patient
from coach import Coach

class Login():

    def page(self):

        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password")
        hashed_password = stauth.Hasher(password).generate()
        st.sidebar.button("Connexion", on_click=self.chosen_page(username, hashed_password))
       
    def chosen_page(self, username, hashed_password):
        # Récupérer le is_admin de la table Users avec get_data
        # is_admin = Data.get_admin_rights(username,hashed_password)

        # Pour tester en attendant...
        is_admin = True

        if is_admin == True :
            Coach(username).page()
        else :
            Patient(username).page()

