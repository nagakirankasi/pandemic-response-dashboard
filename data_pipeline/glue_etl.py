import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read raw data from S3
raw_data = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://pandemic-data-bucket/"]},
    format="json"
)

# Transform data
transformed_data = raw_data.toDF()
transformed_data = transformed_data.withColumnRenamed("cases", "total_cases")
transformed_data.write.parquet("s3://pandemic-processed-data/")

job.commit()
