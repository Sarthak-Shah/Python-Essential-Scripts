import cx_Oracle
import pandas as pd
import matplotlib.pyplot as plt

# Establish a connection to the Oracle database
connection = cx_Oracle.connect('sarthak85/sarthak85@DESKTOP-JDP18BT:1521')
# query with left join
sql_query = "SELECT s.*, m.MODEL_NAME, m.manufacturer, m.msrp FROM " \
            "SYS.vw_sales s LEFT JOIN SYS.car_models m ON s.sales_id = m.model_id"

# pandas
df_left = pd.read_sql(sql_query, connection)
print("Left join:")
print(df_left.head())

model_sales = df_left.groupby('MODEL_NAME')['SALES_PRICE'].sum().reset_index()
model_sales = model_sales.sort_values('SALES_PRICE', ascending=False)

# Plotting a bar chart of the total sales for each model
plt.bar(model_sales['MODEL_NAME'], model_sales['SALES_PRICE'])
plt.xticks(rotation=90)
plt.xlabel('Car Model')
plt.ylabel('Total Sales')
plt.title("Model Wise Sales Price (Kajal'S join query concern)")
plt.show()

# Close the connection
connection.close()
