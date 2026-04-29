import pandas as pd

def read_excel(file_path, sheet_name=0):
    try:
        data = pd.read_excel(file_path, sheet_name=sheet_name)
        return data
    except Exception as e:
        return {"error": str(e)}

def get_column_data(file_path, column_name, sheet_name=0):
    try:
        data = read_excel(file_path, sheet_name)
        if isinstance(data, pd.DataFrame):
            if column_name in data.columns:
                return data[column_name].tolist()
            else:
                return {"error": f"Column '{column_name}' does not exist."}
        return data
    except Exception as e:
        return {"error": str(e)}