import logging
import os
class Logger:

    u_code=''
    logger=logging.getLogger(__name__)

    # initilizing logger
    def __init__(self,UCODE,threshold='DEBUG'):
        self.u_code= str(UCODE)
        self.logger.name= UCODE
           
            
            
            #yaha se delete kar dena bhai
            
            
            
        # setting logger level
        logger_level={
        "debug"   :logging.DEBUG,
        "info"    :logging.INFO,
        "warning" :logging.WARNING,
        "error"   :logging.ERROR,
        "critical":logging.CRITICAL

        }
        self.logger.setLevel(logger_level[threshold.lower()])

        # Setting default logger formatter
        # Default:  LEVEL UCODE - Message
        formatter= logging.Formatter('%(levelname)s : %(asctime)s : %(name)s - %(message)s')

        file_handler=logging.FileHandler(os.getcwd()+'/'+self.u_code+'.log')
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        print("Logger created with name ",self.u_code+'.log')



    def info(self,message):
        self.logger.info(message)

    def debug(self,message):
        self.logger.debug(message)

    def warning(self,message):
        self.logger.warning(message)

    def error(self,message):
        self.logger.error(message)

    def critical(self,message):
        self.logger.critical(message)

    """
    Further enhancement 
    
    1. Configuring log directory
    2. 
    
    """

