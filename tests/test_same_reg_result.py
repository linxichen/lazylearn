import unittest
import pandas as pd
import lazylearn.lazydf as lzdf
from sklearn.datasets import load_boston


class MyTestCase(unittest.TestCase):
    def setUp(self):
        out = load_boston()
        X = pd.DataFrame(out['data'],columns=out['feature_names'])
        y = pd.DataFrame(out['target'],columns=['target'])
        self.df = X.join(y).reset_index()

    def test_something(self):
        self.assertEqual(True, False)

    def test_can_turn_to_long(self):
        X_in = lzdf.KungFuDataFrame(self.df, 'tidy',['index'], ['CRIM','AGE'])
        long = (X_in.longform)
        assert long.shape[0] > X_in.df.shape[0]



if __name__ == '__main__':
    unittest.main()
