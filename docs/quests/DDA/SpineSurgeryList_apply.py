import pandas as pd

# CSV 파일 불러오기
df = pd.read_csv('datasets/SpineSurgeryList.csv')

# '체중' 컬럼과 '신장' 컬럼 apply
df['신장'] = df['신장'].apply(lambda x: (x/100)**2)
df['체중'] = df['체중'].apply(lambda x: x)

# BMI 컬럼 생성
df['BMI'] = df['체중'] / df['신장']

def surgery_time(x):
    try:    
        hour = int(x/60)
        min = int(x%60)
        if int(x/60) == 0:
            time = pd.to_datetime(f"{min}", format="%M")
            pass
        else:
            time = pd.to_datetime(f"{hour}, {min}", format="%H, %M")
            pass
        return time
    except:
        pass
pass
df['수술시간_datetime'] = df["수술시간"].apply(surgery_time_time)
df['수술시간_datetime'] = df['수술시간_datetime'].dt.time
pass



print(df['BMI'])
df.info()
pass

