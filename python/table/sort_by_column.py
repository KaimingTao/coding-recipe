from operator import itemgetter

def sort_by_column(table, column_names):
    return sorted(table, key=itemgetter(*column_names))
