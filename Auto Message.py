import pyautogui as auto

msg = input('Enter Your Text Here: ')
num_of_msg = int(input('How Many Message You Want To Sent? : '))
auto.sleep(5)
i = 0
while i < num_of_msg:
    auto.typewrite(msg)
    auto.press('enter')
    i = i + 1


