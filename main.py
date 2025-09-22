import streamlit as st

import utils

utils.page_settings()

def main():
    st.title("✅ ToDo List")
    st.caption("Esvazie sua mente com as tarefas a fazer neste lugar e veja um novo mundo...")

    task = st.text_input("Digite o nome da tarefa")
    submit = st.button("Adicionar Tarefa", type="primary")

    if submit:
        if task == "":
            st.warning("Por favor, certifique-se de ter preenchido o campo de tarefa!")
        elif len(task) <= 0 or len(task) >= 100:
            st.warning("O nome da tarefa deve ter entre 0 a 100 caracteres, certifique-se que sua tarefa tenha menos que isso.")
        else:
            old_data = utils.read_database()
            if task in old_data:
                st.toast("Esta tarefa já foi adicionada!", icon="⚠️", duration="long")
            else:
                old_data.append(task)
                utils.write_database(old_data)

                st.toast(f"Tarefa '{task}' adicionada com sucesso!", icon="✅")

    utils.open_database()


main()
