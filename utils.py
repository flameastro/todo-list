import streamlit as st
import json
import os

def page_settings():
    st.set_page_config (
    page_title = "ToDo List",
    page_icon = "assets/icon.png",
    layout = "centered"
)


def read_database():
    """Lê o banco de dados JSON e retorna uma lista de tarefas"""
    if not os.path.exists("database/data.json"):
        return []

    with open("database/data.json", "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []
    return data


def write_database(data):
    """Escreve a lista de tarefas no banco"""
    with open("database/data.json", "w") as f:
        json.dump(data, f, indent=4)


def open_database():
    data = read_database()
    for e in data:
        st.checkbox(e)
