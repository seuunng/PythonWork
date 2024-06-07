import pandas as pd

data ={ 'name':['Mark', 'Jane', 'Chris', 'Ryan'],
        'age' : [33, 32, 44, 42],
        'score' : [91.3, 83.4, 77.5, 87.7]
}
df = pd.DataFrame(data)
print(df)
#     name  age  score
# 0   Mark   33   91.3
# 1   Jane   32   83.4
# 2  Chris   44   77.5
# 3   Ryan   42   87.7
df_sum=df.sum()
print(df_sum)
# name     MarkJaneChrisRyan
# age                    151
# score                339.9
# dtype: object
df_avg=df.mean(numeric_only=True)
print(df_avg)
# age      37.750
# score    84.975
# dtype: float64
print(df.age)
# 0    33
# 1    32
# 2    44
# 3    42
# Name: age, dtype: int64
print(df['score'])
# 0    91.3
# 1    83.4
# 2    77.5
# 3    87.7
# Name: score, dtype: float64