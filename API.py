
from fastapi import FastAPI
import pandas as pd
import json
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import pandas as pd
import pyodbc 
import warnings
import uvicorn

app = FastAPI(title="Human Resource API",
    description="This is a simple API to predict employee churn",
    version="1.0.0",)
# # create pydantic model
# class Employee(BaseModel):
#    Staff ID: int

conn = pyodbc.connect("Driver={SQL Server};Server=DESKTOP-8CNDV0E\SQL2022;Database=Test;Trusted_Connection=yes;")

df = pd.read_sql_query('select Top 1 * from [dbo].[Book1]', conn)

print(df)
class Employee(BaseModel):
    NO	: int
    Branch: str	
    Responsible_Staff_ID: int
    Staff_Name: str
    Being_Balance_of_Year:float
    Beginning_Balance: float
    Current_Balance_Growth : float
    Plan_of_Account:int
    ACTUAL_NUM_T24:float
    Variation_NUM_T24:int 
    NUM_T24	:int
    ACTUAL_BAL_T24:float
    Variation_BAL_T24:int
    BAL_T24:float
    Plan_of_Register_AM:int
    ACTUAL_NUM_ACLEDA:float	
    Variation_NUM_ACL:int
    NUM_ACL:int	
    Plan_of_Balance_AM:int	
    ACTUAL_BAL_ACL:float
    Variation_BAL_ACL:int
    BAL_ACL:float	
    Plan_of_Partner:float
    ACTUAL_NUM_PAR:float	
    Variation_NUM_PAR:int
    NUM_PAR:int	
    Plan_of_Balance_Partner:int
    ACTUAL_BAL_PAR:float
    Variation_BAL_PAR:float
    BAL_PAR	:float
    Plan_From:str
    Plan_To:str
    Booking_Date:str
    POSITION:str
    Location_of_Position:str
    Number_Existing_Customer:int
    Being_Bal_Existing_Customer:float
    Current_Bal_Existing_Customer:float
    Variation:int
@app.get('/')
@app.get('/home')
def home():
    return {'message': 'Welcome to Employee Churn Prediction API'}
# Ml api route
@app.post('/model')
def index(data: Employee):
    # convert input data to a pandas DataFrame
    data_dict = data.dict()
    data = pd.DataFrame([data_dict]).values
    data = pd.DataFrame(data)
    
    print(data)
    
    # ingore warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        
        # make prediction
        result = df.index(data)
        print(result)
    
    result = result.tolist()
    return result[0]
#How to run this code
#1. Open terminal

# print(type(df))


# #correct fub
# @app.get("/sql")
# def connect_to_sql_server():
#     conn = pyodbc.connect("Driver={SQL Server};Server=DESKTOP-8CNDV0E\SQL2022;Database=Test;Trusted_Connection=yes;")
#     cursor = conn.cursor()
#     cursor.execute("select  top 1 * from [dbo].[Book1]  ")
#     rows = cursor.fetchall()
#     #convert data format from database to dataframe
#     df = pd.DataFrame(rows)
#     print(df)
#     return df.to_json(orient="records")

  




   


    
    # # ingore warnings
    # with warnings.catch_warnings():
    #     warnings.simplefilter("ignore")
        
    #     # make prediction
    #     result = model.index(data)
    #     print(result)
    
    # result = result.tolist()
    # return result[0]




# # convert to 2D array
#     data = []
#     for row in rows:
#         data.append(list(row))
#     return data
#     #convert data format from database to dataframe
#     df = pd.DataFrame(data)
#     return df.to_json(orient="records")

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000, reload=True)


