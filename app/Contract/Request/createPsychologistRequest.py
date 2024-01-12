
class createPsychologistRequest:
    def __init__(self,
                 name, profile_image,
                 contactNumber, emailId,
                 description, shortDescription, yearsOfExp,
                 education, gender, age, interest, language,
                 sessionCount, rating, preferenceOrder):
        self.name = name
        self.profile_image = profile_image
        self.contactNumber = contactNumber
        self.emailId = emailId
        self.description = description
        self.shortDescription = shortDescription
        self.yearsOfExp = yearsOfExp
        self.education = education
        self.gender = gender
        self.age = age
        self.interest = interest
        self.language = language
        self.sessionCount = sessionCount
        self.rating = rating
        self.preferenceOrder = preferenceOrder