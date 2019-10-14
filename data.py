import json
import numpy as np

DATA_PATH = 'board.json'

def get_data():
    with open(DATA_PATH) as f:
        return np.array(json.load(f))

if __name__ == '__main__':
    print(get_data())
