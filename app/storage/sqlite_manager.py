import json                                 #used for human-readable storage
from pathlib import Path                    #works on both Linux / Windows safely
BASE_DIR = Path(__file__).resolve().parent  #folder containing sqlite_manager.py
DATA_FILE = BASE_DIR / "data.json"          #app/storage/data.json

def _ensure_data_file(): #ensures data exists
    if not DATA_FILE.exists():  
        DATA_FILE.write_text(json.dumps({"tasks": []}, indent=2))

def load_data():
    _ensure_data_file() #guarantees file exists
    return json.loads(DATA_FILE.read_text()) #reads JSON text and converts it into Python dict

def save_data(data):
    DATA_FILE.write_text(json.dumps(data, indent=2))

def get_tasks(): #returns the list of tasks directly.
    return load_data()["tasks"]

def save_tasks(tasks_list): #basically does what it's named after
    data=load_data()
    data["tasks"]= tasks_list
    save_data(data)
