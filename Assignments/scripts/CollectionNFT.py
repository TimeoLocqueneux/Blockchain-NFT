from helpers import timestamp, cryptography

from json import dumps

class Collection():
    def __init__(self, issuerPublicKey, size):
        self.issuerPublicKey = issuerPublicKey
        self.timestamp = timestamp.now()
        self.size = size
        self.tokens = []

    def mint_token(self,owner, image_link,description,can_be_exchanged):
         #ajouter les arguements si besoin
        if self.is_token_allowed():

            payload = {}
                                         
            payload['image_link'] = image_link # link
            payload['description'] = description # description
            payload['can_be_exchanged'] = can_be_exchanged # bool

            payloadString = dumps(payload, sort_keys=True)
            payload['identifier'] = cryptography.hash_string(payloadString)

            payload['owner'] = owner

            self.tokens.append(payload)
            
            # Ajouter la creation du token
            self.size += 1


    def change_ownership(self, senderPublicKey, receiverPublicKey, numberoftokens):
        Collection_Sender = senderPublicKey.tokens
        Collection_Receiver = receiverPublicKey.tokens # list of tokens

        i = 0
        for token in Collection_Sender:
            i+=1
            if i < numberoftokens:
                token['owner'] = None
                

        for token in Collection_Receiver:
            i+=1
            if i < numberoftokens:
                token['owner'] = receiverPublicKey.issuerPublickKey 
        
        

    def is_token_allowed(self):
        if len(self.tokens) < self.size:
            return True

    def display(self):
        for token in self.tokens:
            for element in token:
                return element