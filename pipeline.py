from processes.extract import get_ovapi_line_data
from processes.load import create_table, insert_into_table, get_connection
from processes.validate import validate_data

OVAPI_LINE_URL = "http://v0.ovapi.nl/line/"
DB_PATH = "/ovapi_db.sqlite"


def run_pipeline():
    connection = get_connection(DB_PATH)
    cursor = connection.cursor()

    create_table(cursor)

    ovapi_data = get_ovapi_line_data(OVAPI_LINE_URL)
    validated_data = validate_data(ovapi_data)

    for line in validated_data:
        insert_into_table(cursor, line)
    connection.commit()


if __name__ == '__main__':
    run_pipeline()
