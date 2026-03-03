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
