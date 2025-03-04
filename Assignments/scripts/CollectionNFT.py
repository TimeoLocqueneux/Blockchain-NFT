from helpers import timestamp
from NFTProject import Tokisen

class Collection(Tokisen):
    def __init__(self, issuerPublicKey, size):
        self.issuerPublicKey = issuerPublicKey
        self.timestamp = timestamp.now()
        self.size = size
        self.tokens = []

    def mint_token(self,image_link,description,can_be_exchanged):
         #ajouter les arguements si besoin
        if self.is_token_allowed():
            payload = super().build_payload() # with the owner ID and the time that the token was created
            payload['identifier'] = super().generate_token_key()
            payload['image_link'] = image_link # link
            payload['description'] = description # description
            payload['can_be_exchanged'] = can_be_exchanged # bool

            # Ajouter la creation du token
            self.size += 1

    def is_token_allowed(self):
        if len(self.tokens) < self.size:
            return True

    def display(self):
        for token in self.tokens:
            for element in token:
                return element