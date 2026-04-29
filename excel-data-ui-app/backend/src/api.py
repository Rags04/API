from flask import Flask, jsonify, request
import pandas as pd
import os

app = Flask(__name__)

# Endpoint to fetch data from the Excel file
@app.route('/api/data', methods=['GET'])
def get_data():
    file_path = 'path/to/your/excel/file.xlsx'  # Update with your Excel file path
    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404

    try:
        # Read the Excel file
        data = pd.read_excel(file_path)
        return jsonify(data.to_dict(orient='records')), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)