from unittest.mock import MagicMock

from hospital import Hospital


class TestHospitalCommands:

    def test_get_patient_status(self):
        hospital = Hospital(patients=[0,2])
        console = MagicMock()
        hospital_commands = HospitalCommands(hospital, console)

        console.input.return_value = 1

        hospital_commands.get_patient_status()

        console.input.assert_called_once_with('Введите ID пациента: ')
        console.print.assert_called_once_with('Статус пациента: "Тяжело болен"')

