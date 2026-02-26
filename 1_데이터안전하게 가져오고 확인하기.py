# %%
import pandas as pd

# 파일 경로를 넣을 때는 꼭 앞에 r을 붙이세요! (왕초보 경로 에러 방지용)


path =r'C:\Users\korea\Desktop\c\src\csv\노인요양시설.csv'
# r은 **Raw string(가공되지 않은 문자열)**의 약자

#우리나라에서 만든 한글 중심의 인코딩 cp949 (공공한글데이터), 표준 utf-8
df = pd.read_csv(path, encoding='cp949')

# try:
#     df = pd.read_csv(file_path, encoding='cp949')
#     print("성공! cp949 방식으로 읽었습니다.")
# except:
#     df = pd.read_csv(file_path, encoding='utf-8')
#     print("성공! utf-8 방식으로 읽었습니다.")

print("데이터 이사 완료! 이제 위쪽 Jupyter Variables를 눌러 표를 확인하세요.")
# %%
