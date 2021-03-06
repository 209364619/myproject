# coding=utf-8
import pandas as pd
import numpy as np

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

dates = pd.date_range('20170101', periods=7)
print(dates)

print("--" * 16)
# 数据帧
print '数据帧'
df = pd.DataFrame(np.random.randn(7, 4), index=dates, columns=list('ABCD'))
print(df)

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20170102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

print(df2)
