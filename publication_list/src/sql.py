def select(
    columns: list[str], 
    table: str, 
    condition: str = None, 
    ordering: str = None,
    distinct: bool = False) -> str:

    query = "SELECT "

    # distinct
    if distinct:
        query = query+"DISTINCT "

    # columns
    if len(columns) == 0:
        query = query+"*"
    else:
        query = query+columns[0]
        for col in columns[1:]:
            query = query+", "+col

    # table
    query = query+"\nFROM "+table

    # condition
    if condition is not None:
        query = query+"\nWHERE "+condition

    # ordering
    if ordering is not None:
        query = query+"\nORDER BY "+ordering

    return query

def innerJoin(
    left_table: str, 
    left_column: str, 
    right_table: str, 
    right_column: str) -> str:

    return left_table+"\nINNER JOIN "+right_table+"\nON "+left_table+"."+left_column+"="+right_table+"."+right_column

# def create(
#     temp: str,
#     selection: str) -> str:

#     return "CREATE TABLE #"+temp+" AS\n"+selection



