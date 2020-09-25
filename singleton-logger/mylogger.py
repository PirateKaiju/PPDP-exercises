#import logging

class Logger(): 

    logger_instance = None

    class __Logger(object):
        
        def _write_file(self, level, msg):

            with open("./test.log", 'a') as log_file:
                log_file.write(level + " : " + msg)

        def error(self, msg):
            self._write_file("Error", msg + "\n")
        
        def warning(self, msg):
            self._write_file("Warning", msg + "\n")

        #Can be more

    def __new__(self): #Can also be solved by using the __init__ method

        if Logger.logger_instance == None:
            Logger.logger_instance = Logger.__Logger()
        return Logger.logger_instance

    def __getattr__(self, name): #Pass it up to the nested class
        return getattr(self.logger_instance, name)

    def __setattr__(self, name): #Pass it up to the nested class
        return setattr(self.logger_instance, name)

    
    


