# Backend API for Excel Data UI App

This README provides instructions for setting up and using the backend of the Excel Data UI application.

## Overview

The backend is built using Flask and provides an API for fetching data from Excel sheets. It includes endpoints for retrieving data and handles errors related to file access.

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd excel-data-ui-app/backend
   ```

2. **Create a virtual environment (optional but recommended):**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the Flask API:**
   ```
   python src/api.py
   ```

   The API will be available at `http://localhost:5000`.

## API Endpoints

- **GET /api/data**
  - Fetches data from the specified Excel sheet.
  - Returns the data in JSON format.

### Error Handling

The API includes basic error handling for file access issues. If the Excel file cannot be found or read, a relevant error message will be returned.

## Additional Information

For more details on the utility functions used to read Excel files, refer to `src/excel_utils.py`.