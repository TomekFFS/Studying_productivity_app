import json                                 
from pathlib import Path                    

# Point directly to the new safe data folder mapped by Docker
DATA_DIR = Path("/app/data")

# Safety check: ensure the directory actually exists before trying to write to it
DATA_DIR.mkdir(parents=True, exist_ok=True) 

DATA_FILE = DATA_DIR / "data.json"          

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
