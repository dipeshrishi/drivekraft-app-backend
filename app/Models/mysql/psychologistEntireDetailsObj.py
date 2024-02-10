class psychologistEntireDetailsObj:
    def __init__(self, id, session_count, rating, preference_order, is_busy, status, online, last_seen,
                 missed_request_count, total_requests_received_count, firebase_id, firebase_name,
                 firebase_email, firebase_password, psychologist_id, psychologist_uuid, psychologist_name,
                 psychologist_user_id, psychologist_profile_image, psychologist_contact_number,
                 psychologist_email_id, psychologist_enabled, psychologist_description,
                 psychologist_short_description, psychologist_years_of_exp, psychologist_education,
                 psychologist_gender, psychologist_age, psychologist_interest, psychologist_language):
        self.id = id
        self.session_count = session_count
        self.rating = rating
        self.preference_order = preference_order
        self.is_busy = is_busy
        self.status = status
        self.online = online
        self.last_seen = last_seen
        self.missed_request_count = missed_request_count
        self.total_requests_received_count = total_requests_received_count
        self.firebase_id = firebase_id
        self.firebase_name = firebase_name
        self.firebase_email = firebase_email
        self.firebase_password = firebase_password

        self.psychologist = {
            'id': psychologist_id,
            'uuid': psychologist_uuid,
            'name': psychologist_name,
            'userId': psychologist_user_id,
            'profile_image': psychologist_profile_image,
            'contactNumber': psychologist_contact_number,
            'emailId': psychologist_email_id,
            'enabled': psychologist_enabled,
            'description': psychologist_description,
            'shortDescription': psychologist_short_description,
            'yearsOfExp': psychologist_years_of_exp,
            'education': psychologist_education,
            'gender': psychologist_gender,
            'age': psychologist_age,
            'interest': psychologist_interest,
            'language': psychologist_language
        }