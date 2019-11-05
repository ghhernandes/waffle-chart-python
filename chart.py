import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

class WaffleChart:
    def __init__(self, x, y, width=40, height=10, color='', title=''):
        self.x = x
        self.y = y
        self.title = title
        self.width = width
        self.height = height
        self.color = color
        # wafflechart total size 
        self.total_values = sum(self.y)
        # data normalization 
        self.category_proportions = [(float(value) / self.total_values) for value in y]
        
        self.total_num_tiles = self.width * self.height
        # num of tiles per category 
        self.tiles_per_category = [round(proportion * self.total_num_tiles) 
                for proportion in self.category_proportions]

        self.waffle_array = np.zeros((self.height, self.width))
        
        self.category_index = 0
        self.tile_index = 0
        for col in range(self.width):
            for row in range(self.height):
                self.tile_index += 1

                if self.tile_index > sum(self.tiles_per_category[0: self.category_index]):
                        self.category_index += 1

                self.waffle_array[row, col] = self.category_index

        # plotting
        self.fig = plt.figure()
        colormap = plt.cm.coolwarm
        plt.matshow(self.waffle_array, cmap=colormap)
        plt.colorbar()
        
        # get the axis
        ax = plt.gca()
        # set ticks limit
        ax.set_xticks(np.arange(-.5, (self.width), 1), minor=True)
        ax.set_yticks(np.arange(-.5, (self.height), 1), minor=True)

        # add gridlines
        ax.grid(which='minor', color='w', linestyle='-', linewidth=2)

        plt.xticks([])
        plt.yticks([])

        values_cumsum = np.cumsum(self.y)
        total_values = values_cumsum[len(values_cumsum)-1]


        legend_handles = []

        for i, category in enumerate(x):
            label_str = category + ' (' + str(self.y[i]) + ')'
            color_val = colormap(float(values_cumsum[i]) / total_values)
            legend_handles.append(mpatches.Patch(color=color_val, label=label_str))

        plt.legend(handles=legend_handles,
                loc='lower center',
                ncol=len(x),
                bbox_to_anchor=(0., -0.2, 0.95, .1)
                )

        plt.title(self.title)
        plt.show()

    def version(self):
        return mpl.__version__

    def get_categories(self):
        return self.x

    def get_values(self):
        return self.y

    def get_proportions(self):
        return self.category_proportions

if __name__ == '__main__':
    chart = WaffleChart(x=['First', 'Second', 'Third'], y=np.array([1000, 3000, 5000]), title="Waffle Chart")
 
