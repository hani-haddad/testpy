import pandas as pd
import csv
import os.path

class exporter():
    data_frame = pd.DataFrame()


    def csv_export(self, Question):
        '''Write item to CSV file'''

        # Check if "Questions Details.csv" file exists
        questions_exists = os.path.isfile('Questions_Details.csv')

        # Append data to CSV file
        with open('Questions_Details.csv', 'a') as csv_file:
            # Init dictionary writer
            writer = csv.DictWriter(csv_file, fieldnames=Question.keys())

            # Write entry to CSV file
            writer.writerow(Question)

    
    def json_export(self):
        self.data_frame.to_json('Questions_Details.json', orient='records', lines=True)



    

