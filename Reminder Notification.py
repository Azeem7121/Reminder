import time
from plyer import notification

"""To run in background open terminal in path of file and type pythonw.exe press enter now type .\filename.py"""
if __name__ == '__main__':
    while True:
        notification.notify(
            title="Drink some Water",
            message="DAILY WATER REQUIREMENT . Human body requires at least 2-2.5 litres of water per day. Various "
                    "foods that are high in water content add to the quantity of water consumed."
                    "drink at least1.5-2 litres water to meet the body’s ...",
            app_icon="D:\\Python\\Learn Python\\glass.ico",
            timeout=10  # visible for 10 secs
        )
        time.sleep(60 * 60)
