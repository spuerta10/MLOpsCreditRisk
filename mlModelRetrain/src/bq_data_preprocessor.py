from datetime import (
    datetime,
    timedelta,
    date
)
from preprocess_data import PreprocessData

from pandas import DataFrame
from credit_risk_lib.config.config import Config
from credit_risk_lib.pipeline.ingest.bigquery import BigQuery
from credit_risk_lib.mlmodel.mllogger import MLLogger
from credit_risk_lib.pipeline.pipeline import Pipeline


class BQDataPreprocessor:
    @staticmethod
    def run(conf: Config) -> DataFrame:
        last_execution = str(
            (datetime.now() - timedelta(weeks=1)).date()
        ) # assuming the DAG will be executed weekly
        ingest = BigQuery(
            sql_query= conf.bq_sql_query.format(last_execution, str(date.today())),
            gcp_project_id= "creditriskmlops" 
        )
        mllogger = MLLogger(conf)
        transform = PreprocessData(mllogger)
        preprocessed_bq_data = Pipeline(
            ingest_stage=ingest,
            transform_stage=transform
        ).run()
        return preprocessed_bq_data