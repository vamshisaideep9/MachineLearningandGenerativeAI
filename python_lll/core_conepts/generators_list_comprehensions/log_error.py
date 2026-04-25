


import re 



def error_log_parser(filepath):
    with open(filepath, 'r') as file:
        er = re.compile("ERROR")
        for line in file:
            if er.search(line):
                yield line.strip()


    
class CustomRange:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop 
        self.step = step
        self.current = self.start 
        self.temp = self.current 

    def __iter__(self):
        return self 
    

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        else:
            self.temp = self.current
            self.current += self.step

        return self.temp  


