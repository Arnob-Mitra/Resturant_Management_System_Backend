from datetime import datetime, timedelta
import jwt, os

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES', 30)) #ABCDEF the access token will be expired within 30 mins
REFRESH_TOKEN_EXPIRE_MINUTES = int(os.environ.get('REFRESH_TOKEN_EXPIRE_MINUTES', 10080)) #ABCDEF refresh token will be expired within 7 days
ALGORITHM = os.environ.get('ALGORITHM', "HS256") #ABCDEF the algorithm assumes as HS256
SECRET_KEY = os.environ.get('SECRET_KEY', "secret_key") #ABCDEF the SECRET KEY assumes as secret key 


def create_access_token(id, expires_time: int = None) -> str: #ABCDEF this function's return type is str
  """
  Used to create access token.
  """  
  if expires_time is not None:  
    expires_time = datetime.utcnow() + timedelta(minutes=expires_time) #ABCDEF expires time will be the summation of the current date-time and expiration time
  else:
    expires_time = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) #ABCDEF expires time will be the summation of the current date-time and access time (30 mins)
  
  to_encode = {"exp": expires_time, "id": str(id)}
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM) #ABCDEF encode with expires time, id, secret key and algorithm 
  return encoded_jwt

def create_refresh_token(id, expires_time: int = None) -> str: #ABCDEF this function's return type is str
  """
  Used to create refresh token.
  """    
  if expires_time is not None:
    expires_time = datetime.utcnow() + timedelta(minutes=expires_time) #ABCDEF expires time will be the summation of the current date-time and expiration time
  else:
    expires_time = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES) #ABCDEF expires time will be the summation of the current date-time and refresh time (7 days)
  
  to_encode = {"exp": expires_time,"id": str(id)}
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM) #ABCDEF encode with expires time, id, secret key and algorithm 
  return encoded_jwt