# from app.models import User
# from app import app, db
# import hashlib
#
#
# # def add_user(name, email, password, avatar=None, verification=True):
# #     if not exist_user(email):
# #         patient = Patient(name=name, email=email, avatar=avatar)
# #         db.session.add(patient)
# #     else:
# #         if Patient.query.filter(Patient.email == email).first():
# #             patient = Patient.query.filter(Patient.email == email).first()
# #         else:
# #             customer = Customer.query.filter(Customer.email == email).first()
# #             patient = customerToPatient(customer, avatar)
# #
# #     password = create_password(email, password)
# #     account_patient = AccountPatient(email=patient.email, password=password, patient=patient)
# #     db.session.add(account_patient)
# #
# #     # send the link to user via Gmail
# #     if email_verification(email):
# #         db.session.commit()
# #         return True
# #
# #     return False