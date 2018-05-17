'''
3D accelerometer draw
@author: Kemeng Chen
'''
import os
import sys
import numpy as np
from util import* 

def test_data(file_name):
	cur_dir=os.getcwd()
	file_path=os.path.join(cur_dir, 'data', file_name)
	data=read_data(file_path, [1,2,3])
	plot_lines(data)

	

if __name__ == '__main__':
	if len(sys.argv)<2:
		raise ValueError('No file name specified')
	test_data(sys.argv[1])