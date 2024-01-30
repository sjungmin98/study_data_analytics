import pandas as pd

# CSV 파일 불러오기
df = pd.read_csv('datasets/SpineSurgeryList.csv')

# '체중' 컬럼과 '신장' 컬럼 apply
df['신장'] = df['신장'].apply(lambda x: (x/100)**2)
df['체중'] = df['체중'].apply(lambda x: x)

# BMI 컬럼 생성
df['BMI'] = df['체중'] / df['신장']

print(df['BMI'])
df.info()
pass
