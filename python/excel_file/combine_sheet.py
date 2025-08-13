import pandas as pd


def combine_sheets(excel_file_path, with_header=True):
    excel = pd.ExcelFile(excel_file_path)

    sheet_names = excel.sheet_names
    print("Sheet names:", sheet_names)

    dfs = []

    for sheet in sheet_names:
        if not with_header:
            df = pd.read_excel(excel, sheet_name=sheet, header=None)
            # df.columns = ['Country', 'Number']
        else:
            df = pd.read_excel(excel, sheet_name=sheet)
        df['SheetName'] = sheet

        dfs.append(df)

    return pd.concat(dfs, ignore_index=True)
