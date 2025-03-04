from certificate import Certificate

class SmartContractDefinition(Certificate):
    @staticmethod
    def get_smart_contract_at_current_state(blockchain, targetSmartContractHash):
        Operations = []
        for block in blockchain.blockList:
            print(block.display())
            for certificate in block.certificateList:
                if isinstance(certificate, SmartContractDefinition):
                    certificate = certificate.instantiate_contract()
                    for block2 in blockchain.blockList:
                        for certificate2 in block2.certificateList:
                            if isinstance(certificate2, SmartContractWritingOperation) and certificate2.targetSmartContractHash == targetSmartContractHash:
                                Operations.append(certificate2)
                    
                    sorted(Operations, key=lambda x: x.timestamp)
                    for operation in Operations:
                        operation.apply_on_contract(certificate)
                    return certificate
        return None

    def __init__(self, issuerPublicKey, smartContract):
        super().__init__(issuerPublicKey)
        self.sourceCode = smartContract

    def build_payload(self):
        payload = super().build_payload()
        payload['sourceCode'] = self.sourceCode
        return payload

    def instantiate_contract(self):
        exec(self.sourceCode)
        return locals()['SmartContract'](self.issuerPublicKey)



class SmartContractWritingOperation(Certificate):
    def __init__(self, issuerPublicKey, targetSmartContractHash, targetFunctionName, functionArgumentList):
        super().__init__(issuerPublicKey)
        self.targetSmartContractHash = targetSmartContractHash
        self.targetFunctionName = targetFunctionName
        self.functionArgumentList = functionArgumentList
    
    def build_payload(self):
        payload = super().build_payload()
        payload['targetSmartContractHash'] = self.targetSmartContractHash
        payload['targetFunctionName'] = self.targetFunctionName
        payload['functionArgumentList'] = self.functionArgumentList
        return payload
    
    def apply_on_contract(self, contractPythonObject):
        applyfunction = getattr(contractPythonObject, self.targetFunctionName)
        return applyfunction(*[self.issuerPublicKey, f"{self.functionArgumentList[0]}"])
        


'''

class SmartContract:
    
    def __init__(self, ownerPublicKey):
        self.messages = []
        
    def write_message(self, callerPublicKey, message):
        displayedName = callerPublicKey[256:264]
        self.messages.append(f'[{displayedName}] {message}')
        
    def display_chat(self):
        for message in self.messages:
            print(message)

'''
