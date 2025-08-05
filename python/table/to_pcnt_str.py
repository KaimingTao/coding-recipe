
def to_pcnt_str(table, pcnt_col):
    [
        i.update({pcnt_col: f"{round(i[pcnt_col] * 100)}%"})
        for i in table
    ]

    return table
