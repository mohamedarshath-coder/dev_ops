# Databricks notebook source
# MAGIC %md
# MAGIC # Stage Orders
# MAGIC Loads raw orders into a staging view for downstream tasks.

# COMMAND ----------

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("StageOrders").getOrCreate()

orders = spark.createDataFrame(
    [
        (1, 101, "confirmed", 100.0),
        (1, 102, "shipped", 50.0),
        (2, 103, "confirmed", 200.0),
    ],
    ["customer_id", "order_id", "status", "net_amount"],
)

orders.createOrReplaceTempView("stg_orders")
print(f"Staged {orders.count()} orders into stg_orders")
