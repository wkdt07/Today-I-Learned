### A. 데이터 전처리 - 데이터 읽어오기

다행히 데이터를 불러오는 부분에 대해선 크게 어려운 점이 없었습니다. 그런데 해당 데이터에서는 필요한 열이 붙어있었기에 range(5)를 통해 구해도 상관이 없었지만, 만약 열이 떨어져 있었다면 어떻게 했어야 할지가 궁금했습니다.

```python
df = pd.read_csv(csv_path, usecols=range(5))

#여기서 usecols로 불러올 열을 선택할 때, 만약 그 열이 1,3,6 등 불연속적인 열이었다면?
```

### B. 데이터 전처리 – 2021년 이후의 종가 데이터 출력하기

데이터를 전처리, 특히 필터링하는 부분에서 데이터 타입에 문제가 있었습니다. 형태는 같았기에 굳이 변형이 필요하지 않다 생각했지만, 오류가 났기 때문에, to_datetime()의 역할을 확실히 알 수 있었습니다

```python
# 비교 가능하도록 데이터 타입 변경
df["Date"] = pd.to_datetime(df["Date"])

""" 데이터 타입의 변형이 선행되어야 이후 비교를 통한 필터링이 필요 """

#새로운 df 생성(2021년 이후로 데이터 필터링)
df_after_2021 = df[df["Date"]>="2021-01-01"]

# 그래프 그리기 (가로, 세로 축에 표시될 데이터를 차례로 기입)
plt.plot(df_after_2021['Date'], df_after_2021['Close'])


# 그래프 제목 설정
plt.title('NETFLIX Close Price')

# x축 레이블 설정
plt.xlabel('Date')

# y축 레이블 설정
plt.ylabel('Close')

# 그래프 표시
plt.show()
```

### C. 데이터 분석 – 2021년 이후 최고, 최저 종가 출력하기

이 부분에선 크게 어려운 점이 없었습니다. 다만 최저, 최고 종가 값을 찾아 변수에 할당할 때, 키값이 int형일 수 있다는 점을 새로 배웠습니다.

```python
# 값 정렬
df_after_2021['Close'].sort_values() # 이거 출력하면 key값 알 수 있다

#최저, 최고 종가 값 할당
min_one = df_after_2021['Close'][1001] # 키값이 int 형
max_one = df_after_2021['Close'][954]
print("최고 종가 :", max_one)
print("최저 종가 :", min_one)
```

### D. 데이터 분석 - 2021년 이후 월 별 평균 종가 출력하기

오늘 시도해봤던 내용 중 가장 어려웠던 부분이었습니다. 가장 신기했던 부분은, datetime 변수형이 자동적으로 Y,M,D 로 값이 할당되어 있다는 점이었습니다. frequence를 'M'으로 할당할 수 있다는 점이 굉장히 편했습니다.

또한 검색 등으로 새롭게 배웠던 내용이 가장 많은 파트였습니다. 기존에 존재하던 데이터를 일부만 groupby와 Grouper로 뽑아내어 새롭게 만들어내는 부분이 인상적이었습니다.

가장 큰 문제는 index가 제대로 적용이 되지 않아, 이하의 코드에선 키로 접근하는 부분에서 문제가 생겼다는 것이었습니다. 이를 해결하기 위해 여러 블로그와 chat GPT의 도움을 받아 reset_index() 메서드를 사용했습니다.

```python
#groupby와 grouper로 close 데이터들을 달에 맞게 그룹화하고, 이후 mean()을 이용해 평균 출력 후 할당
df_meanclose = df_after_2021.groupby(pd.Grouper(key='Date',freq='M')).mean().reset_index()

df_meanclose['Date'] = df_meanclose['Date'].dt.strftime('%Y-%m')

# 그래프 그리기 (가로, 세로 축에 표시될 데이터를 차례로 기입)
plt.plot(df_meanclose['Date'], df_meanclose['Close'])


# 그래프 제목 설정
plt.title('NETFLIX Monthly Average Close Price')

# x축 레이블 설정
plt.xlabel('Date')

# x 축 설정(회전시키기) ****
plt.xticks(df_meanclose['Date'][::2], rotation=45)
#step으로 레이블에 나타나는 애들을 1,3,5... 만

# y축 레이블 설정
plt.ylabel('Price')

# 그래프 표시
plt.show()
```

### E. 데이터 시각화 – 2022년 이후 최고, 최저, 종가 시각화하기

이 부분에선 여러 종류의 데이터를 하나의 좌표평면 위에 표현하는 부분을 배웠습니다.

다행히 예시로 올려주신 자료가 충분히 혼자서도 이해할 수 있을 정도로 자세했기에 이 부분에 대해선 큰 어려움 없이 과제를 마칠 수 있었습니다.

```python

```#새로운 df 생성(2022년 이후로 데이터 필터링)
df_after_2022 = df[df["Date"]>="2022-01-01"]

plt.plot(df_after_2022['Date'], df_after_2022['High'], label='High')
plt.plot(df_after_2022['Date'], df_after_2022['Low'], label='Low')
plt.plot(df_after_2022['Date'], df_after_2022['Close'], label='Close')

plt.title('High, Low, and Close Prices since January 2022')

plt.xlabel('Date')

plt.ylabel('Price')

plt.xticks(rotation=45)

# 범례 표시
plt.legend()

# 그래프 표시
plt.show()