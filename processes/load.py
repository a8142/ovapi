import sqlite3
from datetime import datetime


def get_connection(db_path: str) -> sqlite3.Connection:
    return sqlite3.connect(db_path)


def create_table(cursor):
    query = """
    CREATE TABLE IF NOT EXISTS line (
    DataOwnerCode VARCHAR(255) NOT NULL,
    LinePlanningNumber VARCHAR(255) NOT NULL,
    LineDirection INT NOT NULL,
    LinePublicNumber VARCHAR(255),
    LineName VARCHAR(255),
    DestinationName50 VARCHAR(255),
    DestinationCode VARCHAR(255),
    LineWheelchairAccessible VARCHAR(255),
    TransportType VARCHAR(255),
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    deleted_at TIMESTAMP,
    PRIMARY KEY(DataOwnerCode, LinePlanningNumber, LineDirection)
    );
    """
    cursor.execute(query)


def insert_into_table(cursor: sqlite3.Cursor, line_data: dict):

    current_ts = f"'{datetime.now()}'"

    columns = [column for column in line_data.keys()] + ["created_at", "updated_at"]
    columns_str = ", ".join(columns)

    # workaround for ' in one of the values
    values = []
    for value in line_data.values():
        if isinstance(value, str):
            values.append(f"""'{value.replace("'", "")}'""")
        else:
            values.append(f"'{value}'")
    values.extend([current_ts, current_ts])
    values_str = ", ".join(values)

    update_str = ", ".join([f"{column} = excluded.{column}" for column in columns if column != "created_at"])

    query = f"""
        INSERT INTO line ({columns_str})
        VALUES ({values_str})
        ON CONFLICT (DataOwnerCode, LinePlanningNumber, LineDirection) DO UPDATE
        SET {update_str}
        WHERE excluded.updated_at > line.updated_at
        ;
    """
    cursor.execute(query)
