from helpers import timestamp, cryptography
import time
from json import dumps

class Collection():

    def __init__(self, CollectionOwner, size):
        self.CollectionOwner = CollectionOwner
        self.timestamp = timestamp.now()
        self.size = size
        self.tokens = []

    def mint_token(self,MinterPublicKey, image_link,description):
        """At the beginning the minter is the owner"""
        if self.is_active() == True:

            if len(self.tokens) < self.size: # If the collection has not reached its maximum capacity

                print("Minting")
            # time.sleep(10) # “mint” period 
                    
                
                
                # Token characteristics
                payload = {}

                payload['identifier'] = len(self.tokens)
                payload['image_link'] = image_link # link
                payload['description'] = description # description
                payload['owner'] = MinterPublicKey

                self.tokens.append(payload)
                print (self.tokens)

                print("Minted !")

            else:
                print("Limit of tokens reached")
            
            self.change_ownership(self.CollectionOwnerPublicKey, MinterPublicKey)

            
        else:
            print("Minting is closed")


    def change_ownership(self, SenderPublicKey, ReceiverPublicKey):
        """The change_ownership is a function use to exchange token between users"""             

        return f'''

        {SenderPublicKey} sent a nft to {ReceiverPublicKey}

        '''

    def open_minting(self, time_in_seconds):
        self.time_in_seconds = time_in_seconds
        self.start_time=time.time()
        print("Minting is open")

    def is_active(self):
        if (time.time() - self.start_time) < self.time_in_seconds:
            return True
        else:
            return False
        
        
        

                   
            
        
    def display(self):
        output = {}
        for i, token in enumerate(self.tokens):
            output[f"Token No{i}"] = token
        return output
    




