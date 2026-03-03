# %%
import pandas as pd

df = pd.read_csv('../src/csv/노인요양시설.csv',  encoding='cp949')
# %%
print(df)

# %%
print(df.shape)
# %%
print(df.transpose())
# %%
print('확인')
print(df.head())
print(df.head(1))
# %%
print(df.columns)

# %%
print(type(df))
# %%
print(df.dtypes)

# %%
# df_t = df.transpose()
# print(df_t, df_t.shape, df_t.columns)
# %%
print('전치후 컬럼명 확인하기/ 숫자임')
df_t = df.T
print(df_t.head(), df_t.shape, df_t.columns)

# %%
print('컬럼명 수정하기')
df_t = df_t.reset_index()
df_t.columns = ["년월", "신고수", "신축수"]
print(df_t.head())

# %%
# df_t.columns = df_t.iloc[0]
print(df_t.columns)

# %%
df_t = df_t[1:]
print(df_t.head())

# %%

import numpy as np
df_t[['신고수', '신축수']] = df_t[['신고수', '신축수']].replace(0, np.nan)
print(df_t)

# %%
print(df_t.isnull().sum())
# %%
# '신고수'와 '신축수' 컬럼의 빈값을 숫자 0으로 채우기
df_t[['신고수', '신축수']] = df_t[['신고수', '신축수']].fillna(0)
print('빈값은 \n',df_t.isnull().sum())

print('0의 값은 \n', (df_t == 0).sum())
# %%
# 1. 각 행의 모든 값이 0인지 검사 (True/False 결과 반환)
# axis=0 (기본값): 세로 방향 (위에서 아래로)

#axis=1: 가로 방향 (왼쪽에서 오른쪽으로)
# null은 실수라 다른 값으로 대체될때 소수점이 생김
print(df_t)
all_zero_rows = (df_t == 0).all(axis=1)

# 2. True(모든 값이 0인 행)의 개수 합산
print(all_zero_rows.sum())
# %%
df_t[['신고수', '신축수']] = df_t[['신고수', '신축수']].astype(int)
print(df_t.head(3))
all_zero_rows = (df_t == 0).all(axis=1)

# 2. True(모든 값이 0인 행)의 개수 합산
print('모든 행의 값이 0인 행의 수는 ', all_zero_rows.sum())
# %%
custom_zero_rows = (df_t[['신고수', '신축수']] == 0).all(axis=1)
count = custom_zero_rows.sum()
print(f"두 컬럼 모두 0인 행의 개수: {count}")
print('전체 행의 개수 ',df_t.shape[0])
# %%
