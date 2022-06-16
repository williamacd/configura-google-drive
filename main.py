import time
import pyautogui
import os
import easygui
import cv2

def detect_darkmode_in_windows():
    try:
        import winreg
    except ImportError:
        return False
    registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    reg_keypath = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize'
    try:
        reg_key = winreg.OpenKey(registry, reg_keypath)
    except FileNotFoundError:
        return False

    for i in range(1024):
        try:
            value_name, value, _ = winreg.EnumValue(reg_key, i)
            if value_name == 'AppsUseLightTheme':
                return value == 0
        except OSError:
            break
    return False

Tema = "White"

if detect_darkmode_in_windows():
    Tema = "Dark"

GDriveIco = pyautogui.locateCenterOnScreen(Tema + "\\logo.png", confidence=0.7)
time.sleep(1)
pyautogui.leftClick(GDriveIco)

pyautogui.hotkey("win", "m")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("space")
time.sleep(1)
GDriveIco = pyautogui.locateCenterOnScreen(Tema + "\\logo.png", confidence=0.7)
time.sleep(1)
pyautogui.leftClick(GDriveIco)
GDrivePref = pyautogui.locateCenterOnScreen(Tema + "\\logo2.png", confidence=0.7)
time.sleep(1)
pyautogui.leftClick(GDrivePref)
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
GDriveBtn = pyautogui.locateCenterOnScreen(Tema + "\\btn.png", confidence=0.7)
time.sleep(1)
pyautogui.leftClick(GDriveBtn)
time.sleep(1)

quantidade = 0

perfil = os.getenv("USERPROFILE")
for diretorio in ["\\3D Objects", "\\Contacts", "\\Desktop", "\\Documents", "\\Downloads", "\\Favorites", "\\Links",
                    "\\Music", "\\Pictures", "\\Saved Games", "\\Searches", "\\Videos"]:
    quantidade = quantidade + 1

for diretorio in ["\\3D Objects", "\\Contacts", "\\Desktop", "\\Documents", "\\Downloads", "\\Favorites", "\\Links",
                    "\\Music", "\\Pictures", "\\Saved Games", "\\Searches", "\\Videos"]:
    caminhocompleto = perfil+diretorio
    pyautogui.write(caminhocompleto)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    GDriveCon = pyautogui.locateCenterOnScreen(Tema + "\\concluido.png", confidence=0.7)
    time.sleep(1)
    pyautogui.leftClick(GDriveCon)
    time.sleep(1)
    GDriveAdd = pyautogui.locateCenterOnScreen(Tema + "\\addPasta.png", confidence=0.7)
    time.sleep(1)
    quantidade = quantidade - 1
    if quantidade != 0:
        pyautogui.leftClick(GDriveAdd)
        time.sleep(1)
    else:
        GDriveSalvar = pyautogui.locateCenterOnScreen(Tema + "\\salvar.png", confidence=0.7)
        pyautogui.leftClick(GDriveSalvar)

easygui.msgbox("Google drive configurado com sucesso. Gentileza validar!!", title="Configuração concluida")
