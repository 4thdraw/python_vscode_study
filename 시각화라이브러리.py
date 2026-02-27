# %%
import matplotlib.pyplot as plt
print("맵플로립 호출")

# %%
# 1. 데이터 준비 (공부하신 리스트 활용!)
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
study_hours = [2, 5, 4, 8, 3]
print("데이터체크", days, study_hours )


# %%
# 2. 그래프 그리기 (함수 호출)
plt.plot(days, study_hours)
plt.show()


# %%
plt.plot(days, study_hours, marker='o', color='#fadc44')
plt.show()


# %%
plt.plot(days, study_hours, 
         color='springgreen',      # 선 색상 (이름이나 HEX 코드 가능)
         linestyle='dashed',       # 선 모양 (solid, dashed, dotted, dashdot)
         linewidth=3,              # 선 두께
         marker='D',               # 마커 모양 (D: 다이아몬드)
         markerfacecolor='white',  # 마커 내부 색상
         markersize=10,            # 마커 크기
         markeredgecolor='black',  # 마커 테두리 색상
         alpha=0.7)                # 투명도 (0~1 사이)
plt.show()

# %%
# 3. 꾸미기
plt.title('My Study Hours')
plt.xlabel('Day')
plt.ylabel('Hours')
plt.plot(days, study_hours)
# 4. 출력
plt.show()


# %% [3] Scatter Plot (산점도)
# 데이터의 개별 지점을 점으로 표시할 때 사용합니다. 
# 데이터의 분포나 상관관계를 보기에 좋습니다.
plt.scatter(days, study_hours, 
            s=100,                  # 점의 크기 (size)
            c='tomato',             # 점의 색상 (color)
            alpha=0.6,              # 투명도
            edgecolors='black')     # 테두리 색상
plt.title('Scatter Plot: Study Hours')
plt.show()

# %% [4] Bar Chart (막대 그래프)
# 항목 간의 수치를 비교할 때 가장 효과적입니다.
plt.bar(days, study_hours, 
        color='gold',               # 막대 색상
        width=1,                  # 막대 너비
        edgecolor='darkgoldenrod',  # 테두리 색상
        linewidth=2)                # 테두리 두께
plt.title('Bar Chart: Study Hours')
plt.xlabel('Day')
plt.ylabel('Hours')
plt.show()

# %% [5] Barh Chart (가로 막대 그래프) - 보너스!
# 항목 이름이 길 때 유용한 가로 막대 형태입니다.
plt.barh(days, study_hours, color='lightcoral')
plt.title('Horizontal Bar Chart')
plt.show()

# %%
import matplotlib.font_manager as fm
print('한글깨짐방지 모듈호출')
# %%
font_path = r'C:\Windows\Fonts\malgunbd.ttf'
# 2. 폰트 이름 가져오기
font_name = fm.FontProperties(fname=font_path).get_name()

# 3. 마플로립의 전체 폰트 설정 업데이트
plt.rc('font', family=font_name)

# 4. 마이너스 기호(-)가 깨지는 현상 방지
plt.rcParams['axes.unicode_minus'] = False

print(f"설정된 폰트: {font_name}")

# %%
import matplotlib.ticker as ticker
print("눈금 정밀 제어 눈금제어옵션모듈호출")


# %%
# 옵션: y축 눈금 정밀 제어 (ticker)
# 1. 먼저 데이터를 그립니다 (본질)
plt.plot(days, study_hours, marker='o', color='dodgerblue', linewidth=2)

# 2. 그 다음 축 설정을 가져옵니다 (옵션)
ax = plt.gca() 

# 3. Y축 눈금을 1 단위로 정밀 제어 (데이터가 8까지이므로 1이 적당함)
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

# 4. 타이틀 및 라벨 설정
plt.title('공부 시간 분석 (정밀 눈금 적용)')
plt.xlabel('요일')
plt.ylabel('시간 (Hours)')

# 5. 격자 추가 (눈금이 잘 들어갔는지 확인용)
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()




# %%
