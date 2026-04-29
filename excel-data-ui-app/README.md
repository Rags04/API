# Excel Data UI App

This project is a web application that allows users to fetch and display data from an Excel sheet using a user-friendly interface. The application is structured into two main components: a backend API built with Flask and a frontend user interface built with React.

## Project Structure

```
excel-data-ui-app
├── backend
│   ├── src
│   │   ├── api.py          # Flask API for handling requests
│   │   └── excel_utils.py  # Utility functions for reading Excel files
│   ├── requirements.txt     # Python dependencies for the backend
│   └── README.md            # Documentation for the backend
├── frontend
│   ├── src
│   │   ├── App.js           # Main entry point for the React application
│   │   ├── components
│   │   │   └── DataTable.js # Component for displaying data in a table
│   │   └── api
│   │       └── fetchData.js # Functions for making API calls
│   ├── package.json         # npm configuration for the frontend
│   └── README.md            # Documentation for the frontend
└── README.md                # Overview of the entire project
```

## Getting Started

### Prerequisites

- Python 3.x
- Node.js and npm

### Backend Setup

1. Navigate to the `backend` directory.
2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
3. Run the Flask API:
   ```
   python src/api.py
   ```

### Frontend Setup

1. Navigate to the `frontend` directory.
2. Install the required npm packages:
   ```
   npm install
   ```
3. Start the React application:
   ```
   npm start
   ```

## Usage

Once both the backend and frontend are running, you can access the application in your web browser. The frontend will allow you to fetch data from the Excel sheet through the API provided by the backend.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License.