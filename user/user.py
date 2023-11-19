class user:
  def __init__(self,id,name, username,emailId,contact,totalSessions,firebase_id,firebase_name,firebase_email,firebase_password,credits,role_id,is_online,is_busy,is_call,is_chat):
    self.id = id
    self.name = name
    self.username = username
    self.email = emailId
    self.mobile = contact
    self.totalSessions = totalSessions
    self.firebase_id=firebase_id
    self.firebase_name=firebase_name
    self.firebase_email= firebase_email
    self.firebase_password=firebase_password
    self.credits=credits
    self.role_id=role_id
    self.online=is_online
    self.is_busy=is_busy
    self.is_call=is_call
    self.is_chat=is_chat
