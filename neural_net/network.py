import itertools

import numpy as np
import pandas as pd


N = 100


def main():
    data_set = DataSet(N)
    print(data_set)
    print(data_set.data.head())
    [X_train, y_train], [X_test, y_test] = data_set.split_data()
    features = list(X_train)
    print(features)
    network = Network(features)


class DataSet:
    def __init__(self, n, response='y', path=None, test_frac=0.2):
        self.response = response
        self.test_frac = test_frac
        if path is not None:
            self._data = pd.read_csv(path)
            self.n = self._data.shape[0]
        else:
            self.n = n
            self._data = self._make_test_data(n, self.test_frac)

    def __str__(self):
        return f'DataSet of shape {self._data.shape}'

    @property
    def data(self):
        return self._data
            
    def _make_test_data(self, n, test_frac):
        A = np.random.uniform(size=n)
        B = np.random.poisson(lam=2., size=n)
        C = np.random.normal(size=n)
        D = np.random.choice([0, 1], size=n)
        E = np.random.standard_t(df=2, size=n)
        y = (A - 2*B + 1.1*C**2 - np.log(2*(B+2)) + 0.2*A*B + 1/(C+1)**2
             - 0.77*E + np.sqrt(D*B)/(B + 1))
        data = pd.DataFrame({'y': y, 'A': A, 'B': B, 'C': C, 'D': D, 'E': E})
        return data

    def split_data(self, shuffle=False):
        data = self.data
        n_train = int(round(self.n * (1 - self.test_frac)))
        if shuffle:
            data = data.sample(frac=1).reset_index(drop=True)
        train = data.loc[:n_train, :]
        test = data.loc[n_train:, :]
        y_train = train[self.response]
        y_test = test[self.response]
        X_train = train.drop(self.response, axis=1)
        X_test = test.drop(self.response, axis=1)
        return [[X_train, y_train], [X_test, y_test]]
            

class Network:
    def __init__(self, feature_names, n_inputs=1, n_outputs=1):
        self.features = features
        self.n_inputs = n_inputs
        self.n_outputs = n_outputs
        self.inputs = []


def relu(x):
    return x if x > 0 else 0



if __name__ == '__main__':
    main()
