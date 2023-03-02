import pymongo
import pandas as pd
import json


client = pymongo.MongoClient("mongodb+srv://singh:singh9821@cluster0.7a31upb.mongodb.net/?retryWrites=true&w=majority")
db = client.test


#database name
Database_name="aps"
Collection_name="sensor"
Data_file_path="C:/Users/prata/PycharmProjects/sensor fault detection/aps_failure_training_set1.csv"



if __name__=="__main__":
    df=pd.read_csv(Data_file_path)
    print(f"rows and columns:{df.shape}")

    #convert dataframe to json so that we can dump these record in mongodb

    df.reset_index(drop=True,inplace=True)

    json_records=list(json.loads(df.T.to_json()).values())

    print(json_records[0])


    client[Database_name][Collection_name].insert_many(json_records)








