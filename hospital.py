class Hospital:

    def __init__(self, patients):
        self._patients = patients

    def get_status(self, patient_id):
        patient_idx = patient_id - 1
        return self._patients[patient_idx]

    def status_up(self, patient_id):
        patient_idx = patient_id - 1
        self._patients[patient_idx] += 1
