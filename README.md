# Student-Performance-Analysis

This Project is End to End ML based on Student Exam Performance Analysis. It predicts the Math Score of the individual students based on some factors:

- `Gender` : Male or Female
- `Race/Ethnicity` : Group A, Group B, Group C, Groud D & Group E  
- `Parental Level of Education` : Associate's degree, Bachelor's degree, High school, Master's degree, Some college, Some high school
- `Lunch` : Free/reduced, Standard
- `Test Preparation Course`: None, Completed
- `Reading Score` : Min: 0 , Max: 100
- `Writing Score` : Min: 0 , Max: 100

  In EDA, it seen that female students performs better than male, Group E students are also performing better than other groups, and there is no effect of parental level education on students.
  You can check out all the analysis in [EDA Files](https://github.com/Mihir-M112/Student-Performance-Analysis/blob/main/notebook/EDA_STUDENT_PERFORMANCE%20.ipynb)

 
## **Approach for the project**

- **Data Ingestion** :

In Data Ingestion phase the data is read as csv.
Then the data is split into training and testing and saved as csv file.

- **Data Transformation** :

In this phase a ColumnTransformer Pipeline is created.
for Numeric Variables first SimpleImputer is applied with strategy median , then Standard Scaling is performed on numeric data.
for Categorical Variables SimpleImputer is applied with most frequent strategy, then One Hot encoding performed , after this data is scaled with Standard Scaler.
This preprocessor is saved as pickle file namely preprocessor.pkl.

- **Model Training** :

In this phase base model is tested . The best model found was Linear Regression with 88% accuracy.
The model is selected on based on R2 Score Evaluation Metric. The highest R2 Score model selected.

- **Prediction Pipeline** :

This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python.

- **Web Work**:
  The entire project is shown by using HTML, CSS & FAST API for Web Work.

### How to use this project? 

1. Download the whole project in you system or you can also clone it.
2. Make a virtual environment uisng the command:  
    `python -m venv venv`
3. Activate the virtual environments:  
    `.\venv\Scripts\activate`
4. Run the requirements.txt file in venv:  
    `pip install -r requirements.txt`
5. Run the below command:   
    `uvicorn app.main:app --reload`
   

![image](https://github.com/user-attachments/assets/a9312176-d4a8-4627-8138-1e7079597798)

![image](https://github.com/user-attachments/assets/458c1014-b854-422f-80a9-aa35a73526d7)




