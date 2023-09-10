import zmq

from streamdeck_sdk import (
    StreamDeck,
    Action,
    events_received_objs,
    logger,
)

from streamdeck_sdk.sd_objs import events_received_objs

import settings
        
class ShowImage(Action):
    def __init__(self, socket):
        self.socket = socket
    UUID = "com.saltchicken.zeromq.showimage"
    
    def on_dial_rotate(self, obj: events_received_objs.DialRotate):
        logger.info(obj.payload)


    def on_key_down(self, obj: events_received_objs.KeyDown):
        category = obj.payload.settings.get("category", "test")
        # logger.info(prompt)
        # union_type = obj.payload.settings.get("union_type", "or")
        # grayscale_flag = obj.payload.settings.get("grayscale_flag", False)
        
        self.socket.send_string("ShowImage")
        
class SaveImage(Action):
    def __init__(self, socket):
        self.socket = socket
    UUID = "com.saltchicken.zeromq.saveimage"
    
    def on_dial_rotate(self, obj: events_received_objs.DialRotate):
        logger.info(obj.payload)

    def on_key_down(self, obj: events_received_objs.KeyDown):        
        self.socket.send_string("SaveImage")
        

if __name__ == '__main__':
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.bind("tcp://*:5557")
    StreamDeck(
        actions=[
            ShowImage(socket),
            SaveImage(socket)
        ],
        log_file=settings.LOG_FILE_PATH,
        log_level=settings.LOG_LEVEL,
        log_backup_count=1,
    ).run()
