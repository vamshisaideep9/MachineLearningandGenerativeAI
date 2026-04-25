class DatabaseConnection:
    def __init__(self, db_url):
        self.db_url = db_url
    
    def __enter__(self):
        # 1. Acquire resource 
        print(f"Connecting to {self.db_url}") 
        self.connection = "Activate Connection Object"
        return self.connection 
    

    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type is not None:
            print(f"Error occured: {exc_type}. Rolling back.") 
        else: 
            print("Success. COmmitting transcation.")

        print("Closing connection.")
        return False
    


"""
Usage:

with DatabaseConnection("postgresql://localhost") as conn:
    pass

"""
                 