import pandas as pd
from bokeh.io import show, output_file
from bokeh.plotting import figure, show, output_file

extract_data = pd.read_csv('hdd_cdd.csv')

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