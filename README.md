# databricks-connect

Databricks-Connect allows you to run Spark code from your favorite IDE or notebook server.

## 1. Cluster Setup

1. For Databricks Runtime Version, select Databricks Runtime 5.1 or above.
2. Click the Spark tab and add the following Spark conf:
`spark.databricks.service.server.enabled true`
`spark.databricks.service.port 8787`
3. Click Create Cluster.

## 2. Client Setup

1. Create a virtual python environment (I'm using pipenv, but you can use conda, virtualenv or something else).
2. Make sure that the minor version of your client python installation is the same as the Databricks cluster python version.
3. Install `Java 8`, the client does not support `Java 11`.
4. Install the `databricks-connect` client in my case:
`pipenv install databricks-connect==5.2.*`, where the version matches my Databricks Runtime.

## 3. Configuring Connection Properties

1. Collect the following configuration properties:

  - URL: A URL of the form https:<region>.azuredatabricks.net.
  - User token: A user token.
  - Cluster ID: The ID of the cluster you created. You can obtain the cluster ID from the URL. Here the cluster ID is 1108-201635-xxxxxxxx.
  - Organization ID. Every workspace has a unique organization ID. The random number after o= in the workspace URL is the organization ID. If the workspace URL is https://westus.azuredatabricks.net/?o=7692xxxxxxxx, organization ID is 7692xxxxxxxx.
  - Port: The port that Databricks Connect connects to. Set to 8787.

2. Configure Databricks Connect.

Run: `databricks-connect configure`. The license displays:

```
Copyright (2018) Databricks, Inc.

This library (the "Software") may not be used except in connection with the
Licensee's use of the Databricks Platform Services pursuant to an Agreement
...
```

Accept the license and supply configuration values.

```python
you accept the above agreement? [y/N] y
Set new config values (leave input empty to accept default):
Databricks Host [no current value, must start with https://]: 'DATABRICKS_URL'
Databricks Token [no current value]: 'DATABRICKS_TOKEN'
Cluster ID (e.g., 0921-001415-jelly628) [no current value]: 'CLUSTER_ID'
Org ID (Azure-only, see ?o=orgId in URL) [0]: 'ORGANIZATION_ID'
Port (Use 15001 for AWS, 8787 for Azure) [15001]: 'PORT'
```
