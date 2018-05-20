'''
3D accelerometer filtering with median and low pass filter
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
	cutoff=10
	file_path=os.path.join(cur_dir, 'data', file_name)
	data=read_data(file_path, [1,2,3])
	plot_lines(data, fs, 'Raw data')
	fft_plot(data, fs, 'Raw data')
	median_data=median_filter(data, 155)
	lpf_data=freq_filter(data, 155, cutoff/fs)
	comb_data=freq_filter(median_data, 155, cutoff/fs)
	plot_lines(median_data, fs, 'median filter')
	plot_lines(lpf_data, fs, 'low pass filter')
	plot_lines(comb_data, fs, 'median+low pass filter')
	fft_plot(lpf_data, fs, 'low pass filter')
	fft_plot(median_data, fs, 'median filter')
	fft_plot(comb_data, fs, 'median+low pass filter')
	plot3D(data, 'raw data')
	plot3D(median_data, 'median filter')
	plot3D(lpf_data, 'low pass filter')
	plot3D(comb_data, 'median+low pass filter')
	plt.show()

if __name__ == '__main__':
	if len(sys.argv)<2:
		raise ValueError('No file name specified')
	test_data(sys.argv[1])