from app import create_app

app = create_app() #building the car

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0") #starting the engine

    #in case of sharing via host add this to ' , host="0.0.0.0" '