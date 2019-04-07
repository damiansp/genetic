import numpy as np
import pandas as pd


class DataSplitter:
    def __init__(self, filepath):
        extension = filepath.split('.')[-1]
        assert extension == 'csv', 'input data must be in csv format'
        print(f'Reading data from {filepath}...')
        self.data = pd.read_csv(filepath)
        print(f'Data has shape: {self.data.shape}')
        self.n = self.data.shape[0]
        print('n:', self.n)
        
    def split_data(self, y_col, fraction_train=0.8, shuffle=False):
        n_train = int(round(self.n * fraction_train))
        if shuffle:
            self._shuffle()
        self.train = self.data.loc[:n_train, :]
        self.test = self.data.loc[n_train:, :]
        data_sets = []
        for set_name, dataset in zip(['train', 'test'],
                                     [self.train, self.test]):
            y = pd.DataFrame(dataset[y_col])
            X = dataset.drop(y_col, axis=1)
            data_sets.append([X, y])
            print(f'{set_name}:\n X: {X.shape}\n y: {y.shape}')
        return data_sets
        

    def _shuffle(self):
        shuffled_idxs = np.random.permutation(range(self.n))
        self.data = self.data.loc[shuffled_idxs, :]
        self.data.index = range(self.n)




# Test
#splitter = DataSplitter('data/heart.csv')
#[[X_train, y_train],
# [X_test, y_test]] = splitter.split_data(
#     'target', fraction_train=0.75, shuffle=True)
