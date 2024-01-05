from typing import List
from app.Models.mysql import psychologistEntireDetailsObj

class allPsychologistResponse:
    def __init__(self, psychologist_data_list: List[psychologistEntireDetailsObj]):
        self.psychologist_data_list = psychologist_data_list