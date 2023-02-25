class EntityNotFoundError(Exception):
    def __init__(self, status_code:int=400, message:str="Entity not found"):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)
        
class Unauthorized(Exception):
    def __init__(self, status_code:int=401, message:str="User is unauthorized"):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)     
        
class  NotAcceptable(Exception):
    def __init__(self, status_code=406, message:str="Not Acceptable"):
        self.status_code = status_code
        self.message = message      
        super().__init__(self.message)