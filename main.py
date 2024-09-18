from application import Application
from console import Console
from hospital import Hospital
from hospital_commands import HospitalCommands


if __name__ == "__main__":
    hospital = Hospital(patients=[0, 2])
    console = Console()
    hospital_commands = HospitalCommands(hospital, console)
    app = Application(hospital_commands, console)
    app.run()
