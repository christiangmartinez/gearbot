import sqlite3


def post_gear_list(gear_list: list):
    connection = None
    try:
        connection = sqlite3.connect("gear_list.db")
        cursor = connection.cursor()

        cursor.execute("""CREATE TABLE gear_list(
            name TEXT NOT NULL,
            price REAL NOT NULL, 
            link TEXT
        )""")

        table_data = []
        for item in gear_list:
            name = item["name"]
            price = item["price"]
            link = item["link"]
            table_data.append((name, price, link))

        if not table_data:
            print("No valid data exists...")

        cursor.executemany("INSERT INTO gear_list (name, price, link) VALUES (?, ?, ?)", table_data)

    except sqlite3.Error as e:
        print(f'Database error: {e}')
    
    finally:
        if connection:
            connection.close()
