from pyspark.sql import SparkSession
from pyspark.sql.functions import desc

# Create Spark Session
spark = SparkSession.builder \
    .appName("SalesDataFrameApp") \
    .master("local[*]") \
    .getOrCreate()

# Read CSV file
df = spark.read.csv("sales.csv", header=True, inferSchema=True)

# -----------------------------
# 1. Sort products by sales
# -----------------------------
sorted_df = df.orderBy(desc("sales"))

print("\n=== Products Sorted by Sales (Descending) ===")
sorted_df.show()

# -----------------------------
# 2. Top 3 highest sales
# -----------------------------
print("\n=== Top 3 Products by Sales ===")
top3 = sorted_df.limit(3)
top3.show()

# -----------------------------
# 3. Filter sales > 80000
# -----------------------------
filtered_df = df.filter(df.sales > 80000)

print("\n=== Products with Sales > 80000 ===")
filtered_df.show()

# Save filtered data as CSV
filtered_df.toPandas().to_csv("filtered_sales.csv", index=False)

print("\nFiltered data saved to filtered_sales.csv")

spark.stop()