def clean_sheet(uncleaned_sheet: list):
    """Delete all the rows that have empty cells in a spreadsheet and remove extra white-spaces."""

    cleaned_sheet = []

    for row in uncleaned_sheet:
        if ',,' in row or ',\n' in row:
            continue
        else:
            cleaned_sheet.append(row)

    return [' '.join(row.split()) + '\n' for row in cleaned_sheet]
