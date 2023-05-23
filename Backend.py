import pyodbc
from fastapi import FastAPI
import uvicorn
import pandas as pd
import json
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Query
# from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(title="Human Resource API",
    description="This is a simple API to predict employee churn",
    version="1.0.0",)


origins = [
    "http://localhost:3000",
]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#correct fub
@app.get("/sql")
async def connect_to_sql_server():
    conn = pyodbc.connect("Driver={SQL Server};Server=DESKTOP-8CNDV0E\SQL2022;Database=Test;Trusted_Connection=yes;")
    cursor = conn.cursor()
    cursor.execute("select  top 10 * from [dbo].[Book1]  ")
    results = cursor.fetchall()
    rows = []
    for row in results:
        row_dict = {}
        for i in range(len(row)):
            if row[i] is not None:
                column_name = cursor.description[i][0]
                row_dict[column_name] = row[i]
        rows.append(row_dict)
    print(4444444444444444444444444444, rows)
    # Close the cursor and connection
    cursor.close()
    conn.close()
    print(rows)
    return rows



if __name__ == '__main__':
    # uvicorn.run(app, host='localhost', port=8000, reload=True)
      uvicorn.run(app, host="0.0.0.0", port=8000)


#how to run this code
#1. Open terminal
#2. cd to the folder that contains this file
#3. type uvicorn Backend:app --reload
