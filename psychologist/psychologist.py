class psychologist:
  def __init__(self,id,name,profile_image,is_busy,firebase_id,firebase_name,firebase_email,firebase_password,uuid,
      user_id, description,session_count,rating,
               yrs_of_exp,education,short_desc,status,order,created_at
               ,updated_at,gender,age,interests,languages,online,contact,is_call,is_chat,delta,lastSeen):
    self.id = id
    self.name = name
    self.profile_image = profile_image
    self.is_busy = is_busy
    self.firebase_id = firebase_id
    self.firebase_name = firebase_name
    self.firebase_email = firebase_email
    self.firebase_password = firebase_password
    self.uuid = uuid
    self.user_id = user_id
    self.description = description
    self.session_count = session_count
    self.rating = rating
    self.yrs_of_exp = yrs_of_exp
    self.education = education
    self.short_desc = short_desc
    self.status = status
    self.order_ = order
    self.created_at = created_at
    self.updated_at = updated_at
    self.gender = gender
    self.age = age
    self.interests = interests
    self.languages = languages
    self.online = online
    self.contact = contact
    self.is_call = is_call
    self.is_chat = is_chat
    self.delta= delta
    self.lastSeen=lastSeen


# will take contact , is_Call and is_chat to psychologist table in furute