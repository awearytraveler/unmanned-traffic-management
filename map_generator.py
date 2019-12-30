import numpy as np 
import scipy as sp 
import matplotlib

GRID_SIZE = 100
CITY_DENSITY = 0.8 # Density of the city between 0 and 1, where 0 is plain land and 1 is a cyberpunk future city
HEIGHT_DENSITY = 35 # 
class Grid:

    def __init__(self, city_density=CITY_DENSITY, grid_size=GRID_SIZE):
        
        self.size = (grid_size,grid_size)
        self.grid = np.zeros(self.size)
        self.city_density = city_density
        self.heights = np.zeros(self.size)

    def populate(self):

        self.grid = np.random.normal(0,1,size=self.size)
        self.heights = np.random.normal(35,1,size=self.size)
        self.grid = self.grid*(self.grid<(1-self.city_density))
        


a = Grid()
