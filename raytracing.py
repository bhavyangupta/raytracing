#!/usr/bin/python

"""
Implementation of the Bresenham algorithm to get the coordinates
of the cells along a line on a grid

References:
http://eugen.dedu.free.fr/projects/bresenham/
https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm
http://www.phatcode.net/res/224/files/html/ch35/35-01.html#Heading1

"""

import math
import matplotlib.pyplot as plt
import numpy as np

class Grid():
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.grid = np.ones(shape = dimensions)

    def bresenhamCalculateGridCells(self, start, end):
        print ("coordinates")
        print(start, end)
        cell_coordinates = []
        x_start = float(start[0])
        x_end = float(end[0])
        y_start = float(start[1])
        y_end = float(end[1])

        slope = ((y_end - y_start) / (x_end - x_start))
        y = y_start;
        error = 0

        for x in range(int(x_start), int(x_end), 1):
            function_value = (slope * (x - x_start)) + y_start

            error += slope

            if (error > 0.5):
                y = y + (np.sign(y_end - y_start) * 1)
                error -= 1.0

            #print(error, y)

            cell_coordinates.append((int(x), int(y)))

        return cell_coordinates

    def viewLine(self, start, end):
        delta_x = end[0] - start[0]
        delta_y = end[1] - start[1]

        swapped = False
        if (delta_y > delta_x):
            swapped = True
    
        fig = plt.figure()
        ax = fig.add_subplot(111)
        #if swapped:
        plt.plot([start[1], end[1]], [start[0], end[0]], 'ob')
        #else:
        #    plt.plot([start[0], end[0]], [start[1], end[1]], 'ob')
        if swapped:
            temp = start[1]
            start = (start[0], end[1])
            end = (end[0], temp)

        cell_coordinates = self.bresenhamCalculateGridCells(start, end)

        print (cell_coordinates)

        for coordinate in cell_coordinates:
            #if swapped:
            self.grid[coordinate[0], coordinate[1]] = 0
            #else:
            #    self.grid[coordinate[1], coordinate[0]] = 0

        plt.imshow(self.grid, cmap='gray')
        plt.xlabel('X')
        plt.ylabel('Y')
        ax.xaxis.set_ticks(np.arange(0, self.dimensions[0], 1))
        ax.yaxis.set_ticks(np.arange(0, self.dimensions[1], 1))
        plt.grid(True)
        plt.show()

if __name__ == '__main__':
    start_pt = (10, 75)
    end_pt = (20, 10)
    grid = Grid((100, 100))
    grid.viewLine(start_pt, end_pt)
