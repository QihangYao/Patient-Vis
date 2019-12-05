""" Mimic-III database """

# Whether to use local database
LOCAL_DB = False
# If local database is available, following configuration
# will be used to access MIMIC-III database.
LOCAL_DB_NAME = "mimic"
LOCAL_DB_USER = "postgres"
LOCAL_DB_PWD = "postgres"
LOCAL_HOSTNAME = "localhost"
LOCAL_PORT = "5432"

# Whether to use athena database
ATHENA_DB = False
# If athena database is specified to be used, use following
# configurations
AWS_ACCESS_KEY_ID = None
AWS_SECRET_ACCESS_KEY = None
S3_STAGING_DIR = None
REGION_NAME = None

def get_db_conn():

    # Local database and athena database shouldn't be used together
    assert not all((LOCAL_DB, ATHENA_DB))
    
    # Get the database connection based on previous settings.
    if LOCAL_DB:

        import psycopg2

        return psycopg2.connect(
            "dbname=" + LOCAL_DB_NAME +
            " user=" + LOCAL_DB_USER +
            " host=" + LOCAL_HOSTNAME +
            " password=" + LOCAL_DB_PWD +
            " port=" + LOCAL_PORT  + " options=--search_path=mimiciii"
        )
    elif ATHENA_DB:

        import pyathena

        return pyathena.connect(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            s3_staging_dir=S3_STAGING_DIR,
            region_name=REGION_NAME,
            schema_name="mimiciii",
        )
    else:
        return None