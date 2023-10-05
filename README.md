# XML2CSV

## extract fuel consumption from SUMO emssion.xml file to a CSV file/ calculate the total fuel consumption / fuel consumption to a plot.\
to run the code run the command "**sh run.sh**".\
this project is an example of extracting data from an .xml emission files of a SUMO simulation.\
the extracted data are stored on the CSV files.\


# Fuel Consumption Analysis Script

This Python script is designed for analyzing fuel consumption data. It performs the following tasks:

1. **Data Preparation**: Reads input data files containing vehicle fuel consumption data.

2. **Total Fuel Consumption Calculation**: Calculates the total fuel consumption for each time step and stores the results in output CSV files.

3. **Fuel Consumption Visualization**: Generates plots to visualize fuel consumption data for different vehicle models.

## Usage

To use this script, follow these steps:

1. **Install Dependencies**:

Make sure you have the necessary Python libraries installed. You can install them using pip:

     ```bash
     pip install pandas pandas_datareader matplotlib numpy

4. **Data Preparation**:

Prepare input data files containing vehicle fuel consumption data. The script assumes these files are in CSV format.
Update the file paths in the script to point to your input data files.

2. **Run the Script**:

Execute the Python script using your preferred Python interpreter:

    ```bash
    python fuel_consumption.ipynb
View the Results:

The script will calculate the total fuel consumption and save the results in output CSV files ("fuelwith.csv" and "fuelwithout.csv").
It will also generate a plot ("fuel_consumption.png") comparing fuel consumption between different vehicle models.
Dependencies
The script relies on the following Python libraries:

pandas: Used for data manipulation and analysis.
pandas_datareader: Used for reading data from various online sources (optional).
matplotlib: Used for creating data visualizations.
numpy: Used for numerical operations.
Example Output
The script will generate a plot (fuel_consumption.png) that compares fuel consumption between a conventional model and an adaptive model. The plot provides insights into fuel consumption patterns over time.

Fuel Consumption Plot

Author
[Your Name]
License
This script is licensed under the MIT License.

