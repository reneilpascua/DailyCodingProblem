import sys
sys.path.append('../..')
from helpers import helpers

print('''
[MEDIUM] Mar. 10, 2021
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
''')

# solution
'''
learned in physics class one time
1. consider a cartesian square with width 2R
    - x in [-R, R], y in [-R, R]
2. perfectly contained inside is a circle of radius R
    - equation x^2 + y^2 = R^2
3. randomly place a pixel anywhere within the square whose area is 4R^2
    - should be uniform
4. repeat step 3 for high N, keeping track of how many pixels fall inside the circle
    - a pixel is inside the circle if its (x, y) satisfies x^2 + y^2 < R^2 !!
    - notice the 'less than' sign
5. (number of pixels inside circle / total pixels) = (area of circle / area of square)
6. (number of pixels inside circle / total pixels) = (pi*R^2 / 4*R^2)
7. ==> pi can be approximated as 4*(n_pixelsIn / n_pixels)
'''

import random

def randomCoords(R):
    '''returns random cartesian coordinates within a square of -R to R as x, y'''
    return random.uniform(-R, R), random.uniform(-R, R)

def isInside(x, y, R):
    '''
    returns whether a point is inside an origin-centered circle of radius R

    coords: [int]   cartesian coordinates of a point
    R: int          radius of a circle centered at the origin
    '''
    return (x**2 + y**2 < R**2)

def approximatePi(N, R):
    '''
    approximates pi using N points in a square of width 2R.
    note: does R affect accuracy or precision?
    '''
    N_in = 0
    for i in range(N):
        x, y = randomCoords(R)
        if (isInside(x, y, R)): N_in+=1
    
    return 4.0*N_in/N



# run solution

# python p14_med.py 1000000 100 
# arg[1] is N, arg[2] is R (arg[0] is the script name)
print(f'pi ~ {approximatePi(int(sys.argv[1]), int(sys.argv[2])):.3f}\napproximated using {sys.argv[1]} samples')
