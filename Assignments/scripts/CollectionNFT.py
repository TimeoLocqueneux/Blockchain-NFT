from helpers import timestamp, cryptography

from json import dumps

class Collection():

    @staticmethod
    def hash(payload):                  # We want to hash the whole payload
        payloadString = dumps(payload, sort_keys=True)     # Here I use dumps to transform a dictionary into a string, also sort_keys to ensure all keys will be in the same order
        return cryptography.hash_string(payloadString)     # The "cryptography" module does the rest
    


    def __init__(self, CollectionOwner, size):
        self.CollectionOwner = CollectionOwner
        self.timestamp = timestamp.now()
        self.size = size
        self.token_used = 0
        self.minting = False
        self.tokens = {'Token No0': {'name': 'pikachu', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png', 'description': 'electric'}, 
'Token No1': {'name': 'bulbasaur', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png', 'description': 'grass'}, 
'Token No2': {'name': 'charmander', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png', 'description': 'fire'}, 
'Token No3': {'name': 'squirtle', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png', 'description': 'water'}, 
'Token No4': {'name': 'caterpie', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/10.png', 'description': 'bug'}, 
'Token No5': {'name': 'pidgey', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/16.png', 'description': 'normal'}, 
'Token No6': {'name': 'rattata', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/19.png', 'description': 'normal'}, 
'Token No7': {'name': 'spearow', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/21.png', 'description': 'normal'}, 
'Token No8': {'name': 'ekans', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/23.png', 'description': 'poison'}, 
'Token No9': {'name': 'sandshrew', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/27.png', 'description': 'ground'}, 
'Token No10': {'name': 'clefairy', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/35.png', 'description': 'fairy'}, 
'Token No11': {'name': 'vulpix', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/37.png', 'description': 'fire'}, 
'Token No12': {'name': 'jigglypuff', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png', 'description': 'normal'}, 
'Token No13': {'name': 'zubat', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/41.png', 'description': 'poison'}, 
'Token No14': {'name': 'oddish', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/43.png', 'description': 'grass'}, 
'Token No15': {'name': 'paras', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/46.png', 'description': 'bug'}, 
'Token No16': {'name': 'venonat', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/48.png', 'description': 'bug'}, 
'Token No17': {'name': 'diglett', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/50.png', 'description': 'ground'}, 
'Token No18': {'name': 'meowth', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/52.png', 'description': 'normal'}, 
'Token No19': {'name': 'psyduck', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/54.png', 'description': 'water'}, 
'Token No20': {'name': 'mankey', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/56.png', 'description': 'fighting'}, 
'Token No21': {'name': 'growlithe', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/58.png', 'description': 'fire'},
'Token No22': {'name': 'poliwag', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/60.png', 'description': 'water'}, 
'Token No23': {'name': 'abra', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/63.png', 'description': 'psychic'}, 
'Token No24': {'name': 'machop', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/66.png', 'description': 'fighting'}, 
'Token No25': {'name': 'bellsprout', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/69.png', 'description': 'grass'}, 
'Token No26': {'name': 'tentacool', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/72.png', 'description': 'water'}, 
'Token No27': {'name': 'geodude', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/74.png', 'description': 'rock'}, 
'Token No28': {'name': 'ponyta', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/77.png', 'description': 'fire'}, 
'Token No29': {'name': 'slowpoke', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/79.png', 'description': 'water'}, 
'Token No30': {'name': 'magnemite', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/81.png', 'description': 'electric'}, 
'Token No31': {'name': 'doduo', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/84.png', 'description': 'normal'}, 
'Token No32': {'name': 'seel', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/86.png', 'description': 'water'}, 
'Token No33': {'name': 'grimer', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/88.png', 'description': 'poison'}, 
'Token No34': {'name': 'shellder', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/90.png', 'description': 'water'}, 
'Token No35': {'name': 'gastly', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/92.png', 'description': 'ghost'}, 
'Token No36': {'name': 'onix', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/95.png', 'description': 'rock'}, 
'Token No37': {'name': 'drowzee', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/96.png', 'description': 'psychic'}, 
'Token No38': {'name': 'krabby', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/98.png', 'description': 'water'}, 
'Token No39': {'name': 'voltorb', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/100.png', 'description': 'electric'}, 
'Token No40': {'name': 'exeggcute', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/102.png', 'description': 'grass'}, 
'Token No41': {'name': 'cubone', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/104.png', 'description': 'ground'}, 
'Token No42': {'name': 'hitmonlee', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/106.png', 'description': 'fighting'},
'Token No43': {'name': 'lickitung', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/108.png', 'description': 'normal'}, 
'Token No44': {'name': 'koffing', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/109.png', 'description': 'poison'},
'Token No45': {'name': 'rhyhorn', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/111.png', 'description': 'ground'}, 
'Token No46': {'name': 'tangela', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/114.png', 'description': 'grass'}, 
'Token No47': {'name': 'kangaskhan', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/115.png', 'description': 'normal'}, 
'Token No48': {'name': 'horsea', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/116.png', 'description': 'water'}, 
'Token No49': {'name': 'goldeen', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/118.png', 'description': 'water'}, 
'Token No50': {'name': 'staryu', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/120.png', 'description': 'water'}, 
'Token No51': {'name': 'mr-mime', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/122.png', 'description': 'psychic'}, 
'Token No52': {'name': 'scyther', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/123.png', 'description': 'bug'}, 
'Token No53': {'name': 'jynx', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/124.png', 'description': 'ice'}, 
'Token No54': {'name': 'electabuzz', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/125.png', 'description': 'electric'},
'Token No55': {'name': 'magmar', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/126.png', 'description': 'fire'}, 
'Token No56': {'name': 'pinsir', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/127.png', 'description': 'bug'}, 
'Token No57': {'name': 'tauros', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/128.png', 'description': 'normal'},
'Token No58': {'name': 'magikarp', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/129.png', 'description': 'water'}, 
'Token No59': {'name': 'lapras', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/131.png', 'description': 'water'}, 
'Token No60': {'name': 'ditto', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/132.png', 'description': 'normal'}, 
'Token No61': {'name': 'eevee', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png', 'description': 'normal'}, 
'Token No62': {'name': 'porygon', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/137.png', 'description': 'normal'}, 
'Token No63': {'name': 'omanyte', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/138.png', 'description': 'rock'},
'Token No64': {'name': 'kabuto', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/140.png', 'description': 'rock'}, 
'Token No65': {'name': 'aerodactyl', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/142.png', 'description': 'rock'},
'Token No66': {'name': 'snorlax', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/143.png', 'description': 'normal'}, 
'Token No67': {'name': 'articuno', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/144.png', 'description': 'ice'}, 
'Token No68': {'name': 'zapdos', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/145.png', 'description': 'electric'},
'Token No69': {'name': 'moltres', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/146.png', 'description': 'fire'}, 
'Token No70': {'name': 'dratini', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/147.png', 'description': 'dragon'},
'Token No71': {'name': 'mewtwo', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png', 'description': 'psychic'}, 
'Token No72': {'name': 'mew', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/151.png', 'description': 'psychic'}, 
'Token No73': {'name': 'chikorita', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/152.png', 'description': 'grass'}, 
'Token No74': {'name': 'cyndaquil', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/155.png', 'description': 'fire'}, 
'Token No75': {'name': 'totodile', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/158.png', 'description': 'water'}, 
'Token No76': {'name': 'sentret', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/161.png', 'description': 'normal'},
'Token No77': {'name': 'hoothoot', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/163.png', 'description': 'normal'},
'Token No78': {'name': 'ledyba', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/165.png', 'description': 'bug'}, 
'Token No79': {'name': 'spinarak', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/167.png', 'description': 'bug'}, 
'Token No80': {'name': 'chinchou', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/170.png', 'description': 'water'}, 
'Token No81': {'name': 'pichu', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/172.png', 'description': 'electric'},
'Token No82': {'name': 'cleffa', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/173.png', 'description': 'fairy'}, 
'Token No83': {'name': 'igglybuff', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/174.png', 'description': 'normal'},
'Token No84': {'name': 'togepi', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/175.png', 'description': 'fairy'}, 
'Token No85': {'name': 'natu', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/177.png', 'description': 'psychic'}, 
'Token No86': {'name': 'mareep', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/179.png', 'description': 'electric'},
'Token No87': {'name': 'marill', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/183.png', 'description': 'water'}, 
'Token No88': {'name': 'sudowoodo', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/185.png', 'description': 'rock'}, 
'Token No89': {'name': 'hoppip', 'image_link': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/187.png', 'description': 'grass'}}


    def mint_token(self,MinterPublicKey):
        """At the beginning the minter is the owner"""
        if self.minting==True :
            if self.is_active() == True:
            
                if self.token_used < self.size: # If the collection has not reached its maximum capacity
                    
                    print("Minting")

                    # Token characteristics
                    token_key = f'Token No{self.token_used}'
                    token = self.tokens[token_key]
                    payload = {
                        'name': token['name'],
                        'image_link': token['image_link'],
                        'description': token['description'],
                    }
                    # h = hash(payload)
                    self.token_used += 1
                    print("Minted !")

                else:
                    print("Limit of tokens reached")
                
                self.change_ownership(self.CollectionOwner, MinterPublicKey)
                # if h:
                #     return h

                
            else:
                print("Minting is closed")
        else:
            print("Minting is closed")


    def change_ownership(self, publicKey, token_hash, ReceiverPublicKey):
        """The change_ownership is a function use to exchange token between users"""             
        print('ownership changed')
        return f'''
        I sent {token_hash} to {ReceiverPublicKey}
        '''
        
    
    

    def open_minting(self,publicKey, time_in_seconds):
        self.time_in_seconds = time_in_seconds
        self.start_time=timestamp.now()
        self.minting = True
        print("Minting is open")

    def is_active(self):
        if (timestamp.now() - self.start_time) < self.time_in_seconds:
            return True
        else:
            return False
        
        
    
    def display(self):
        output = {}
        for i, token in enumerate(self.tokens):
            output[f"Token No{i}"] = token
        return output
    




