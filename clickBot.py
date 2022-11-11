import pyautogui as pyg
import webbrowser as wb
import datetime
import time
# import pillow
import click


# functions to format date, time
def format_date(x):
    date_list = x.split(sep="-")
    return list(map(int, date_list))

def format_time(x):
    time_list = x.split(sep="-")
    return list(map(int, time_list))

def given_datetime(given_date, given_time):

    # YY, MM, DD, HH, MM
    return datetime.datetime(given_date[2], given_date[1], given_date[0], given_time[0], given_time[1], given_time[2])


# join the meeting
def join_meeting(zoom_link, meeting_date, meeting_time):

    meeting_date_x = format_date(meeting_date)
    meeting_time_x = format_time(meeting_time)
    required_datetime = given_datetime(meeting_date_x, meeting_time_x)

    # time difference between current and meeting time
    wait_time_sec = (required_datetime - datetime.datetime.now().replace(microsecond=0)).total_seconds()
    print("Your ZOOM meeting starts in " + str(wait_time_sec/60) + " min")
    time.sleep(wait_time_sec)

    # zoom app related
    wb.get(using='chrome').open(zoom_link, new=2) #open zoom link in a new window
    time.sleep(5) # given time for the link to show app top-up window
    pyg.click(x=805, y=254, clicks=1, interval=0, button='left') # click on open zoom.app option
    time.sleep(10) # wait for 10 sec
    pyg.click(x=195, y=31, clicks=1, interval=0, button='left') # maximize zoom app
    time.sleep(3) # wait for 3 sec
    pyg.click(x=50, y=776, clicks=1, interval=0, button='left')

def printPos():
    # ! python3
    import pyautogui, sys
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')

button = pyg.locateOnScreen('power.png',confidence=0.7)
pyg.moveTo(button.left,button.top,2)
pyg.click()
time.sleep(2)

# button2 = pyg.locateOnScreen('zoom.png',confidence=0.7)
# pyg.moveTo(button2.left, button2.top,2)
# pyg.click(clicks=2)
#
time.sleep(70)
button3 = pyg.locateOnScreen('realPlay.png',confidence=0.7)
pyg.moveTo(button3.left, button3.top,2)
pyg.click(clicks=2)

# time.sleep(2)