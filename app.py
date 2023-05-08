import sqlite3
import pandas as pd
import streamlit as st


# Функции для выполнения операций с базой данных
def execute_query(query, params=()):
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()


def select_data(query, params=()):
    conn = sqlite3.connect("my_database.db")
    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    return df


def main():
    st.title("Мое автосервисное приложение")

    # Выбор раздела
    section = st.sidebar.selectbox(
        "Выберите раздел",
        ("Филиалы", "Клиенты", "Автомобили", "Заказы")
    )

    if section == "Филиалы":
        st.header("Филиалы")
        branches = select_data("SELECT * FROM Branches")
        st.table(branches)
    elif section == "Клиенты":
        st.header("Клиенты")
        clients = select_data("SELECT * FROM Clients")
        st.table(clients)
    elif section == "Автомобили":
        st.header("Автомобили")
        cars = select_data("SELECT * FROM Cars")
        st.table(cars)
    elif section == "Заказы":
        st.header("Заказы")
        orders = select_data("SELECT * FROM Orders")
        st.table(orders)


if __name__ == "__main__":
    main()
