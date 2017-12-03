import time
import gmailhelper
import config
import controlrelay
import logging

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('boilerloop.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def heater_start():
    controlrelay.trigger_relay_on()
    logger.info("HEATING ON\n")
def heater_stop():
    controlrelay.trigger_relay_off()
    logger.info("HEATING OFF\n")

def get_target_temperature():
    try:
        lastemail = gmailhelper.get_last_gmail_from_label(config.GMAIL_LABEL_TARGET_TEMPERATURE)
        subject = gmailhelper.get_mail_subject(lastemail)
        fromemail = gmailhelper.get_mail_from_mail(lastemail)
        if fromemail == config.GMAIL_FROM_CALENDAR:
            target_temperature = float(subject.split()[1])
        else:
            target_temperature = float(subject)
        return target_temperature
    except Exception, e:
        target_temperature=config.DEFAULT_TEMP
        logger.error("error getting current temperature" + str(e))

def get_current_temperature():
    try:
        return float(gmailhelper.get_mail_subject(gmailhelper.get_last_gmail_from_label(config.GMAIL_LABEL_CURRENT_TEMPERATURE)))
    except Exception, e:
        target_temperature=config.DEFAULT_TEMP
        logger.error("error getting target temperature" + str(e))

def main():
    controlrelay.set_gpio()
    while True:
        current_temperature = get_current_temperature()
        logger.debug(current_temperature)
        target_temperature = get_target_temperature()
        logger.debug(target_temperature)
        if (current_temperature <= target_temperature):
            heater_start()
        else:
            heater_stop()
        time.sleep(5)

if __name__ == "__main__":
    main()
