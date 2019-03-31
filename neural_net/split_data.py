import numpy as np
import pandas as pd


class DataSplitter:
    def __init__(self, filepath, fraction_train=0.6, fraction_valid=0.2):
        extension = filepath.split('.')[-1]
        assert extension == 'csv', 'input data must be in csv format'
        print(f'Reading data from {filepath}...')
        data = pd.read_csv(filepath)
        print(f'Data has shape: {data.shape}')
        n = data.shape[0]
        n_train = int(round(n * fraction_train))
        n_valid = int(round(n * fraction_valid))
        self.train = data.loc[:n_train, :]
        self.valid = data.loc[n_train:n_train + n_valid, :]
        self.test = data.loc[n_train + n_valid:, :]

    def split_data(self, y_col, shuffle=False):
        if shuffle:
            self._shuffle()
        data_sets = []
        for set_name, dataset in zip(['train', 'valid', 'test'],
                                     [self.train, self.valid, self.test]):
            y = pd.DataFrame(dataset[y_col])
            X = dataset.drop(y_col, axis=1)
            data_sets.append([X, y])
            print(f'{set_name}:\n X: {X.shape}\n y: {y.shape}')
        return data_sets
        

    def _shuffle(self):
        shuffled_idxs = np.random.shuffle(range(n))
        self.data = data.loc[shuffled_idxs, :]




# Test
splitter = DataSplitter('data/heart.csv')
[[X_train, y_train],
 [X_valid, y_valid],
 [X_test, y_test]] = splitter.split_data('target')

