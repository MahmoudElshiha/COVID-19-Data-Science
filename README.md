# COVID-19 Data Science

## Kaggle Dataset

[Explore the COVID-19 Dataset on Kaggle](https://www.kaggle.com/datasets/meirnizri/covid19-dataset)

---

## Understanding the Dataset

This dataset, provided by the Mexican government, contains anonymized patient-related information, including pre-existing conditions. It comprises **21 unique features** and data from **1,048,576 unique patients**.

- **Boolean Features**: `1` indicates "Yes", and `2` indicates "No".
- **Missing Data**: Values such as `97` and `99` represent missing information.

---

## Feature Descriptions

### Demographics

- **Sex**:  
   `1` - Female  
   `2` - Male
- **Age**: Age of the patient.

### COVID-19 Diagnosis

- **COVID_Test_Result**:
  - `1-3`: Diagnosed with COVID-19 (various degrees).
  - `4+`: Not a carrier or inconclusive test results.

### Patient Care

- **Patient_Care_Type**:
  - `1`: Returned home.
  - `2`: Hospitalized.
- **Treatment_Level**: Indicates the level of medical unit care: first, second, or third level.
- **Medical_Unit_Type**: Type of institution within the National Health System providing care.

### Pre-existing Conditions

- **Pneumonia**: Air sacs inflammation.
- **Pregnant**: Pregnancy status.
- **Diabetes**: Presence of diabetes.
- **COPD**: Chronic Obstructive Pulmonary Disease.
- **Asthma**: Asthma condition.
- **Immunosuppressed**: Immunosuppression status.
- **Hypertension**: High blood pressure.
- **Cardiovascular_Disease**: Heart or blood vessel-related disease.
- **Chronic_Renal_Disease**: Chronic kidney disease.
- **Other_Disease**: Other unspecified diseases.
- **Obesity**: Obesity status.
- **Tobacco_Use**: Tobacco usage.

### Critical Care

- **Intubated**: Whether the patient was connected to a ventilator.
- **ICU_Admission**: Admission to an Intensive Care Unit.

### Outcome

- **Date_of_Death**:
  - If deceased: Date of death.
  - Otherwise: `9999-99-99`.

---
