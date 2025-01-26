from pydantic import BaseModel


class RetrainConfSchema(BaseModel):
    """Class to parse and validate an MLmodel conf file. 
    """
    mlflow_ip: str
    bq_sql_query: str