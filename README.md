# Car Fuel Consumption data Analysis 

## the fuel consumption XLM files are extracted from SUMO simulation of two platoon's driving models.

# Dependencies
The script relies on the following Python libraries:

- pandas: Used for data manipulation and analysis.
- pandas_datareader: Used for reading data from various online sources.
- matplotlib: Used for creating data visualizations.
- numpy: Used for numerical operations.

# Fuel Consumption Analysis Script

This Python script is designed for analyzing fuel consumption data. It performs the following tasks:

1. **Data Preparation**:
   - Ensure that you have XML data files ready for conversion.
   - Update the script 'xml2csv.ipynb' to specify the path to the input XML data file.
   - converting data from XML format to CSV format.
   - Reads converted CSV input data files containing vehicle fuel consumption data.

2. **Total Fuel Consumption Calculation**: Calculates the total fuel consumption for each time step and stores the results in output CSV files.

3. **Fuel Consumption Visualization**: Generates plots to visualize fuel consumption data for different vehicle models.

## Usage

To use this script, follow these steps:

1. **Install Dependencies**:

Make sure you have the necessary Python libraries installed. You can install them using pip:

     ```bash
     pip install pandas pandas_datareader matplotlib numpy ElementTree


2. **Data Preparation**:

Prepare input data files containing vehicle fuel consumption data. The script assumes these files are in CSV format.
Update the file paths in the script to point to your input data files.

3. **Run the Script**:

Execute the sh script:

     ```bash
     sh run.sh
     
    
4.View the Results:

The script will :
   - convert the XML data into a CSV file and save it with the specified output filename.
   - generate converted CSV files ("emissionwith.csv" and "emissionwithout.csv") containing the converted data.
   - calculate the total fuel consumption and save the results in output CSV files ("fuelwith.csv" and "fuelwithout.csv").
   - also generate a plot ("fuel_consumption.png") comparing fuel consumption between different vehicle models.
     

# Example Output
The script will generate a plot (fuel_consumption.png) that compares fuel consumption between a conventional platoon driving model and an adaptive driving model. The plot provides insights into fuel consumption patterns over time.


Author
[JawaherCharfeddine]
License
This script is licensed under the MIT License.

