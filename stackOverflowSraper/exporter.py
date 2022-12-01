import pandas as pd

class exporter():

    def to_data_frame(data):
        data_frame = pd.DataFrame(data)
        return data_frame


    def csv_export(self):
        self.data_frame.to_csv('Questions_Details.csv')


    def json_export(self):
        self.data_frame.to_json('Questions_Details.json', orient='records', lines=True)

