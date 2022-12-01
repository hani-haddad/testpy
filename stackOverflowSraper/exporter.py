import pandas as pd


class exporter():
    data=[]
    data_frame = pd.DataFrame(data)


    def csv_export(self):
        self.data_frame.to_csv('Questions_Details.csv')


    def json_export(self):
        self.data_frame.to_json('Questions_Details.json', orient='records', lines=True)

