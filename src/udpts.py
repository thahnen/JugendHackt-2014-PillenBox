# UnbelievableDirtyPythonTimingSolution
# Dieses Script wird stündlich per Cronjob aufgerufen,
# läd die Konfigurationsdatei und prüft, ob für die aktuelle Stunde eine
# Abgabe vorgesehen ist. Ist dies der Fall ruft es das Controll-Skript auf,
# wartet die Statusmeldung dieser ab und meldet diese an den Server.
import time
import control
import sys
import logging
logging.basicConfig(filename='udpts.log', level=logging.DEBUG)
apiurl = "localhost"
logpath = "udpts.log"
log = open(logpath, "a")

try:
    config = open(configpath, "r")
    for line in config:
        einheit = line.split(",")
        if (time.localtime[tm_hour] == int(einheit[0])):
            dosis = int(einheit[1])
            break
except:
    logging.error("Error while Parsing")
    sys.exit(1)
control.dispense(dosis)
logging.info("Ordered " + dosis + " pills.")
sys.exit(0)
