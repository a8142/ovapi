# To run the code:

Pre requisite: you need docker

Go to the path where you cloned the repo and run the following commands:
```shell
docker build -t ovapi-pipeline . 
docker run ovapi-pipeline
```

# How it works:

The pipeline works as follows (the main script is pipeline.py):

- data is extracted from the OVAPI with the the extract.py script.
This is a simple API request. It should be done in a lazy way to not get all the data at once in case of big volume.
We should find a way to query the API data part by part and yield the reponse to process it before loading it to the db.

- data is validated with the validate.py script.
The validation is done using the jsonschema library.
It is a simple validation, we should do something more elaborate in real life.
For the errors, instead of just being logged, they should be stored in a table with a proper monitoring and alerting on
this table.
Also for the errors we should try to see if we want to discard the whole line for a column which is in error or handle
different cases (accept the line and put NULL in this column for instance).
The validation operation could also be parallelized in case of high data volume.
Finally the validation could also be done in SQL (loading the raw data directly and doing this part in SQL from raw table to validated).

- data is loaded into the table with the load.py script.
I used the sqlite db as it is the easiest to use with Python, not requiring any setup. In a real use, we would use
something else, a postgres or else instance or a data warehouse like BigQuery or Snowflake.
The table is created if it does not exists.
Then the data is upserted in the table on the primary key made of 3 columns.
There are 3 technical timestamps: created_at (first time the record appears in the table), updated_at (used for updates
when there is a match in the upsert operation), and deleted_at (not used here, if the record was to be deleted)
The current_timestamp is the one of python datetime here, we should use one provided by the database.

For the testing, I only tested the validation part as the extract part is straightforward here (only a http request).
The load part would require to test the sql execution (which should be done in reality, but I did not implement it for
time reason).
Testing should also be done using a proper testing framework such as unittest or pytest.

Finally, I did not implement the Airflow part as it would only be wrapping the main.py script in a Python operator and
calling it in a dag file.