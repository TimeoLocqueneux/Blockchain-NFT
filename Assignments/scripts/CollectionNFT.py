from helpers import timestamp, cryptography
import time
from json import dumps

class Collection():

    def __init__(self, CollectionOwner, size):
        self.CollectionOwner = CollectionOwner
        self.timestamp = timestamp.now()
        self.size = size
        self.tokens = []

    def mint_token(self,owner, image_link,description):
        """At the beginning the minter is the owner"""

        if len(self.tokens) < self.size: # If the collection has not reached its maximum capacity

            print("Minting")
                
            # Token characteristics
            payload = {}

            payload['identifier'] = len(self.tokens)
            payload['image_link'] = image_link # link
            payload['description'] = description # description
            payload['owner'] = owner

            self.tokens.append(payload)

            print("Minted !")

        else:
            print("Limit of tokens reached")


    def change_ownership(self, OldOwnerPublicKey, NewOwnerPublicKey, identifier):
        """The change_ownership is a function use to exchange token between users"""             

        # if the previous user owns the NFT, he can exchange it

        for token in self.tokens:
            if token['identifier'] == identifier:
                if token['owner'] == OldOwnerPublicKey:
                    token['owner'] = NewOwnerPublicKey
                else:
                    print("The sender does not owns the NFT")
            
        
    def display(self):
        output = {}
        for i, token in enumerate(self.tokens):
            output[f"Token No{i}"] = token
        return output
    



