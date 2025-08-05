import pygame
import pyautogui
import math

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

LBletters = ['r','t','q','w','e']
RBletters = ['o','p','y','u','i']
LBpTletters = ['f','g','a','s','d']
RBpTletters = ['l','h','j','k']
LTletters = ['c','v','z','x']
RTletters = ['m','b','n']
nums = ['6','7','8','9','0','1','2','3','4','5']
numsym = ['^','&','*','(',')','!','@','#','$','%']
sym = ["'",',','.','/','`','-',"=",'[',']',';']
shtsym = ['"','<','>','/','~','_','+','{','}',':']

def getAngle(x,y):
    return (math.degrees(math.atan2(y,x)) + 360) % 360

def getSelectedLetter(angle, letters):
    if letters != None:
        anglePerLetter = 360 / len(letters)
        ind = int(angle//anglePerLetter) % len(letters)
        return letters[ind]
    return None

def main():
    state = True
    LBl = False
    LTl = False
    LBpTl = False
    RBl = False
    RTl = False
    RBpTl = False
    numkey = False
    shiftky = False
    symkey = False
    Selectedletter = None
    SelectedLtrLst = None   

    # THE BELOW CODE IS ONLY VALID FOR Xinput ONLY. 
    while state:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 6:
                    print("Program Ending")
                    pygame.quit()
                    state = False
                elif event.button == 4:
                    LBl = True
                    if not shiftky:
                        SelectedLtrLst = LBletters
                        print("Activated menu: ", ['q','w','e','r','t'])
                    else:
                        SelectedLtrLst = list(map(str.upper, LBletters))
                        print("Activated menu: ", list(map(str.upper, LBletters)))
                elif event.button == 5:
                    RBl = True
                    if not shiftky:
                        SelectedLtrLst = RBletters
                        print("Activated Menu: ", ['y','u','i','o','p'])
                    else:
                        SelectedLtrLst = list(map(str.upper,RBletters))
                        print("Activated Menu: ", list(map(str.upper,['y','u','i','o','p'])))
                elif event.button == 1:
                    pyautogui.press('backspace')
                elif event.button == 3:
                    pyautogui.write(' ')
                # elif event.button == 0:
                #     pyautogui.press('enter')
                elif event.button == 2:
                    if not numkey:
                        numkey = True
                        if shiftky:
                            SelectedLtrLst = numsym
                            print("Activated menu: ",numsym)
                        else:
                            SelectedLtrLst = nums
                            print("Activated menu: ",[1,2,3,4,5,6,7,8,9,0])
                    else:
                        numkey = False
                        SelectedLtrLst = None
                        if shiftky:
                            print("Deactivated menu: ", numsym)
                        else:
                            print("Deacivated menu: ",[1,2,3,4,5,6,7,8,9,0])
                elif event.button == 9:
                    if not symkey:
                        symkey = True
                        if shiftky:
                            SelectedLtrLst = shtsym
                            print("ACtivated menu: ", ['~','_','+','{','}',':','"','<','>','?'])
                        else:
                            SelectedLtrLst = sym
                            print("Activated menu: ", ['`','-','=','[',']',';',"'",',','.','/'])
                    else:
                        symkey = False
                        SelectedLtrLst = None
                        if shiftky:
                            print("Deactivated Menu: ", ['~','_','+','{','}',':','"','<','>','?'])
                        else:
                            print("Deactivated Menu: ", ['`','-','=','[',']',';',"'",',','.','/'])


                elif event.button == 0 and LBl:
                    if Selectedletter != None:
                        pyautogui.write(Selectedletter)
                        Selectedletter = None
                    else:
                        print("Please Select a character.")
                elif event.button == 0 and RBl:
                    if Selectedletter != None:
                        pyautogui.write(Selectedletter)
                        Selectedletter = None
                    else:
                        print("Please Select a character.")
                elif event.button == 0 and LBpTl:
                    if Selectedletter != None:
                        pyautogui.write(Selectedletter)
                        Selectedletter = None
                    else:
                        print("Please Select a character.")
                elif event.button == 0 and RBpTl:
                    if Selectedletter != None:
                        pyautogui.write(Selectedletter)
                        Selectedletter = None
                    else:
                        print("Please Select a character.")
                elif event.button == 0 and LTl:
                    if Selectedletter != None:
                        pyautogui.write(Selectedletter)
                        Selectedletter = None
                    else:
                        print("Please Select a character.")
                elif event.button == 0 and RTl:
                    if Selectedletter != None:
                        pyautogui.write(Selectedletter)
                        Selectedletter = None
                    else:
                        print("Please Select a character.")


            elif event.type == pygame.JOYBUTTONUP:
                if event.button == 4:
                    LBl = False
                    SelectedLtrLst = None
                    if not shiftky:
                        print("Deactivated menu: ", ['q','w','e','r','t'])
                    else:
                        print("Deactivated menu: ", list(map(str.upper, ['q','w','e','r','t'])))
                elif event.button == 5:
                    RBl = False
                    SelectedLtrLst = None
                    if not shiftky:
                        print("Deactivated Menu: ", ['y','u','i','o','p'])
                    else:
                        print("Deactivated menu: ", list(map(str.upper, ['y','u','i','o','p'])))

            
            elif event.type == pygame.JOYHATMOTION:
                if joystick.get_hat(0)[1] == 1:
                    if not shiftky:
                        pyautogui.keyDown('shift')
                        shiftky = True
                        print("Shift key pressed")
                    else:
                        pyautogui.keyUp('shift')
                        shiftky = False
                        print("Shift key released")

            elif event.type == pygame.JOYAXISMOTION:
                if LBl or RBl or LTl or RTl or LBpTl or RBpTl or numkey:
                    x = round(joystick.get_axis(0), 1)  # Horizontal axis
                    y = round(joystick.get_axis(1), 1)  # Vertical axis
                    if abs(x) > 0.2 and abs(y) > 0.2:
                        angle = getAngle(x, y)
                        Selectedletter = getSelectedLetter(angle, SelectedLtrLst)
                        print(f"Selected letter: {Selectedletter}")

                if joystick.get_axis(4) > 0.5 and joystick.get_button(4):
                    if not LBpTl:
                        LBpTl = True
                        if not shiftky:
                            SelectedLtrLst = LBpTletters
                            print("Activated menu: ", ['a','s','d','f','g'])
                        else:
                            SelectedLtrLst = list(map(str.upper, LBpTletters))
                            print("Activated menu: ", list(map(str.upper, ['a','s','d','f','g'])))
                    else:
                        pass
                elif joystick.get_axis(5) > 0.5 and joystick.get_button(5):
                    if not RBpTl:
                        RBpTl = True
                        if not shiftky:
                            SelectedLtrLst = RBpTletters
                            print("Activated menu: ", ['h','j','k','l'])
                        else:
                            SelectedLtrLst = list(map(str.upper, RBpTletters))
                            print("Activated menu: ", list(map(str.upper, ['h','j','k','l'])))
                    else:
                        pass
                elif abs(joystick.get_axis(4)) < 0.1 and not joystick.get_button(4):
                    if LBpTl:
                        LBpTl = False
                        SelectedLtrLst = None
                        if not shiftky:
                            print("Deactivated menu: ", ['a','s','d','f','g'])
                        else:
                            print("Deactivated menu: ", list(map(str.upper, ['a','s','d','f','g'])))
                    else:
                        pass
                elif abs(joystick.get_axis(5)) < 0.1 and not joystick.get_button(5):
                    if RBpTl:
                        RBpTl = False
                        SelectedLtrLst = None
                        print("Deactivated menu: ", ['h','j','k','l',';'])
                    else:
                        pass

                if joystick.get_axis(4) > 0.5:
                    if not LBpTl and not LTl:
                        LTl = True
                        if not shiftky:
                            SelectedLtrLst = LTletters
                            print("Activated Menu: ", ['z','x','c','v'])
                        else:
                            SelectedLtrLst = list(map(str.upper, LTletters))
                            print("Activated Menu: ", list(map(str.upper, ['z','x','c','v'])))
                    else:
                        pass
                elif joystick.get_axis(5) > 0.5:
                    if not RBpTl and not RTl:
                        RTl = True
                        if not shiftky:
                            SelectedLtrLst = RTletters
                            print("Activated Menu: ", ['b','n','m'])
                        else:
                            SelectedLtrLst = list(map(str.upper, RTletters))
                            print("Activated Menu: ", list(map(str.upper, ['b','n','m'])))
                    else:
                        pass
                elif abs(joystick.get_axis(4)) < 0.1:  
                    if LTl:
                        LTl = False
                        SelectedLtrLst = None
                        print("Deactivated Menu: ", ['z','x','c','v'])
                    else:
                        pass
                elif abs(joystick.get_axis(5)) < 0.1:  
                    if RTl:
                        RTl = False
                        SelectedLtrLst = None
                        print("Deactivated Menu: ", ['b','n','m',','])
                    else:
                        pass

'''
For Xinput:-
KEYS ARE:-
0 = A, 1 = B, 2 = X, 3 = Y, 4 = LB, 5 = RB, 6 = BACK, 7 = START, 8 = LAS, 9 = RAS, 10 = Logitech button
AXES ARE:-
0 = L hori, 1 = L verti, 2 = R Hori, 3 = R Verti, 4 = LT, 5 = RT

For DirectInput:-
KEYS ARE:-
0 = A, 1 = B, 2 = X, 3 = Y, 4 = LB, 5 = RB, 6 = LT, 7 = RT, 8 = BACK, 9 = START, 10 = LAS, 11 = RAS, NO BUTTON VALUE = Logitech button
AXES ARE:-
0 = L hori, 1 = L verti, 2 = R Hori, 3 = R Verti

'''

print("Prog running")
main()