import pyodbc
from fastapi import FastAPI
import uvicorn
import pandas as pd
import json
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
# from pydantic import BaseModel


app = FastAPI(title="Human Resource API",
    description="This is a simple API to predict employee churn",
    version="1.0.0",)


#correct fub
@app.get("/sql")
def connect_to_sql_server():
    conn = pyodbc.connect("Driver={SQL Server};Server=DESKTOP-8CNDV0E\SQL2022;Database=Test;Trusted_Connection=yes;")
    cursor = conn.cursor()
    cursor.execute("select  top 1 * from [dbo].[Book1]")
    rows = cursor.fetchall()
    #convert data format from database to dataframe
    df = pd.DataFrame(rows)
    print(df)
    return df.to_json(orient="records")

# # convert to 2D array
#     data = []
#     for row in rows:
#         data.append(list(row))
#     return data
#     #convert data format from database to dataframe
#     df = pd.DataFrame(data)
#     return df.to_json(orient="records")



#convert

#how to run this code
#1. Open terminal
#2. cd to the folder that contains this file
#3. type uvicorn Backend:app --reload



if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000, reload=True)


