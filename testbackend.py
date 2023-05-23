from fastapi import FastAPI
from pydantic import BaseModel
import pyodbc
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(title="Human Resource API",
    description="This is a simple API to predict employee churn",
    version="1.0.0",)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the Pydantic model
class StaffRequest(BaseModel):
    staff_id: str

# Define the database connection string
conn_str = "Driver={SQL Server};Server=DESKTOP-8CNDV0E\SQL2022;Database=Test;Trusted_Connection=yes;"

# Define the function to query the database
def get_staff_data(staff_id: str):
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    query = f"SELECT * FROM [dbo].[Book1] WHERE Responsible_Staff_ID='{staff_id}'"
    cursor.execute(query)

    rows = cursor.fetchall()
    results = []
    for row in rows:
        result = {}
        for i, column in enumerate(cursor.description):
            result[column[0]] = row[i]
        results.append(result)

    cursor.close()
    conn.close()
    return results

# Define the FastAPI endpoint
@app.get("/staff")
def get_staff_data_endpoint(staff: StaffRequest):
    staff_id = staff.staff_id
    results = get_staff_data(staff_id)

    return {"data": results}
