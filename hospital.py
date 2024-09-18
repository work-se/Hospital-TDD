class Hospital:

    def __init__(self, patients):
        self._patients = patients

    def get_status(self, patient_id):
        patient_idx = patient_id - 1
        statuses_code_to_title_mapping = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}
        patient_status_code = self._patients[patient_idx]
        return statuses_code_to_title_mapping[patient_status_code]

    def status_up(self, patient_id):
        patient_idx = patient_id - 1
        self._patients[patient_idx] += 1
