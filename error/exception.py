class EntityNotFoundError(Exception):
    def __init__(self, status_code:int=400, message:str="Entity not found"):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)