import numpy as np
import socket


class ServerMethods():

    """ 
        Server method needs to be modified based on the type of hardware that's being used. 
        It can have different requests and responses based on the medium of communication 
        and user. 
    
    """ 

    def __init__(self, location, radius):

        self.location = location 
        self.radius = radius
        self.entities = -1
        
    def uplink(self, updates):


    def sendData(self, request_idx):

