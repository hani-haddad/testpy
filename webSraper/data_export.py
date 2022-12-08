import pandas
import pandas as pd


class Exporter:
    def __init__(self, location):
        self.location = location

    @staticmethod
    def to_data_frame(data):
        data_frame = pd.DataFrame(data)
        return data_frame

    def csv_export(self, data_frame):
        data_frame.to_csv(self.location + '.csv')

    def json_export(self, data_frame):
        data_frame.to_json(self.location + '.json', orient='records', lines=True)

#rkrkrk