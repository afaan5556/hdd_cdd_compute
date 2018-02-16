import pandas as pd
import os
import numpy as np
from bokeh.io import show, output_file
from bokeh.plotting import figure, show, output_file
from tmy_header_city_state_extractor import get_head

DIRECTORY = '../tmy_data/'
BASE = 18.3

# Variables to hold list data needed 
station_list, HDD_list, CDD_list = [], [], []

# Create final df needed for viz
extract_data = pd.DataFrame()

# Function to make df on any csv file
def make_df(file=str):
	return pd.read_csv(DIRECTORY + file, skiprows=1)

# Funciton to create and set hourly_CDD and hourly_HDD columns in df
def calc_hourly_HDD_CDD(df):
	df['hourly_HDD'] = np.vectorize(max)(BASE - df['Dry-bulb (C)'], [0]*len(df))
	df['hourly_CDD'] = abs(np.vectorize(min)(BASE - df['Dry-bulb (C)'], [0]*len(df)))

# Function to calc annual HDD and CDD for 1 df
def calc_HDD_CDD(df):
	HDD = int(sum(df['hourly_HDD'])/24)
	CDD = int(sum(df['hourly_CDD'])/24)
	return HDD, CDD


def main_func():
	# Walk files to:
	for roots, dirs, files in os.walk(DIRECTORY):
		for file in files:
			# 1. Call make_df func on file
			file_df = make_df(file)
			# 2. Call the calc hourly HDD and CDD on file df
			calc_hourly_HDD_CDD(file_df)
			# 3. Update file name list and get rid of the 'TYA.CSV' in each file name
			full_path = DIRECTORY + file
			station_list.append(get_head(full_path))
			i, j = calc_HDD_CDD(file_df)
			# 4. Update HDD list
			HDD_list.append(i)
			# 5. Update CDD list
			CDD_list.append(j)
	# 6. Combine series data lsits
	series_lists = [station_list, HDD_list, CDD_list]
	# 8. Create data series in final df
	for index, i in enumerate(['File', 'HDD', 'CDD']):
		extract_data[i] = pd.Series(series_lists[index])
	# Add a total HDD, CDD column to the df
	extract_data['TDD'] = extract_data['HDD'] + extract_data['CDD']

main_func()


print(extract_data)

# Set plot tools
tool_bar = ['box_zoom','pan','save', 'reset', 'wheel_zoom', 'hover', 'crosshair']

# Loop to create 3 bokeh plots (TDD ascending, HDD ascending, and CDD ascending)
for param, html_file in zip(['TDD', 'HDD', 'CDD'], ['TDD_Ascending.html', 'HDD_Ascending.html', 'CDD_Ascending.html']):
	# Sort extract_data df in place by ascending HDD, TDD, and CDD
	extract_data.sort_values([param], inplace=True)
	# Set ouput file
	output_file(html_file)
	# Create chart
	line_chart = figure(x_range=list(extract_data['File']), title='TMY Station HDD CDD Spread', x_axis_label='Station', tools=tool_bar)
	# Create data lines for chart
	for i, j in zip(['HDD', 'CDD', 'TDD'], ['#ff0000', '#0000ff', 'Black']):
		line_chart.line(list(range(0,len(extract_data[i]))), list(extract_data[i]), legend=i, color=j)
	# Set chart scaling
	line_chart.sizing_mode='scale_both'
	# Remove vertical grid lines
	line_chart.xgrid.grid_line_color = None
	# Show chart
	show(line_chart)