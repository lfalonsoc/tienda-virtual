import os

from dotenv import load_dotenv

class Config:
  SECRET_KEY=os.environ.get('SECRECT_KEY','')
  DEBUG=True

  TEMPLATE_FOLDER='views/templates/'
  STATIC_FOLDER='views/static/'