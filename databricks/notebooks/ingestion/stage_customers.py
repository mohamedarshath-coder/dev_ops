# Databricks notebook source
# MAGIC %md
# MAGIC # Stage Customers
# MAGIC Loads raw customers into a staging view for downstream tasks.

# COMMAND ----------

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("StageCustomers").getOrCreate()

customers = spark.createDataFrame(
    [
        (1, "Alice"),
        (2, "Bob"),
    ],
    ["customer_id", "customer_name"],
)

customers.write.mode("overwrite").saveAsTable("stg_customers")
print(f"Staged {customers.count()} customers into stg_customers")
