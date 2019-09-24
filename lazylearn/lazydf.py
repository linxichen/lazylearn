import pandas as pd


class KungFuDataFrame():
    def __init__(self, df, form, id_vars, value_vars, *args, **kwargs):
        self.df = df
        self.id_vars = id_vars
        self.value_vars = value_vars
        self.form = form

    @property
    def longform(self):
        if self.form is not 'long':
            out = self.df.melt(id_vars=self.id_vars,value_vars=self.value_vars)
            return out
        else:
            return self.df

    @property
    def shape(self):
        return self.df.shape


