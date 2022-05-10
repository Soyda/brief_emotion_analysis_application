import streamlit as st
import pandas as pd
from PIL import Image
from authentification import Login
from data_methods import Data


URI_SQLITE_DB = "users_notes.db"
conn = Data.get_connection(URI_SQLITE_DB)

def main():

    # #HAUT DE PAGE
    st.title("Journal intime avec Coach Zen")

    #LOGO
    img = Image.open("diary.jpg") 
    st.image(img, width=600) 

    #Initialisation des tables Users et Notes
    Data.init_db_users(conn)
    Data.init_db_notes(conn)

    #Lancement page d'accueil pour se log
    Login().page()

    
if __name__ == "__main__":
    main()