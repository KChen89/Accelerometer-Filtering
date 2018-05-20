'''
3D accelerometer draw
@author: Kemeng Chen
'''
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from util import* 

def test_data(file_name):
	cur_dir=os.getcwd()
	fs=512
	file_path=os.path.join(cur_dir, 'data', file_name)
	data=read_data(file_path, [1,2,3])
	plot_lines(data, fs)
	fft_plot(data, fs)
	f_data=median_filter(data, 155)
	plot_lines(f_data, fs)
	fft_plot(f_data, fs)
	plot3D(data)
	plot3D(f_data)
	plt.show()

if __name__ == '__main__':
	if len(sys.argv)<2:
		raise ValueError('No file name specified')
	test_data(sys.argv[1])