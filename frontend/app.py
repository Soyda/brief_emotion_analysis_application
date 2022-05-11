import streamlit as st 
import requests


def main():
    
    st.title("Emotion prediction")
    x = requests.get('http://host.docker.internal:8000/test')
    st.write(x.json()["message"])



                    
if __name__ == '__main__':
    main()