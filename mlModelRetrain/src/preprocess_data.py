from credit_risk_lib.pipeline.transform.transform_interface import TransformInterface
from credit_risk_lib.mlmodel.mllogger import MLLogger

from pandas import DataFrame, concat
from sklearn.preprocessing import LabelEncoder


class PreprocessData(TransformInterface):
    def __init__(self, mllogger: MLLogger, step_name: str = "MLModelRetrain"):
        self.mllogger = mllogger
        self._step_name = step_name
    
    
    @staticmethod
    def _drop_outliers(data: DataFrame) -> DataFrame:
        for col in data.select_dtypes(include=["Int64", "Float64"]).columns:
            quartiles = data[col].quantile([0.25, 0.75])
            iqr = quartiles[0.75] - quartiles[0.25]
            severe_lower_outliers = quartiles[0.25] -3 * iqr
            severe_upper_outliers = quartiles[0.25] +3 * iqr
            if severe_upper_outliers > 0 and severe_lower_outliers > 0:
                data = data[(data[col] > severe_lower_outliers)&(data[col] < severe_upper_outliers)]
        return data 
    
    
    @staticmethod
    def _encode_data(data: DataFrame) -> DataFrame:
        encoded_cols: DataFrame = data.select_dtypes(include=["string"]) \
            .apply(lambda x: LabelEncoder().fit_transform(x))
        encoded_cols.columns = [f"encoded_{col}" for col in encoded_cols.columns]
        transformed_data = concat([data, encoded_cols], axis =1)
        return transformed_data.drop(data.select_dtypes(include=["string"]), axis=1)
    
    
    def transform(self, data: DataFrame) -> DataFrame:
        self.mllogger.log_param("raw_data_shape", data.shape)
        data = data.convert_dtypes()
        data.dropna(inplace=True)
        data.drop_duplicates(inplace=True)
        data = self._drop_outliers(data)
        self.mllogger.log_param("preprocessed_data_shape", data.shape)
        encoded_data = self._encode_data(data)
        self.mllogger.log_param("encoded_data_shape", encoded_data.shape)
        return encoded_data
        
        