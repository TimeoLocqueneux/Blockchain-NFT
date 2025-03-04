from helpers import timestamp, cryptography
import time
from json import dumps

class Collection():

    def __init__(self, CollectionOwner, size):
        self.CollectionOwner = CollectionOwner
        self.timestamp = timestamp.now()
        self.size = size
        self.tokens = []

    def mint_token(self,owner, image_link,description,can_be_exchanged):
        """At the beginning the minter is the owner"""

        if len(self.tokens) < self.size: # If the collection has not reached its maximum capacity

            print("Minting")
           # time.sleep(10) # “mint” period 
                
            # Token characteristics
            payload = {}
                                        
            payload['image_link'] = image_link # link
            payload['description'] = description # description
            payload['can_be_exchanged'] = can_be_exchanged # bool

            payloadString = dumps(payload, sort_keys=True)
            payload['identifier'] = cryptography.hash_string(payloadString)

            payload['owner'] = owner

            self.tokens.append(payload)

            print("Minted !")

        else:
            print("Limit of tokens reached")


    def change_ownership(self, NewOwnerPublicKey, identifier):
        """The change_ownership is a function use to exchange token between users"""             

        for token in self.tokens:
            if token['identifier'] == identifier:
                if token['can_be_exchanged'] == True:
                    token['owner'] = NewOwnerPublicKey
                else:
                    print("The token can not be exchange")
            
        
    def display(self):
        output = {}
        for i, token in enumerate(self.tokens):
            output[f"Token No{i}"] = token
        return output



