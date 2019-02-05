from hcc_esrd import Diagnosis, Beneficiary, ICDType, score, EntitlementReason
from pyDatalog import pyDatalog

jane = Beneficiary(hicno='0220F11E0B2EC004', sex='female', dob='19990601', age_upto= '20180201')
dx1 = Diagnosis(jane, "E1165", ICDType.TEN)
jane.add_diagnosis(dx1)
dx2 = Diagnosis(jane, "E118", ICDType.TEN)
jane.add_diagnosis(dx2)

pyDatalog.create_terms("X")
score(jane, "functioning_graft_new_enrolle", X)
print("X: %s" % X)

score(jane, "functioning_graft_new_enrolle", X)
print("X: %s" % X)

score(jane, "functioning_graft_new_enrolle", X)
print("X: %s" % X)


daniel = Beneficiary(hicno=1,sex="male",dob="19740824", original_reason_entitlement=EntitlementReason.DIB, age_upto='19990201')
daniel.add_diagnosis(Diagnosis(daniel,"A0223",ICDType.TEN))  # 51
daniel.add_diagnosis(Diagnosis(daniel,"A0224",ICDType.TEN))  # 52
daniel.add_diagnosis(Diagnosis(daniel,"D66",ICDType.TEN))
daniel.add_diagnosis(Diagnosis(daniel,"C163",ICDType.TEN))
daniel.add_diagnosis(Diagnosis(daniel,"C163",ICDType.TEN))
daniel.add_diagnosis(Diagnosis(daniel,"C182",ICDType.TEN))
daniel.add_diagnosis(Diagnosis(daniel,"C800",ICDType.TEN))
daniel.add_diagnosis(Diagnosis(daniel,"A072",ICDType.TEN))
score(daniel, "functioning_graft_new_enrolle", X)
print("Daniel functioning_graft_new_enrolle Score: %s" % X)