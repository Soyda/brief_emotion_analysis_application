import streamlit as st 
import requests

URL_API = "http://host.docker.internal:8000"

def main():
    
    st.title("Emotion prediction")
    x = requests.get('http://host.docker.internal:8000/test')
    st.write(x.json()["message"])


def post_text(username, text):
    text_data = {
        "note": text,
        "user_username": username
    }
    response = requests.post(f"{URL_API}/text", json=text_data)

def create_user(is_admin, username, password):
    infos = {
        "is_admin": is_admin,
        "username": username,
        "password": password
    }
    response = requests.post(f"{URL_API}/users", json=infos)
    if response.status_code == 200:
        return f"Successfully created {infos['username']}"
    else:
        return "Can't create this user"
                    
            
create_user(True, "Mister ZEN", "1234")

x = requests.get(f"{URL_API}/users")
st.write(x.json())

current_user = x.json()[0]["id"]
y = requests.get(f"{URL_API}/users/{current_user}")
st.write("You are logged as " + y.json()["username"])



if __name__ == '__main__':
    main()