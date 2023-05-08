import sqlite3


# Создание базы данных и таблиц
def create_database():
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    # Вставьте здесь SQL-запросы, предоставленные вами, для создания таблиц и индексов, а также добавления начальных данных

    # Создание таблиц и индексов
    table_creation_queries = [
        """
        CREATE TABLE Clients (
            id_client INTEGER PRIMARY KEY,
            surname VARCHAR(50),
            name VARCHAR(50),
            patronymic VARCHAR(50),
            number VARCHAR(15),
            address VARCHAR(100),
            email VARCHAR(100)
        );
        """,

        """
        CREATE TABLE Cars (
            id_car INTEGER PRIMARY KEY,
            brand VARCHAR(50),
            model VARCHAR(50),
            year INTEGER,
            vin VARCHAR(17),
            id_client INTEGER,
            FOREIGN KEY (id_client) REFERENCES Clients (id_client)
        );
        """,

        """
        CREATE TABLE Orders (
            id_order INTEGER PRIMARY KEY,
            id_client INTEGER,
            id_car INTEGER,
            date_create DATE,
            status VARCHAR(20),
            amount DECIMAL(10, 2),
            FOREIGN KEY (id_client) REFERENCES Clients (id_client),
            FOREIGN KEY (id_car) REFERENCES Cars(id_car)
        );
        """,

        """
        CREATE TABLE Services (
            id_service INTEGER PRIMARY KEY,
            name_service VARCHAR(100),
            cost_service DECIMAL(10, 2)
        );
        """,

        """
        CREATE TABLE Orders_services (
            id_order INTEGER,
            id_service INTEGER,
            count_service INTEGER,
            cost_services DECIMAL(10, 2),
            PRIMARY KEY (id_order, id_service),
            FOREIGN KEY (id_order) REFERENCES Orders (id_order),
            FOREIGN KEY (id_service) REFERENCES Services(id_service)
        );
        """,

        """
        CREATE TABLE Spares(
            id_spare INTEGER PRIMARY KEY,
            name VARCHAR(100),
            article VARCHAR(20),
            count INTEGER,
            cost DECIMAL(10, 2)
        );
        """,

        """
        CREATE TABLE Works(
            id_work INTEGER PRIMARY KEY,
            id_order INTEGER,
            id_mech INTEGER,
            id_spare INTEGER,
            date_start DATE,
            date_end DATE,
            during TIME,
            cost DECIMAL(10, 2),
        FOREIGN KEY (id_order) REFERENCES Orders(id_order),
        FOREIGN KEY (id_mech) REFERENCES Employees(id_employee),
        FOREIGN KEY (id_spare) REFERENCES Spares(id_spare)
        );
        """,

        """
        CREATE TABLE Employees(
        id_employee INTEGER PRIMARY KEY,
        surname VARCHAR(50),
        name VARCHAR(50),
        patronymic VARCHAR(50),
        number VARCHAR(15),
        address VARCHAR(100),
        position VARCHAR(50),
        salary DECIMAL(10, 2),
        date_hire DATE
        );
        """,
        """
        CREATE INDEX idx_cars_vin ON Cars (vin);
        """,
        """
        CREATE INDEX idx_orders_date_create ON Orders(date_create);
        """,
        """
        CREATE INDEX idx_orders_status ON Orders(status);
        """,
        """
        CREATE INDEX idx_orders_date_start ON Works (date_start);
        """,
        """
        CREATE INDEX idx_works_date_end ON Works (date_end);
        """
    ]

    initial_data_queries = [
        """
        INSERT INTO Clients VALUES (1, 'Иванов', 'Иван', 'Иванович', '+79991234567', 'г. Москва, ул. Пушкина, д. 1', 'ivanov@example.com');
        """,
        """
        INSERT INTO Clients VALUES (2, 'Петров', 'Петр', 'Петрович', '+79997654321', 'г. Москва, ул. Ленина, д. 2', 'petrov@example.com');
        """,
        """
            INSERT INTO Cars VALUES (1, 'Lada', 'Vesta', 2018, 'XTA211230J0000001', 1);
        """,
        """
            INSERT INTO Cars VALUES (2, 'Toyota', 'Camry', 2015, '4T1BF1FK0FU000001', 2);
        """,
        """
            INSERT INTO Orders VALUES (1, 1, 1, '2023-01-01', 'В работе', 0);
        """,
        """
            INSERT INTO Orders VALUES (2, 2, 2, '2023-01-10', 'Завершен', 15000);
        """,
        """
            INSERT INTO Services VALUES (1, 'Замена масла', 1000);
        """,
        """
            INSERT INTO Services VALUES (2, 'Замена фильтра', 500);
        """,
        """
            INSERT INTO Services VALUES (3, 'Замена тормозных колодок', 3000);
        """,
        """
            INSERT INTO Orders_services VALUES (1, 1, 1, 1000);
        """,
        """
            INSERT  INTO Orders_services VALUES (1, 2, 1, 500);
        """,
        """
            INSERT INTO Orders_services VALUES (2, 1, 1, 1000);
        """,
        """
            INSERT INTO Orders_services VALUES (2, 3, 1, 3000);
        """,
        """
            -- Добавление запасных частей
            INSERT INTO Spares VALUES (1, 'Масло моторное', '12345678', 100, 500);
        """,
        """
            INSERT INTO Spares VALUES (2, 'Фильтр масляный', '87654321', 50, 300);
        """,
        """
            INSERT INTO Spares VALUES (3, 'Тормозные колодки передние', '23456789', 30, 2000);
        """,
        """
            -- Добавление сотрудников
            INSERT INTO Employees VALUES (1, 'Сидоров', 'Сидор', 'Сидорович', '+79993332211', 'г. Москва, ул. Кирова, д. 3', 'Механик', 30000, '2021-05-01');
        """,
        """
            INSERT INTO Employees VALUES (2, 'Алексеев', 'Алексей', 'Алексеевич', '+79994445566', 'г. Москва, ул. Советская, д. 4', 'Менеджер', 40000, '2021-06-01');
        """,
        """
            -- Добавление работ
            INSERT INTO Works VALUES (1, 1, 1, 1, '2023-01-01', '2023-01-01', '02:00:00', 2000);
        """,
        """
            INSERT INTO Works VALUES (2, 2, 1, 2, '2023-01-10', '2023-01-10', '01:00:00', 1000);
        """,
        """
            INSERT INTO Works VALUES (3, 2, 1, 3, '2023-01-10', '2023-01-10', '03:00:00', 4000);
        """,
        """
            CREATE TABLE Branches(
                id_branch INTEGER PRIMARY KEY,
                name VARCHAR(100),
                address VARCHAR(100));
        """,
        """
            -- Добавление филиалов
            INSERT INTO Branches(id_branch, name, address) VALUES (1, 'Центральное производство', 'г. A, ул. Главная, д. 123');
        """,
        """
            INSERT INTO Branches(id_branch, name, address) VALUES (2, 'Филиал 1', 'г. B, ул. Первая, д. 456');
        """,
        """
            INSERT INTO Branches(id_branch, name, address) VALUES (3, 'Филиал 2', 'г. C, ул. Вторая, д. 789');
        """
    ]

    for query in table_creation_queries:
        cursor.execute(query)
    for query in initial_data_queries:
        cursor.execute(query)
    conn.commit()
    conn.close()


create_database()
