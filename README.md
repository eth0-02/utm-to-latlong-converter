## UTM to Latitude/Longitude Converter

This repository contains a Python script designed to convert UTM (Universal Transverse Mercator) coordinates into latitude and longitude.

## Requirements

* **Python 3.x**
* **pyproj library**

Install the necessary library using pip:

```sh
pip install pyproj
Use code with caution.

Usage
This script provides two ways to convert UTM coordinates: using pre-defined values or your own custom values.

Using Default Values
Clone the Repository:

Bash
git clone [https://github.com/yourusername/utm-to-latlong-converter.git](https://github.com/yourusername/utm-to-latlong-converter.git)
Use code with caution.

Navigate to the Repository Folder:

Bash
cd utm-to-latlong-converter
Use code with caution.

Run the Script:

Bash
python utm_to_latlong.py
Use code with caution.

This will run the script using pre-defined UTM coordinates and display the converted latitude and longitude.

Using Custom Values
Follow steps 1 and 2 from the "Using Default Values" section.

Modify the Script (Optional):

Open the utm_to_latlong.py file in a text editor. Update the values of the following variables with your UTM coordinates:

easting
northing
zone_number
zone_letter
Save the file and run the Script again:

Bash
python utm_to_latlong.py
Use code with caution.

This will run the script with your custom UTM coordinates and display the converted latitude and longitude.

Using the Output in GIS Software
The output latitude and longitude can be used in GIS software like ArcGIS or QGIS to locate the specific point on a map.

Here's an example for each software:

ArcGIS Pro:

Open your map view.
Use the "Go To XY" tool and enter the latitude and longitude values obtained from the script output.
QGIS:

Open your QGIS project.
Use the "Coordinate Capture" tool to input the latitude and longitude values obtained from the script output.
Example
If you have UTM coordinates like:

Easting: 339374
Northing: 9959921
Zone Number: 37
Zone Letter: S
Running the script with these default values will output:

Latitude: -0.365196, Longitude: 37.557491
Contributing
Feel free to contribute by submitting issues or pull requests to improve this script.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any inquiries regarding this script, reach out via email: your.email@example.com
