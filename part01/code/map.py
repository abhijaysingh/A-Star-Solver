import numpy as np
from matplotlib import patches
import matplotlib.pyplot as plt
import matplotlib.path as mplPath

class Map:
    """
    The map class.
    """

    def __init__(self, width : int = 600, height : int = 200):
        """
        Initialize the map with the given width, height, and clearance.

        Parameters
        ----------
        width : int, optional
            The width of the map, by default 600
        height : int, optional
            The height of the map, by default 250
        """
        self.width = width
        self.height = height

        self.map = np.zeros((width, height))
        self.workspace = mplPath.Path(np.array([(0, 0), [width-1, 0], [width-1, height-1], [0, height-1], [0, 0]]))

    def set_clearance_radius(self, clearance : int) -> None:
        self._radius = 10
        self.clearance = clearance + self._radius
        self._set_obstacles()

    def _set_obstacles(self):
        """
        Set the obstacles on the map.
        """
        for i in range(self.width):
            for j in range(self.height):
                try:
                    if i < self.clearance or i >= (self.width - self.clearance) or j < self.clearance or j >= (self.height - self.clearance):
                        self.map[i][j] = 1
                        
                    if (i >= (150 - self.clearance)) and (i <= (165 + self.clearance)) and (j <= (125 + self.clearance)) and (j >= 0):
                        self.map[i][j] = 1

                    if (i >= (250 - self.clearance)) and (i <= (265 + self.clearance)) and (j >= (75 - self.clearance)) and (j <= self.height):
                        self.map[i][j] = 1

                    if ((i-400)**2 + (j-90)**2 <= (50 + self.clearance)**2):
                        self.map[i][j] = 1
                except Exception:
                    print(Exception)
                    
    def _is_obstacle(self, i, j):
        """
        Check if the given state is an obstacle.

        Parameters
        ----------
        i : int
            The x coordinate of the state.
        j : int
            The y coordinate of the state.

        Returns
        -------
        bool
            True if the state is an obstacle, False otherwise.
        # """

        if i < self.clearance or i >= (self.width - self.clearance) or j < self.clearance or j >= (self.height - self.clearance):
            return True
                        
        if (i >= (150 - self.clearance)) and (i <= (165 + self.clearance)) and (j >= (75 - self.clearance)) and (j <= self.height):
            return True
        
        if (i >= (250 - self.clearance)) and (i <= (265 + self.clearance)) and (j >= 0) and (j <= (125 + self.clearance)):
            return True
        
        if ((i-400)**2 + (j-110)**2 <= (50 + self.clearance)**2):
            return True

    def _is_in_bounds(self, x, y):
        """
        Check if the given state is in bounds.

        Parameters
        ----------
        x : int
            The x coordinate of the state.
        y : int
            The y coordinate of the state.

        Returns
        -------
        bool
            True if the state is in bounds, False otherwise.
        """
        return x >= 0 and x < self.width and y >= 0 and y < self.height

    def is_valid(self, x, y):
        """
        Check if the given position is valid.

        Parameters
        ----------
        x : int
            The x coordinate of the position.
        y : int
            The y coordinate of the position.

        Returns
        -------
        bool
            True if the position is valid, False otherwise.
        """
        return self._is_in_bounds(x, y) and not self._is_obstacle(x, y)
    
    def plot_map(self):
        """
        Plot the map.

        Returns
        -------
        fig, ax
            The figure and axis of the plot.
        """
        fig, ax = plt.subplots(subplot_kw={'aspect': 'auto'}, dpi=250)

        ws_verts = self.workspace.vertices
        plt.plot(ws_verts[:,0],ws_verts[:,1], color='y', linewidth=5)
        self.plot_obstacles(ax)

        return fig, ax
    
    def plot_obstacles(self, ax):
        """
        Plot the obstacles on the map.

        Parameters
        ----------
        ax : axis
            The axis to plot the obstacles on.
        """
        rect1 = [[150 - self.clearance, 75 - self.clearance], [165 + self.clearance, 75 - self.clearance], [165 + self.clearance, self.height], [150 - self.clearance, self.height]]
        e = patches.Polygon(xy=rect1)
        ax.add_artist(e)
        e.set_facecolor('y')

        rect2 = [[250 - self.clearance, 0], [250 - self.clearance, 125 + self.clearance], [265 + self.clearance, 125 + self.clearance], [265 + self.clearance, 0]]
        e = patches.Polygon(xy=rect2)
        ax.add_artist(e)
        e.set_facecolor('y')

        circle = plt.Circle((400, 110), 50 + self.clearance, color='y')
        ax.add_artist(circle)