import pandas as pd
covid = pd.read_csv('covid_data.csv' )
covid.info()

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 1048575 entries, 0 to 1048574
# Data columns (total 21 columns):
#  #   Column                Non-Null Count    Dtype 
# ---  ------                --------------    ----- 
#  0   USMER                 1048575 non-null  int64 
#  1   MEDICAL_UNIT          1048575 non-null  int64 
#  2   SEX                   1048575 non-null  int64
#  3   PATIENT_TYPE          1048575 non-null  int64
#  4   DATE_DIED             1048575 non-null  object
#  5   INTUBED               1048575 non-null  int64
#  6   PNEUMONIA             1048575 non-null  int64
#  7   AGE                   1048575 non-null  int64
#  8   PREGNANT              1048575 non-null  int64
#  9   DIABETES              1048575 non-null  int64
#  10  COPD                  1048575 non-null  int64
#  11  ASTHMA                1048575 non-null  int64
#  12  INMSUPR               1048575 non-null  int64
#  13  HIPERTENSION          1048575 non-null  int64
#  14  OTHER_DISEASE         1048575 non-null  int64
#  15  CARDIOVASCULAR        1048575 non-null  int64
#  16  OBESITY               1048575 non-null  int64
#  17  RENAL_CHRONIC         1048575 non-null  int64
#  18  TOBACCO               1048575 non-null  int64
#  19  CLASIFFICATION_FINAL  1048575 non-null  int64
#  20  ICU                   1048575 non-null  int64
# dtypes: int64(20), object(1)
# memory usage: 168.0+ MB