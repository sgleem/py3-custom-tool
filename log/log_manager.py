import numpy as np
import torch

class LogManager:
    """
    LogManager has these features
    - crawl all stat value
    - calculate mean value
    - save history
    """
    def __init__(self):
        self.log_book=dict()
        self.history=dict()
    ########################################################
    def alloc_stat_type(self, stat_type):
        """ add stat-type """
        self.log_book[stat_type] = []
        self.history[stat_type] = []
    def alloc_stat_type_list(self, stat_type_list):
        """ add stat-type in stat-type list """
        for stat_type in stat_type_list:
            self.alloc_stat_type(stat_type)
    def init_stat(self):
        """ initialize each statistics """
        for stat_type in self.log_book.keys():
            self.log_book[stat_type] = []
    def save_to_history(self):
        """ save current stat to history """
        for stat_type in self.log_book.keys():
            stat = self.get_stat(stat_type)
            self.history[stat_type].append(stat)
        self.init_stat()
    ########################################################

    ########################################################
    def add_stat(self, stat_type, stat):
        """ add stat to stat_type """
        assert stat_type in self.log_book, "Wrong stat type"
        assert isinstance(stat, int) or isinstance(stat, float), "Wrong stat value"
        
        self.log_book[stat_type].append(stat)
    def add_torch_stat(self, stat_type, stat_tensor):
        """ extract tensor value, then add-stat """
        stat = stat_tensor.item.detach().cpu().item()
        self.add_stat(stat_type, stat)
    ########################################################
    
    def get_stat(self, stat_type):
        """
        1. crawl all stat value
        2. calculate mean value
        3. return rounded mean value
        """
        result_stat = 0
        stat_list = self.log_book[stat_type]
        if len(stat_list) != 0:
            result_stat = np.mean(stat_list)
            result_stat = np.round(result_stat, 4)
        return result_stat
    
    def get_all_stat(self):
        """
        get all stat value in stat book
        """
        all_stat=dict()
        for stat_type in self.log_book.keys():
           stat = self.get_stat(stat_type)
           all_stat[stat_type] = stat
        return all_stat

    def print_stat(self):
        """
        print all stat value in stat book
        """
        all_stat = self.get_all_stat()
        for stat_type, stat in all_stat.items():
           print(stat_type,":",stat, end=' / ')
    
    def get_history(self):
        """ get current histroy """
        return self.history
