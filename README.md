# Unit Converter App

This is a simple unit converter web application built using Streamlit. The application allows users to convert between various units of measurement.

## Project Structure

```
├── unit-converter-app 
│   ├── main.py          # Entry point of the Streamlit application
│   └── utils
│       └── __init__.py  # Utility functions for unit conversion
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd unit-converter-app
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the unit converter application, execute the following command:

```
streamlit run main.py
```

This will start the Streamlit server and open the application in your default web browser.

## Usage

Once the application is running, you can select the units you want to convert from and to, enter the value, and click the convert button to see the result.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.
