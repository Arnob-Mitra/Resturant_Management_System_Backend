from datetime import datetime, timedelta
import jwt, os

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES', 30))
REFRESH_TOKEN_EXPIRE_MINUTES = int(os.environ.get('REFRESH_TOKEN_EXPIRE_MINUTES', 10080)) # 7 days
ALGORITHM = os.environ.get('ALGORITHM', "HS256")
SECRET_KEY = os.environ.get('SECRET_KEY', "secret_key")


def create_access_token(id, expires_time: int = None) -> str:
  """
  Used to create access token.
  """  
  if expires_time is not None:
    expires_time = datetime.utcnow() + timedelta(minutes=expires_time)
  else:
    expires_time = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  
  to_encode = {"exp": expires_time, "id": str(id)}
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
  return encoded_jwt

def create_refresh_token(id, expires_time: int = None) -> str:
  """
  Used to create refresh token.
  """    
  if expires_time is not None:
    expires_time = datetime.utcnow() + timedelta(minutes=expires_time)
  else:
    expires_time = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
  
  to_encode = {"exp": expires_time,"id": str(id)}
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
  return encoded_jwt
