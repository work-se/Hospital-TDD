from hospital import Hospital


class TestHospital:

    def test_get_patient_status(self):
        hospital = Hospital([0, 1])

        status = hospital.get_status(patient_id=2)

        assert status == "Болен", "Получен неверный статус пациента"

    def test_status_up(self):
        hospital = Hospital([2, 0])

        hospital.status_up(patient_id=1)

        assert hospital._patients == [3, 0], "После повышения статуса в больнице пациенты оказались в неверных статусах"
