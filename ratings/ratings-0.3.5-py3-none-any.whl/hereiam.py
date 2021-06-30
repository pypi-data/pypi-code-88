
import os
from pathlib import Path
HERE = os.path.dirname(os.path.realpath(__file__))
ROOT = Path(HERE).parent.absolute()
DATA = os.path.join(ROOT,'data')
TRAIN_CSV = os.path.join(DATA,'train.csv')
TEST_CSV = os.path.join(DATA,'test.csv')
TRAINING_CSV = os.path.join(DATA,'training.csv')
TESTING_CSV = os.path.join(DATA,'testing.csv')


if __name__=='__main__':
    print(DATA)