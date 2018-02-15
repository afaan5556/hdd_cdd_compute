# hdd_cdd_compute
This Python script reads TMY files stored in a relative path folder and computes the HDD and CDD for each file. It then uses the bokeh.py library to visualize the results.

## Data required
* TMY files

## Variables
* `DIRECTORY` is a variable that stores the relative path of location of the the TMY files.
* `BASE` is the base temperature used to calculate HDD and CDD in degrees celcius. 

## Use
Place the script files in a folder relative to the TMY files per the `DIRECTORY` variable

Running the script in a terminal should print out the Station (City + State), HDD, CDD, and TDD (total degree days) and generate an html plot.