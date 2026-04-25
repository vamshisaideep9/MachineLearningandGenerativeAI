class DatabaseConnection:
    def __init__(self, database_url):
        self.database_url = database_url

    def __enter__(self):
        self.connection = "Activating Connection"
        return self.connection 
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the conneciton.")
        if exc_type is not None:
            print(f"Error Occured: {exc_type} rollingback")
        else: 
            print("Success, Commiting transaction!")

        print("Close Connection!")
        return False 
    
