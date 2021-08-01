from __future__ import print_function
import numpy as np

grid = [['.','.','.','.','.','.'],
	['.','O','O','.','.','.'],
	['O','O','O','O','.','.'],
	['O','O','O','O','O','.'],
	['.','O','O','O','O','O'],
	['O','O','O','O','O','.'],
	['O','O','O','O','.','.'],
	['.','O','O','.','.','.'],
	['.','.','.','.','.','.']]

# determine list shape
nRow, nCol = np.shape(grid)
#print(nRow, nCol)

# using naive method  
# to print list vertically
for i in range(nCol):
	for x in grid:
		print(x[i], end =' ')
	print()
	
gridTranspose = np.array(grid).T.tolist()

nRow, nCol = np.shape(gridTranspose)
#print(nRow, nCol)

for i in range(nCol):
	for x in gridTranspose:
		print(x[i], end =' ')
	print()
