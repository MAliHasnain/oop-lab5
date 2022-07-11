class Hospital :
    def __init__(self,name,address):
        self.name = name
        self.address = address
class Doctor(Hospital):
    def __init__(self,name,address,specialization):
        super().__init__(name,address)
        self.specialization = specialization
class Patient(Hospital):
    def __init__(self,name,address,disease,doctor):
        super().__init__(name,address)
        self.disease = disease
        self.doctor = doctor
class Medical_test(Patient):
    def __init__(self,name,address,disease,doctor,testno):
        super().__init__(name,address,disease,doctor)
        self.testno = testno
        self.test_status = "uninitialized"
    def DisplayReport(self):
        print(f"The name of patient is : {self.name}")
        print(f"The address of patient is : {self.address}")
        print(f"The disease of patient is : {self.disease}")
        print(f"The doctor of patient is : {self.doctor}")
        print(f"The test no.  of patient is : {self.testno}")
        print(f"The test status of patient is : {self.test_status}")
        if(self.test_status == "uninitialized"):
            print("The test is starting soon!!! ")
        else:
            print("The test is in progress or completed!!! ")
Abbas = Medical_test("Abbas Raza","survey 417","Cancer","Dr. Aun Raza ","2nd")
Abbas.DisplayReport()
