# databricks-connect

Databricks-Connect allows you to run Spark code from your favorite IDE or notebook server.

## 1. Cluster Setup

1. For Databricks Runtime Version, select Databricks Runtime 5.1 or above.
2. Click the Spark tab and add the following Spark conf: spark.databricks.service.server.enabled true.
3. Add the following Spark conf: spark.databricks.service.port 8787.
4. Click Create Cluster.

## 2. Client Setup

1. Create a virtual python environment (I'm using pipenv, but you can use conda, virtualenv or something else).
2. Make sure that the minor version of your client python installation is the same as the Databricks cluster python version.
3. Install Java 8, the client does not support Java 11.
4.
