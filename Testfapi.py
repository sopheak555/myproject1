import pyodbc
from fastapi import FastAPI
import uvicorn
import pandas as pd
import json
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Human Resource API",
    description="This is a simple API to Staff 360 ",
    version="1.0.0",)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Report(BaseModel):
    No:int
    
#correct fub
@app.get("/sql")
def connect_to_sql_server(No: int):
    conn = pyodbc.connect("Driver={SQL Server};Server=DESKTOP-8CNDV0E\SQL2022;Database=Test;Trusted_Connection=yes;")
    cursor = conn.cursor()
    cursor.execute("select  top 1 * from [dbo].[Book1] where NO = '{No}' ")
    results = cursor.fetchall()
    #convert results to json format
    rows = []
    for row in results:
        row_dict = {}
        for i in range(len(row)):
            if row[i] is not None:
                column_name = cursor.description[i][0]
                row_dict[column_name] = row[i]
        rows.append(row_dict)
    print(4444444444444444444444444444, rows)
    cursor.close()
    conn.close()
    return rows

    
    # rows = []
    # for row in results:
    #     row_dict = {}
    #     for i in range(len(row)):
    #         if row[i] is not None:
    #             column_name = cursor.description[i][0]
    #             row_dict[column_name] = row[i]
    #     rows.append(row_dict)
    # print(4444444444444444444444444444, rows)
    # # Close the cursor and connection
    # cursor.close()
    # conn.close()
    # print(rows)
    # return rows

# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # NEW
# # register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)

# # create base model with report_name, start_date, end_date
# class Report(BaseModel):
#     report_name: str
#     start_date: str
#     end_date : str
    
# # ============================================================================

# @app.get("/")
# async def read_root():
#     return {"Hello": "Your API is working normally"}


# # Download excel file
# # ==============================================================================
# @app.get("/nbc")
# async def download_excel(report_name: str, start_date: str, end_date: str):
#     if report_name == "psp_monthly_report":
#         print(report_name)
#         print(start_date)
#         print(end_date)
#         report_result = psp_monthly_report(report_name, start_date, end_date)
#         print(report_result)
#         # convert csv of sheet2_tb1 to excel
#         return FileResponse("src\\Format\\1-PSP_Monthly_Report.xlsx", media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", filename="1-PSP_Monthly_Report.xlsx")
        
        
#     # elif report_name == "trust_emoney_one":
#     #     report_result = trust_emoney_one(report_name, start_date, end_date)
#     #     return FileResponse("Format/1-PSP_Monthly_Report.xlsx", media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", filename="trust_emoney_one.xlsx")
#     else :
#         return {"Report": "Not Found"}



#how to run this code
#1. Open terminal
#2. cd to the folder that contains this file
#3. type uvicorn Backend:app --reload



if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000, reload=True)
