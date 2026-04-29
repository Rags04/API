# Excel Data UI App

This project is a web application that allows users to fetch and display data from an Excel sheet using a user-friendly interface. The application is divided into two main components: the backend and the frontend.

## Project Structure

```
excel-data-ui-app
├── backend
│   ├── src
│   │   ├── api.py          # Flask API for handling requests
│   │   └── excel_utils.py  # Utility functions for reading Excel files
│   ├── requirements.txt     # Dependencies for the backend
│   └── README.md            # Documentation for the backend
├── frontend
│   ├── src
│   │   ├── App.js           # Main entry point for the React application
│   │   ├── components
│   │   │   └── DataTable.js # Component for displaying data in a table
│   │   └── api
│   │       └── fetchData.js # Functions for API calls to the backend
│   ├── package.json         # Configuration for the frontend
│   └── README.md            # Documentation for the frontend
└── README.md                # Overview of the entire project
```

## Frontend Setup

1. Navigate to the `frontend` directory:
   ```
   cd frontend
   ```

2. Install the required dependencies:
   ```
   npm install
   ```

3. Start the development server:
   ```
   npm start
   ```

## Backend Setup

1. Navigate to the `backend` directory:
   ```
   cd backend
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Flask API:
   ```
   python src/api.py
   ```

## Usage

- The frontend application will allow users to interact with the API to fetch data from the Excel sheet.
- The data will be displayed in a table format, providing an easy way to view and analyze the information.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.