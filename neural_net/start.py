from split_data import DataSplitter


DATA_DIR = './data'

def main():
    data_file = f'{DATA_DIR}/heart.csv'
    splitter = DataSplitter(data_file)
    [[X_train, y_train], [X_test, y_test]] = splitter.split_data('target',
                                                                 shuffle=True) 

if __name__ == '__main__':
    main()
