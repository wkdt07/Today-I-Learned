import requests
import pandas as pd

from api import api_key

# API 엔드포인트 URL과 API 키
endpoints = {
    '행정동별 상권분석': f'http://openapi.seoul.go.kr:8088/{api_key}/json/VwsmAdstrdIxQq/1/1/',
    '상권변화지표 상권': f'http://openapi.seoul.go.kr:8088/{api_key}/json/VwsmTrdarIxQq/1/1/',
    '집객시설 상권': f'http://openapi.seoul.go.kr:8088/{api_key}/json/VwsmTrdarFcltyQq/1/1/',
    '추정매출 상권': f'http://openapi.seoul.go.kr:8088/{api_key}/json/VwsmTrdarSelngQq/1/1/',
    '길단위인구 상권배후지': f'http://openapi.seoul.go.kr:8088/{api_key}/json/VwsmTrdhlFlpopQq/1/1/',
    '영역-상권배후지': f'http://openapi.seoul.go.kr:8088/{api_key}/json/TbgisTrdhlRelmW/1/1/'
}

# 모든 데이터를 저장할 빈 DataFrame 생성
all_data = pd.DataFrame()

# API에 요청을 보냅니다.
for title, url in endpoints.items():
    response = requests.get(url)

    # 요청이 성공했는지 확인합니다.
    if response.status_code == 200:
        # JSON 형식으로 파싱합니다.
        data = response.json()

        # JSON 데이터를 DataFrame으로 변환합니다.
        df = pd.DataFrame(data)

        # DataFrame을 빈 DataFrame에 추가합니다.
        all_data = pd.concat([all_data, df], ignore_index=True)
    else:
        print(f"API 요청이 실패했습니다: {title}")

# 모든 데이터를 엑셀 파일로 저장합니다.
all_data.to_excel('new_all_data.xlsx', index=False)
print("엑셀 파일이 생성되었습니다.")
