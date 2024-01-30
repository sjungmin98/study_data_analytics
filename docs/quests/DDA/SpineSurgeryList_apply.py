import pandas as pd
import numpy as np  # 누락값(NaN)을 처리하기 위해 numpy사용 / **ValueError: cannot convert float NaN to integer

# CSV 파일 불러오기
df = pd.read_csv('datasets/SpineSurgeryList.csv')

# '체중' 컬럼과 '신장' 컬럼 apply
df['신장'] = df['신장'].apply(lambda x: (x/100)**2)
df['체중'] = df['체중'].apply(lambda x: x)

# BMI 컬럼 생성
df['BMI'] = df['체중'] / df['신장']

# 분을 시간과 분 형태의 문자열로 변환하고, 이를 datetime 형식으로 변환하는 함수
def surgery_time(minutes):
    if pd.isnull(minutes):
        return np.nan       #Nan
    else:
        hours = minutes // 60
        minutes = minutes % 60
        time_str = f"{int(hours)}:{int(minutes)}"
        return pd.to_datetime(time_str, format='%H:%M').time()

# apply 함수를 사용하여 '수술시간' 컬럼의 각 요소에 대해 함수 적용
df['수술시간_datetime'] = df['수술시간'].apply(surgery_time)

print(df['수술시간_datetime'])
print(df['BMI'])
pass

