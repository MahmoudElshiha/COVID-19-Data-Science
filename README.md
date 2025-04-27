# COVID-19-Data-Science

## The Data Set on Kaggle

[COVID-19 Dataset on Kaggle](https://www.kaggle.com/datasets/meirnizri/covid19-dataset)

### Understanding the Data

The dataset was provided by the Mexican government. This dataset contains an enormous number of anonymized patient-related information, including pre-conditions. The raw dataset consists of 21 unique features and 1,048,576 unique patients. In the Boolean features, `1` means "yes" and `2` means "no". Values such as `97` and `99` represent missing data.

### Feature Descriptions

- **Sex**: `1` for female and `2` for male.
- **Age**: Age of the patient.
- **COVID_Test_Result**: COVID test findings. Values `1-3` mean that the patient was diagnosed with COVID in different degrees. `4` or higher means that the patient is not a carrier of COVID or that the test is inconclusive.
- **Patient_Care_Type**: Type of care the patient received in the unit. `1` for returned home and `2` for hospitalization.
- **Pneumonia**: Whether the patient already has air sacs inflammation or not.
- **Pregnant**: Whether the patient is pregnant or not.
- **Diabetes**: Whether the patient has diabetes or not.
- **COPD**: Indicates whether the patient has Chronic Obstructive Pulmonary Disease or not.
- **Asthma**: Whether the patient has asthma or not.
- **Immunosuppressed**: Whether the patient is immunosuppressed or not.
- **Hypertension**: Whether the patient has hypertension or not.
- **Cardiovascular_Disease**: Whether the patient has heart or blood vessel-related disease.
- **Chronic_Renal_Disease**: Whether the patient has chronic renal disease or not.
- **Other_Disease**: Whether the patient has other diseases or not.
- **Obesity**: Whether the patient is obese or not.
- **Tobacco_Use**: Whether the patient is a tobacco user.
- **Treatment_Level**: Indicates whether the patient was treated in medical units of the first, second, or third level.
- **Medical_Unit_Type**: Type of institution of the National Health System that provided the care.
- **Intubated**: Whether the patient was connected to a ventilator.
- **ICU_Admission**: Indicates whether the patient had been admitted to an Intensive Care Unit.
- **Date_of_Death**: If the patient died, indicates the date of death; otherwise, `9999-99-99`.
