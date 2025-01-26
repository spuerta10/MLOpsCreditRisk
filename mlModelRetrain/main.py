from src.config.retrain_conf_schema import RetrainConfSchema
from src.bq_data_preprocessor import BQDataPreprocessor

from credit_risk_lib.config.config import Config
from credit_risk_lib.config.config_factory import ConfigFactory 

conf: Config = ConfigFactory.get_conf(r"src/config/retrain_conf.json", RetrainConfSchema)
preprocessed_bq_data = BQDataPreprocessor.run(conf)
print(preprocessed_bq_data.head(5))