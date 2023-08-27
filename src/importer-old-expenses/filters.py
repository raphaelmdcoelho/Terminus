def filter_empty_rows(data):
    return [row for row in data if any(cell != '' for cell in row)]


def filter_rows_after_total(data):
    for i, row in enumerate(data):
        if row and row[0].lower() == 'total':
            return data[:i]
    return data


def apply_all_filters(data):
    data = filter_empty_rows(data)
    data = filter_rows_after_total(data)
    return data
