import logging

from connectors.binance import BinanceClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root


# Create and configure the logger object

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)  # Overall minimum logging level

stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler

file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


# logger = logging.getLogger()
# logger.debug("This message is important only whem debugging programm")
# logger.info("This meesage just shows basic information")
# logger.warning("This message is about something you should pay attention to")
# logger.error("This message helps to debug an error")





if __name__ == "__main__":
    
    binance = BinanceClient("", 
    "", testnet=True, futures=True) #insert keys
    
    bitmex = BitmexClient("", "", testnet=True) #insert keys


    root = Root(binance, bitmex)
    root.mainloop()

   

 
    
