from datetime import datetime

def create_update_doc(doc: dict):
  doc['updated_at'] = datetime.now()
  return doc