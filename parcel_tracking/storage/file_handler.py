import os
import json

#print("Libraries succussfully imported")
file_path = os.path.join(os.getcwd(),"data","parcels.json")

def load_data():
    if not os.path.exists(file_path):
        return []
    file = None
    try:
        file = open(file_path,'r')
        data = json.load(file)
        if isinstance(data,list):
            return data
        return []
    except (json.JSONDecodeError,OSError):
        return[]
    finally:
        if file is not None:
            file.close()
    
def save_data(parcels):
    file = None
    try:
        file = open(file_path,'w')
        json.dump(parcels, file, indent=2)
    except OSError:
        print(" Error while saving the parcel data! ")
    finally:
        if file is not None:
            file.close()
