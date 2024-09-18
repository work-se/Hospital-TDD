class TestHospital:

    def test_get_patient_status(self):
        hospital = Hospital([0, 1])

        status = hospital.get_status(patient_id=2)

        assert status == 1, "Получен неверный статус пациента"
