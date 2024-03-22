from models.club import Club
from validators import Validator

class MembershipController:
    def __init__(self, db_controller):
        self.db_controller = db_controller
        self.validator = Validator(db_controller)
        


    def create_member(self, club_id, student_id):
        # Validate if the student is already a member
        if self.validator.validate_membership(club_id, student_id):
            return False  # Student is already a member
        # Add the student to the club membership
        else:
            self.db_controller.add_member(club_id, student_id)
        return True  # Student successfully added to the club
