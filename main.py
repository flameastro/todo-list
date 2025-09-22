import streamlit as st
import json
import os

import utils

utils.page_settings()


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


def main():
    st.title("✅ ToDo List")
    st.caption("Esvazie sua mente com as tarefas a fazer neste lugar e veja um novo mundo...")

    task = st.text_input("Digite o nome da tarefa")
    submit = st.button("Adicionar Tarefa", type="primary")

    if submit:
        if task == "":
            st.warning("Por favor, certifique-se de ter preenchido o campo de tarefa!")
        else:
            old_data = read_database()
            if task in old_data:
                st.toast("Esta tarefa já foi adicionada!", icon="⚠️", duration="long")
            else:
                old_data.append(task)
                write_database(old_data)

                st.toast(f"Tarefa '{task}' adicionada com sucesso!", icon="✅")

    open_database()


main()
