# Bridge Cost Comparison Tool

This project is a PyQt5-based GUI application that allows users to compare the costs of constructing and maintaining steel and concrete bridges. It integrates a SQLite database to store cost-related factors and provides a visualization of the cost breakdown.

## Features

- **Cost Estimation:** Calculates construction, maintenance, repair, demolition, environmental, social, and user costs for steel and concrete bridges.
- **Database Management:** Allows users to update the database with new cost values.
- **Graphical Visualization:** Displays cost comparisons in a bar chart using Matplotlib.
- **Export Options:** Save cost comparisons as PNG images and PDF reports.

## Installation

### Prerequisites
Ensure you have Python 3 installed and the following dependencies:

``` bash
pip install -r requirements.txt
```

### Running the Application
1. Clone or download the repository.
2. Run the following command to start the application:

``` bash
python main.py
```

## Project Structure
├── bridge_costs.db # SQLite database (auto-generated)  
├── database.py # Handles database operations  
├── gui.py # GUI implementation using PyQt5  
├── main.py # Entry point for the application  
├── README.md # Project documentation (this file)  


## Usage
1. **Enter Bridge Parameters**
   - Span Length (m)
   - Width (m)
   - Traffic Volume (vehicles/day)
   - Design Life (years)

2. **Calculate Costs**
   - Click "Calculate Costs" to compare steel and concrete bridges.

3. **Update Database**
   - Click "Update Database" to modify cost parameters.

4. **Export Data**
   - Export results as a PNG image or PDF report.