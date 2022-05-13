import streamlit as st 
import requests
import datetime

URL_API = "http://host.docker.internal:8000"

def main():
    
    st.title("Emotion prediction")
    x = requests.get('http://host.docker.internal:8000/test')
    st.write(x.json()["message"])

# create user
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

# Create a note for a patient
def create_note(user_id, note):
    note_data = {
        "user_id": user_id,
        "note_content": note,
        "date": datetime.date.today().strftime("%d/%m/%Y"),
        "note_sentiment":"TEST_SENTIMENT"
    }
    requests.post(f"{URL_API}/users/{user_id}/notes/", json=note_data)
    
# Return all notes of a patient
def get_notes(user_id):  
    return requests.get(f"{URL_API}/users/{user_id}/notes/").json()

# get one note from a patient
def get_note(user_id, id):  
    return requests.get(f"{URL_API}/users/{user_id}/notes/{id}").json()

# Modify note of the day NOT TESTED YET
def modify_note(user_id, id, new_note):
    today = datetime.date.today().strftime("%d/%m/%Y")
    note_to_modify = get_note(user_id, id)
    if note_to_modify["date"] == today:
        modified_note = {
            # "id": id,
            "user_id": user_id,
            "note_content": new_note,
            # "date":today,
            "note_sentiment":"TEST_SENTIMENT"
        }
        return requests.patch(f"{URL_API}/users/{user_id}/notes/{id}", json=modified_note)
    else :
        st.write("You can't modify a former note")


            
create_user(True, "Mister ZEN", "1234")
create_user(False, "Patient", "1234")

x = requests.get(f"{URL_API}/users")
st.write(x.json())

current_user = x.json()[0]["id"]
y = requests.get(f"{URL_API}/users/{current_user}")
st.write("You are logged as " + y.json()["username"])

patient_id = x.json()[1]["id"]
patient_info = requests.get(f"{URL_API}/users/{patient_id}")
st.write("You are logged as " + patient_info.json()["username"])

note = "Today is a good day"
create_note(patient_id, note)
st.write(get_notes(patient_id))

user_id = 2
id = 15
st.write("test note by id")
st.write(get_note(user_id, id))

# st.write("tet modify note above")
# new_note="I'm a modified note !"
# modify_note(user_id,id,new_note)
# st.write("display modified note")
# st.write(get_note(user_id, id))



if __name__ == '__main__':
    main()