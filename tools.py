from datetime import datetime

def get_current_time():
    return datetime.now().strftime("%H:%M:%S")
def calculate_area(x,y):
    return x*y
def read_file(file_name):
    
        try:
            with open(file_name,"r") as file:
                content=file.read()
                return content
        except:
             return "File not found"
        
