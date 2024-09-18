from hospital import Hospital


class HospitalCommands:

    def __init__(self, hospital: Hospital, console):
        self._hospital: Hospital = hospital
        self._console = console

    def get_patient_status(self):
        patient_id_as_text = self._console.input("Введите ID пациента: ")
        patient_id = int(patient_id_as_text)

        status = self._hospital.get_status(patient_id)

        self._console.print(f'Статус пациента: "{status}"')
