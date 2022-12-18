import pandas as pd
import json

class Exporter:
    def __init__(self, location):
        self.location = location

    @staticmethod
    def to_data_frame(data):
        data_frame = pd.DataFrame(data)
        return data_frame

    def csv_export(self, data):
        data.to_csv(self.location + '.csv')

    def json_export(self, data):
        #data_frame.to_json(self.location + '.json', orient='records', lines=True)
        with open(self.location+".json", 'w') as f:
           json.dump(data, f)