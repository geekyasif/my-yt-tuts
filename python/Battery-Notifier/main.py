# pip install plyer
# pip install psutil

import psutil
from plyer import notification


battery = psutil.sensors_battery()
plugged = battery.power_plugged

if __name__ == '__main__':
    if plugged:
        percent  = battery.percent
        if percent <= 80:
            notification.notify(
                #title of notification
                title  = "Plugged In",

                #message of notification
                message = "For battery life, charge upto 80%"
            )

        elif percent == 100:
            notification.notify(
                title = "Plugged In",
                message = "Please Plugged out the charger, Battery is charged"
            )

        else:
            notification.notify(
                title = "Plugged In",
                message  = "Remove the charger please, for battery life charge upto 80%"
            )

    else:
        percent = battery.percent
        if percent <= 20:
            notification.notify(
                title = "Battery Reminder",
                message = "Your battery is running low. You might want to plug."
            )

        elif percent <= 50:
            notification.notify(
                title = "Battery Reminder",
                message = f"Battery is {percent}"
            )

        elif percent == 100:
            notification.notify(
                title = "Battery Reminder",
                message = "Your Battery is fully charged"
            )
        else:
            notification.notify(
                title = "Battery Reminder",
                message = f"Battery is {percent}",
                timeout = 3
            )


















