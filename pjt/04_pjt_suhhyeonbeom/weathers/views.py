from django.shortcuts import render

# Create your views here.
import pandas as pd




def pb1(request):
    csv_path = 'austin_weather.csv'
    df = pd.read_csv(csv_path)  
    context = {
        'df' : df,
    }
    return render(request,'weathers/problem1.html',context)


import matplotlib.pyplot as plt

def pb2(request):
    csv_path = 'austin_weather.csv'
    df = pd.read_csv(csv_path)
    df["Date"] = pd.to_datetime(df["Date"])
    x = df['Date']
    y1 = df['TempHighF']
    y2 = df['TempLowF']
    y3 = df['TempAvgF']
    
    plt.clf()
    plt.figure(figsize=(6,8))
    plt.plot(x,y1,label = 'High Temperature')
    plt.plot(x,y3,label = 'Average Temperature')
    plt.plot(x,y2,label = 'Low Temperature')

    plt.grid(True)
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature')
    
    plt.legend()
    
    from io import BytesIO
    buffer = BytesIO()
    
    plt.savefig(buffer,format = 'png')# budder에 그래프를 png 형태로 저장
    import base64 # 텍스트와 이진데이터를 서로 변환할 수 있는 인코딩용 모듈
    
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','') # 그냥 이미지는 이렇게 쓰는구나 라고 생각
    buffer.close()

    
    context = {
    'image2' : f'data:image2/png;base64,{img_base64}',
    }
    return render(request,'weathers/problem2.html',context)

def pb3(request):
    
    csv_path = 'austin_weather.csv'
    df = pd.read_csv(csv_path)
    df['Date'] = pd.to_datetime(df['Date'])

    # 'Date' 열을 인덱스로 설정
    df.set_index('Date', inplace=True)

    numeric_columns = ['TempHighF', 'TempAvgF', 'TempLowF', ]  # 숫자형으로 변환할 열 이름 목록

    # 선택한 열에 대해 데이터 형식을 변환
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df_numeric = df[numeric_columns]
    # 월별로 데이터를 리샘플링하고 평균을 계산
    monthly_mean = df_numeric.resample('MS').mean()
    monthly_mean.index = monthly_mean.index.strftime('%Y-%m')   
    # print(monthly_mean)
    x = monthly_mean.index
    y1 = monthly_mean['TempHighF']
    y3 = monthly_mean['TempAvgF']
    y2 = monthly_mean['TempLowF']


    plt.clf()
    plt.figure(figsize=(6,8))
    plt.plot(x,y1,label = 'High Temperature')
    plt.plot(x,y3,label = 'Average Temperature')
    plt.plot(x,y2,label = 'Low Temperature')
    plt.legend()
    plt.grid(True)
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature')
    plt.xticks(monthly_mean.index[::5], rotation=45)
    
    from io import BytesIO
    buffer = BytesIO()
    
    plt.savefig(buffer,format = 'png')# budder에 그래프를 png 형태로 저장
    import base64 # 텍스트와 이진데이터를 서로 변환할 수 있는 인코딩용 모듈
    
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','') # 그냥 이미지는 이렇게 쓰는구나 라고 생각
    buffer.close()
    context = {
    'image3' : f'data:image3/png;base64,{img_base64}',
    }
    return render(request,'weathers/problem3.html',context)

    

def pb4(request):
    csv_path = 'austin_weather.csv'
    df = pd.read_csv(csv_path)
    
    events = df['Events']
    total = len(events)
    rain_count = df['Events'].str.contains('Rain', na=False).sum()
    fog_count = df['Events'].str.contains('Fog', na=False).sum()
    thunderstorm_count = df['Events'].str.contains('Thunderstorm', na=False).sum()
    snow_count = df['Events'].str.contains('Snow', na=False).sum()
    no_count = total - (rain_count+fog_count+thunderstorm_count+snow_count)
    data = {
    'Event': ['Rain', 'Fog', 'Thunderstorm', 'Snow', 'No Event'],
    'Count': [rain_count, fog_count, thunderstorm_count, snow_count, no_count]
    }
    new_df = pd.DataFrame(data)
    new_df.set_index('Event', inplace=True)  # 인덱스 설정
    new_df = new_df.sort_values('Count', ascending=False)  # 내림차순 정렬
    # print(new_df)
    event = new_df.index
    count = new_df['Count']
    plt.clf()
    plt.figure(figsize=(6,8))
    plt.bar(event, count, color='skyblue')

    plt.title('Event Counts')
    plt.xlabel('Event')
    plt.ylabel('Count')

    plt.xticks(rotation=45)
    
    plt.grid(True)
    from io import BytesIO
    buffer = BytesIO()
    
    plt.savefig(buffer,format = 'png')
    import base64 
    
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','') 
    buffer.close()
    context = {
    'image4' : f'data:image4/png;base64,{img_base64}',
    }
    return render(request,'weathers/problem4.html',context)
    
 

# csv_path = 'austin_weather.csv'
# df = pd.read_csv(csv_path)
# events = df['Events']
# total = len(events)
# rain_count = df['Events'].str.contains('Rain', na=False).sum()
# fog_count = df['Events'].str.contains('Fog', na=False).sum()
# thunderstorm_count = df['Events'].str.contains('Thunderstorm', na=False).sum()
# snow_count = df['Events'].str.contains('Snow', na=False).sum()
# no_count = total - (rain_count+fog_count+thunderstorm_count+snow_count)


# data = {
#     'Event': ['Rain', 'Fog', 'Thunderstorm', 'Snow', 'No Event'],
#     'Count': [rain_count, fog_count, thunderstorm_count, snow_count, no_count]
# }
# new_df = pd.DataFrame(data)
# new_df.set_index('Event', inplace=True)  # 인덱스 설정
# new_df = new_df.sort_values('Count', ascending=False)  # 내림차순 정렬
# # print(new_df)
# events = new_df.index
# counts = new_df['Count']

# # 막대 그래프를 그립니다.
# plt.figure(figsize=(10, 6))
# plt.bar(events, counts, color='skyblue')

# # 그래프에 제목과 축 레이블을 추가합니다.
# plt.title('Event Counts')
# plt.xlabel('Event')
# plt.ylabel('Count')

# # x축 눈금 라벨을 45도 회전합니다.
# plt.xticks(rotation=45)

# # 그래프를 표시합니다.
# plt.show()

# print(events)
# print(events)

# df['Date'] = pd.to_datetime(df['Date'])

# # 'Date' 열을 인덱스로 설정
# df.set_index('Date', inplace=True)

# numeric_columns = ['TempHighF', 'TempAvgF', 'TempLowF', ]  # 숫자형으로 변환할 열 이름 목록

# # 선택한 열에 대해 데이터 형식을 변환
# for col in numeric_columns:
#     df[col] = pd.to_numeric(df[col], errors='coerce')

# df_numeric = df[numeric_columns]
# # 월별로 데이터를 리샘플링하고 평균을 계산
# monthly_mean = df_numeric.resample('MS').mean()
# monthly_mean.index = monthly_mean.index.strftime('%y-%m')   
# # print(monthly_mean)
# x = monthly_mean.index
# y1 = monthly_mean['TempHighF']
# y3 = monthly_mean['TempAvgF']
# y2 = monthly_mean['TempLowF']



# plt.clf()
# plt.plot(x,y1,label = 'High Temperature')
# plt.plot(x,y3,label = 'Average Temperature')
# plt.plot(x,y2,label = 'Low Temperature')
# plt.legend()
# plt.grid(True)
# plt.title('Temperature Variation')
# plt.xlabel('Date')
# plt.ylabel('Temperature')
# plt.xticks(monthly_mean.index[::2], rotation=45)
# # print
# plt.show()
# df['Date'] = pd.to_datetime(df['Date'])
# df['TempHighF'] = pd.to_numeric(df['TempHighF'])
# df['TempAvgF'] = pd.to_numeric(df['TempAvgF'])
# df['TempLowF'] = pd.to_numeric(df['TempLowF'])
# # re_df = df.set_index('Date')

# # 'Date' 열을 인덱스로 설정
# df.set_index('Date', inplace=True)

# # 숫자 형식이 아닌 열을 제거
# numeric_columns = df.select_dtypes(include=['number']).columns
# df_numeric = df[numeric_columns]

# # 월별로 데이터를 리샘플링하고 평균을 계산
# resample = df_numeric.resample(rule='1M').mean()
# resample()
# print(resample)

# df['Date'] = pd.to_datetime(df['Date'])
# df['TempHighF'] = pd.to_numeric(df['TempHighF'])
# df['TempAvgF'] = pd.to_numeric(df['TempAvgF'])
# df['TempLowF'] = pd.to_numeric(df['TempLowF'])
# numeric_columns = df.select_dtypes(include=['number']).columns
# # df_numeric = df[numeric_columns]
# df_numeric = df[numeric_columns]
# df_meanclose = df_numeric.groupby(pd.Grouper(key='Date',freq='M')).mean().reset_index()

# print(df_meanclose)

# csv_path = 'austin_weather.csv'
# df = pd.read_csv(csv_path)

# # 'Date' 열을 날짜 형식으로 변환
# df['Date'] = pd.to_datetime(df['Date'])

# # 'Date' 열을 인덱스로 설정
# df.set_index('Date', inplace=True)

# numeric_columns = ['TempHighF', 'TempAvgF', 'TempLowF', ]  # 숫자형으로 변환할 열 이름 목록

# # 선택한 열에 대해 데이터 형식을 변환
# for col in numeric_columns:
#     df[col] = pd.to_numeric(df[col], errors='coerce')

# df_numeric = df[numeric_columns]
# # 월별로 데이터를 리샘플링하고 평균을 계산
# monthly_mean = df_numeric.resample('MS').mean()
# monthly_mean.index = monthly_mean.index.strftime('%Y-%m')   
# print(monthly_mean)