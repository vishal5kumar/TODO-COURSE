def get_schema(table_name, cursor):
    GET_SCHEMA = f"SELECT sql from sqlite_schema where name = '{table_name}'"
    query = ""
    data = cursor.execute(GET_SCHEMA)
    for i in data:
        query = i[0]
    return query
