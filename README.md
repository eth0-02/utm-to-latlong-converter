# UTM to Latitude/Longitude Converter

## Overview

This repository contains a Python script designed to convert UTM (Universal Transverse Mercator) coordinates into latitude and longitude.

## Requirements

- **Python 3.x**
- **pyproj library**

Install the necessary library using pip:

```sh
pip install pyproj
Usage
Step 1: Clone the Repository
sh
Copy code
git clone https://github.com/yourusername/utm-to-latlong-converter.git
Step 2: Navigate to the Repository Folder
sh
Copy code
cd utm-to-latlong-converter
Step 3: Run the Script
sh
Copy code
python utm_to_latlong.py
Step 4: Modify the Script (Optional)
Open the utm_to_latlong.py file in a text editor.
Update the values of easting, northing, zone_number, and zone_letter with your UTM coordinates.
Save the file and run the script again.
Step 5: Using the Output in GIS Software
ArcGIS Pro:

Open your map view.
Use the "Go To XY" tool and enter the latitude and longitude values.
QGIS:

Open your QGIS project.
Use the "Coordinate Capture" tool to input the latitude and longitude.
Example
Easting: 339374
Northing: 9959921
Zone Number: 37
Zone Letter: S
Running the script will output:

mathematica
Copy code
Latitude: -0.365196, Longitude: 37.557491
Contributing
Feel free to contribute by submitting issues or pull requests.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any inquiries, reach out via email: your.email@example.com.
