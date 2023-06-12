# Databricks notebook source
# MAGIC %sql
# MAGIC create table customers
# MAGIC (
# MAGIC cust_id int,
# MAGIC products array<string>,
# MAGIC price array<int>
# MAGIC ) 
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into customers values (1111,array('a','b','c','d','e'),array(100,200,300,400,500))

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into customers values (1112,array('c','d','e','a','a'),array(110,120,130,140,150))

# COMMAND ----------

# MAGIC %sql
# MAGIC #select posexplode(products) from customers
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT cust_id, product_exp, price_exp
# MAGIC FROM customers
# MAGIC LATERAL VIEW posexplode(products) exploded AS pos, product_exp
# MAGIC LATERAL VIEW posexplode(price) exploded2 AS pos2, price_exp
# MAGIC where pos=pos2

# COMMAND ----------

# MAGIC %sql
# MAGIC create table customer_expl
# MAGIC (
# MAGIC customerid int,
# MAGIC products string,
# MAGIC price int)

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into customer_expl values (1111,'a',100),(1111,'b',200),(1111,'c',300),(1111,'d',400),(1111,'e',500);
# MAGIC insert into customer_expl values (1112,'c',110),(1112,'d',120),(1112,'e',130),(1112,'a',140),(1112,'a',150);
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from customer_expl;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT customerid, collect_list(products),collect_list(price) from customer_expl
# MAGIC GROUP BY customerid

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT customerid, collect_set(products),collect_set(price) from customer_expl
# MAGIC GROUP BY customerid
