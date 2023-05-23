def connect_to_sql_server():
    conn = pyodbc.connect("Driver={SQL Server};Server=DESKTOP-8CNDV0E\SQL2022;Database=Test;Trusted_Connection=yes;")
    cursor = conn.cursor()
    cursor.execute("select  top 1 * from [dbo].[Book1]  ")
    rows = cursor.fetchall()
    #convert data format from database to dataframe
    df = pd.DataFrame(rows)
    print(df)
    return df.to_json(orient="records")