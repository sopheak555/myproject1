import uvicorn
from fastapi import FastAPI, Query
import pyodbc
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Query

app = FastAPI()
origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

conn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-8CNDV0E\\SQL2022;Database=Test;Trusted_Connection=yes')
cursor = conn.cursor()

@app.get("/data/")
async def read_data(filter: str = Query(None)):
    query = "SELECT TOP 1 * FROM [dbo].[Book1]"
    if filter:
        query += f" WHERE Responsible_Staff_ID LIKE '%{filter}%'"
    cursor.execute(query)
    results = [Responsible_Staff_ID[0] for Responsible_Staff_ID in cursor.description]
    # data = [columns for row in cursor.fetchall()]
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
    # cursor.close()
    # conn.close()
    print(rows)
    return rows



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
