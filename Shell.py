import time

import pyautogui
import keyboard

class TarkovShell():
    def __init__(self):
        self.region1 = (1247, 61, 1919, 1079)
        self.region2 = (1669, 128, 1880 ,220)
        self.region3 = (746, 427, 1165, 659)
        self.confidence = 0.9

    def goIntoMarket(self, ammoimage, ammoname):
        ammoLoc = pyautogui.locateCenterOnScreen(ammoimage, region=self.region1, confidence=self.confidence)
        if ammoLoc is None:
            print("请将 " + ammoname + "子弹放置一个与仓库界面可见处")
        else:
            pyautogui.click(x=ammoLoc.x, y=ammoLoc.y, button='right', clicks=1)
            time.sleep(0.2)
            searchForItem = pyautogui.locateCenterOnScreen('./image/search_for_item.png', region=self.region1, confidence=self.confidence)
            pyautogui.click(x=searchForItem.x, y=searchForItem.y, button='left', clicks=1)
            time.sleep(1)
            self.buying(ammoname)

    def buying(self, ammoname):
        Yesinventory = pyautogui.locateCenterOnScreen('./image/Yes_inventory.png', region=self.region2, confidence=self.confidence)
        if Yesinventory is not None:
            pyautogui.click(x=Yesinventory.x, y=Yesinventory.y, button='left', clicks=1)
            time.sleep(0.5)
            chooseAll = pyautogui.locateCenterOnScreen('./image/All.png', region=self.region3, confidence=self.confidence)
            pyautogui.click(x=chooseAll.x, y=chooseAll.y, button='left', clicks=1)
            time.sleep(0.5)
            confirmBuying = pyautogui.locateCenterOnScreen('./image/yes.png', region=self.region3,
                                                       confidence=self.confidence)
            pyautogui.click(x=confirmBuying.x, y=confirmBuying.y, button='left', clicks=1)
            time.sleep(1)
            pyautogui.press('esc')
            time.sleep(0.5)
            print(ammoname + " 子弹购买成功")
        else:
            pyautogui.press('esc')
            time.sleep(0.5)
            print(ammoname + " 子弹缺货")


    def Ammo7N31(self, flag):
        if flag == 2:
            self.goIntoMarket('./image/7N31.png', "7N31")
        else:
            return

    def Ammo995(self, flag):
        if flag == 2:
            self.goIntoMarket('./image/995.png', "995")
        else:
            return

    def Ammo855A1(self, flag):
        if flag == 2:
            self.goIntoMarket('./image/855A1.png', "855A1")
        else:
            return

    def AmmoAPSX(self, flag):
        if flag == 2:
            self.goIntoMarket('./image/AP_SX.png', "APSX")
        else:
            return

    def AmmoM61(self, flag):
        if flag == 2:
            self.goIntoMarket('./image/M61.png', "M61")
        else:
            return

    def AmmoSS190(self, flag):
        if flag == 2:
            self.goIntoMarket('./image/SS190.png', "SS190")
        else:
            return

    def ShellM381(self, flag):
        if flag == 2:
            self.goIntoMarket('./image/M381.png', "M381")
        else:
            return

    def AmmoBS(self, flag):
        if flag == 2:
            self.goIntoMarket('./image/BS.png', "BS")
        else:
            return

    def CardLabWhite(self, flag):
        if flag == 2:
            self.goIntoMarket('./image/Lab_white.png', "LabWhite")
        else:
            return

    def listener(self, flags):
        while True:
            self.Ammo7N31(flags[0])
            self.Ammo995(flags[1])
            self.Ammo855A1(flags[2])
            self.AmmoAPSX(flags[3])
            self.AmmoM61(flags[4])
            self.AmmoSS190(flags[5])
            self.ShellM381(flags[6])
            self.AmmoBS(flags[7])
            self.CardLabWhite(flags[8])
            time.sleep(5)

if __name__ == "__main__":
    TarkovShell().listener()