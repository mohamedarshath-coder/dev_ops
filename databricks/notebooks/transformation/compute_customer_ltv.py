# Databricks notebook source
# MAGIC %md
# MAGIC # Customer LTV Computation (dev_ops sandbox)
# MAGIC Computes a simple lifetime-value score for customers.

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# COMMAND ----------

spark = SparkSession.builder.appName("CustomerLTV").getOrCreate()

orders = spark.createDataFrame(
    [
        (1, 101, "confirmed", 100.0),
        (1, 102, "shipped", 50.0),
        (2, 103, "confirmed", 200.0),
    ],
    ["customer_id", "order_id", "status", "net_amount"],
)

# COMMAND ----------

ltv = orders.filter(F.col("status").isin("confirmed", "shipped", "delivered")).groupBy(
    "customer_id"
).agg(
    F.sum("net_amount").alias("monetary_total"),
    F.count("order_id").alias("order_count"),
)

ltv.show()
