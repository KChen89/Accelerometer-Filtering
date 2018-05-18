'''
utility function to read data, integration, and plot
@author: Kemeng Chen
'''

import os
import sys
import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def read_data(file_path, columns):
	'''
	read files according to file_path and columns
	args:
		file_path, columns (list)
	return:
		data (numpy array)
	'''
	if not os.path.isfile(file_path):
		raise AssertionError(file_path, 'not found')
	mode='r'
	with open (file_path, mode) as f:
		lines=f.readlines()
		num_rows=len(lines)
		print(str(num_rows), ' rows')
		num_cols=len(columns)
		data=np.zeros([num_rows, num_cols])
		for indice, line in enumerate(lines[3:]):
			row=line.rstrip().split('\t')
			# print(row)
			for ii, i in enumerate(columns):
				data[indice,ii]=row[i]
		data[:,0]-=np.mean(data[:,0], axis=0)
		data[:,1]-=np.mean(data[:,1], axis=0)
		data[:,2]-=np.mean(data[:,2], axis=0)
	f.close()
	return data

def plot_lines(data):
	num_rows, num_cols=data.shape
	if num_cols!=3:
		raise ValueError('Not 3D data')
	fig, ax=plt.subplots()
	labels=['x','y','z']
	color_map=['r', 'g', 'b']
	for i in range(num_cols):
		ax.plot(data[:,i], color_map[i], label=labels[i])
	ax.set_xlim([0,num_rows])
	ax.set_xlabel('Time')
	ax.legend()

def acc_integration(data):
	num_rows, num_cols=data.shape
	int_data=np.zeros(data.shape)
	for i in range(num_cols):
		int_data[:,i]=TZ_integration(data[:,i])
	return int_data

def plot3D(data):
	fig=plt.figure()
	ax=fig.add_subplot(111, projection='3d')
	ax.plot(xs=data[:,0], ys=data[:,1], zs=data[:,2], zdir='z')

def TZ_integration(in_signal):
	lgth=in_signal.shape
	integral=np.zeros(lgth)
	c=0
	for indice, s in enumerate(in_signal):
		if indice==0:
			integral[indice]=c+in_signal[indice]
		else:
			integral[indice]=integral[indice-1]+in_signal[indice]
	return integral

