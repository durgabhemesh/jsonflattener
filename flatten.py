from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *



spark=SparkSession.builder.appName("flatten").getOrCreate()


schema = StructType([
    StructField("company", StructType([
        StructField("name", StringType()),
        StructField("location", StringType()),
        StructField("departments", ArrayType(
            StructType([
                StructField("name", StringType()),
                StructField("head", StringType()),
                StructField("employees", ArrayType(
                    StructType([
                        StructField("id", StringType()),
                        StructField("name", StringType()),
                        StructField("skills", ArrayType(StringType()))
                    ])
                ))
            ])
        ))
    ]))
])

df=spark.read.format("json").option("multiline","true").option("path","C:\\Users\\durga\\PycharmProjects\\prep\\data\\data.json").load()


df_dept = df.select(
    col("company.name").alias("company_name"),
    col("company.location").alias("company_location"),
    explode(col("company.departments")).alias("department")
)

df_dept=df_dept.select("company_name","company_location","department.name","department.head",explode(col("department.employees")).alias("emp"))

df_all=df_dept.select("company_name","company_location","name","head","emp.id",col("emp.name").alias("ID_NAME"),explode(col("emp.skills")).alias("skills"))

df_all.show()