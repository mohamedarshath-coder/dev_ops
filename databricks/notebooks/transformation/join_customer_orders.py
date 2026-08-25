# Databricks notebook source
# MAGIC %md
# MAGIC # Join Customer Orders
# MAGIC Joins staged orders and customers into a single enriched dataset.
# MAGIC Depends on stage_orders and stage_customers having already run.

# COMMAND ----------

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("JoinCustomerOrders").getOrCreate()

orders = spark.table("stg_orders")
customers = spark.table("stg_customers")

joined = orders.join(customers, on="customer_id", how="inner")
joined.show()
print(f"Joined {joined.count()} rows")
