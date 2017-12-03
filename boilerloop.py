import time
import gmailhelper
import config
import controlrelay
GMAIL_LABEL_CURRENT_TEMPERATURE = "currenttemp"
GMAIL_LABEL_TARGET_TEMPERATURE = "targettemp"
#connect to gmail
def heater_start():
    controlrelay.trigger_relay_on()
    print "HEATING ON\n"
def heater_stop():
    controlrelay.trigger_relay_off()
    print "HEATING OFF\n"

def get_current_temperature():
    try:
        return float(gmailhelper.get_subject_from_mail(gmailhelper.get_last_gmail_from_label(config.GMAIL_LABEL_CURRENT_TEMPERATURE)))
    except Exception, e:
        target_temperature=config.DEFAULT_TEMP
        print "error getting current temperature" + str(e)

def get_target_temperature():
    try:
        return float(gmailhelper.get_subject_from_mail(gmailhelper.get_last_gmail_from_label(config.GMAIL_LABEL_TARGET_TEMPERATURE)))
    except Exception, e:
        target_temperature=config.DEFAULT_TEMP
        print "error getting target temperature" + str(e)

def main():
    controlrelay.set_gpio()
    while True:
        current_temperature = get_current_temperature()
        print current_temperature
        target_temperature = get_target_temperature()
        print target_temperature
        if (current_temperature <= target_temperature):
            heater_start()
        else:
            heater_stop()
        time.sleep(5)

if __name__ == "__main__":
    main()
