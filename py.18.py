# Program to check a simple SQL query

def check_sql(query):
    query = query.strip().upper()

    sql_commands = ["SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", "DROP"]

    if not query.endswith(";"):
        return "Invalid SQL: Missing semicolon (;)"

    first_word = query.split()[0]

    if first_word not in sql_commands:
        return "Invalid SQL: Unknown command"

    return "SQL query appears to be valid"

# Input from user
query = input("Enter SQL query: ")

result = check_sql(query)
print(result)