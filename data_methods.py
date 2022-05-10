
import streamlit as st
import pandas as pd
import sqlite3
from sqlite3 import Connection


class Data():

    def init_db_users(conn: Connection):
        URI_SQLITE_DB = "users_notes.db"
        conn = Data.get_connection(URI_SQLITE_DB)

        conn.execute(
            """CREATE TABLE IF NOT EXISTS Users
                (
                    user_id INT PRIMARY KEY NOT NULL,
                    is_admin BOOL,
                    username VARCHAR(50),
                    password VARCHAR(50)
                );"""
        )
        conn.commit()

    def init_db_notes(conn: Connection):
        URI_SQLITE_DB = "users_notes.db"
        conn = Data.get_connection(URI_SQLITE_DB)

        conn.execute(
            """CREATE TABLE IF NOT EXISTS Notes
                (
                    note_id INT PRIMARY KEY NOT NULL,
                    user_id INT,
                    date DATE,
                    note_content VARCHAR(300),
                    note_sentiment VARCHAR(30)
                );"""
        )
        conn.commit()

    def get_admin_rights(username, hashed_password):
        URI_SQLITE_DB = "users_notes.db"
        conn = Data.get_connection(URI_SQLITE_DB)
        
        is_admin = pd.read_sql("SELECT * FROM Users", con=conn)
        return is_admin

    def get_all_users(Users):
        user_list=[]
        for info in Users.query.all():
            user_list.append(info)
        return user_list

    def get_content(user_id):
        URI_SQLITE_DB = "users_notes.db"
        conn = Data.get_connection(URI_SQLITE_DB)
        
        content = pd.read_sql("SELECT * FROM Notes", con=conn)
        return content

        
    @st.cache(hash_funcs={Connection: id})
    def get_connection(path: str):
        """Put the connection in cache to reuse if path does not change between Streamlit reruns.
        NB : https://stackoverflow.com/questions/48218065/programmingerror-sqlite-objects-created-in-a-thread-can-only-be-used-in-that-sa
        """
        return sqlite3.connect(path, check_same_thread=False)
