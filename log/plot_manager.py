import matplotlib.pyplot as plt

class PlotManager:
    def __init__(self, legend=True):
        ############### option ###############
        self.legend = legend
        ######################################

        self.data = dict()
    def add_data(self, data_name, data_list):
        self.data[data_name] = data_list
    def add_data_dict(self, data_dict):
        for data_name, data_list in data_dict.items():
            self.add_data(data_name, data_list)
    
    def plot_data(self):
        plt.figure() 

        for data_name, data_list in self.data.items():
            time = [t for t in range(0, len(data_list))]
            plt.plot(time, data_list, label=data_name)

        if self.legend:
            plt.legend()
        
        plt.show()