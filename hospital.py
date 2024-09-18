class Hospital:

    def __init__(self, patients):
        self._patients = patients

    def get_status(self, patient_id):
        patient_idx = patient_id - 1
        return self._patients[patient_idx]
