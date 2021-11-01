import pandas as pd

# ахахах ебало представили, если эти две фичи что-то дадут вообще?
def type_id_to_multiple_str_ids(x):
    temp_x = x.unique()
    temp_list = ['0', '0', '0', '0', '0']
    for i in range(1, 6):
        if i in temp_x:
            temp_list[i-1] = '1'
    return ''.join(temp_list)


def add_type_id_values(df):
    db_type_id_values = df.groupby(by='grid_index').agg({'type_id':[type_id_to_multiple_str_ids, 'count']})
    return df.merge(db_type_id_values.type_id, on='grid_index')