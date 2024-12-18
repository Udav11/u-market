import keyboard
import time
import pyautogui as pyg
import pyperclip
import os


def check_items():
    pyg.click(1331, 271, duration=0.75)
    pyg.click(720, 269, duration=0.75)
    print('Проверяю инвентарь')
    time.sleep(0.5)
    pyg.click(1630, 968, duration=0.75)  # собрать в кучу
    pyg.click(1595, 966, duration=0.75)  # сортировать
    time.sleep(0.5)
    print('Проверяю наличие зелий')
    coords = []
    try:
        coords = pyg.locateOnScreen(r'.\Full.png', region=(1551, 500, 72, 37))
    except pyg.ImageNotFoundException:
        print('Зелий нет')
    if len(coords) > 0:
        print('Зелья найдены')
        auc_check()


def auc_check(delay=1.5):
    time.sleep(delay)
    print('Проверяю есть ли ордер')
    pyg.click(1383, 576, duration=0.75)  # клик по мои заказы
    time.sleep(2)
    coords = []
    try:
        coords = pyg.locateOnScreen(
            r'.\zakaz.png', region=(1170, 690, 115, 48))
    except pyg.ImageNotFoundException:
        print('Ордера нет, проверяю инвентарь')
        pyg.click(1630, 968, duration=0.75)  # собрать в кучу
        pyg.click(1595, 966, duration=0.75)  # сортировать
        try:
            coords = pyg.locateOnScreen(
                r'.\Full.png', region=(1551, 500, 72, 37))
        except pyg.ImageNotFoundException:
            print('Ордера нет, зелий нет - это победа.')
            return
            #os.system('shutdown /s /f /t 0')  # конец функции
        auc_sell()
    print('Ордер имеется, ждем продажи.')
    while True:
        pyg.click(1317, 624, duration=0.75)  # кнопка обновить
        order_check()
        time.sleep(60)
        try:
            coords_2 = pyg.locateOnScreen(
                r'.\zakaz.png', region=(1170, 690, 115, 48))
        except pyg.ImageNotFoundException:
            print('Ордера больше нет, делаю ордер')
            auc_sell()
            break


def order_check():
    print('Проверяю инвентарь на наличие зелий')
    pyg.click(1630, 968, duration=0.75)  # собрать в кучу
    pyg.click(1595, 966, duration=0.75)  # сортировать
    coords = []
    try:
        coords = pyg.locateOnScreen(r'.\Full.png', region=(1551, 500, 72, 37))
    except pyg.ImageNotFoundException:
        print('Зелий нет, удаляю старый ордер')
        pyg.click(1307, 706, duration=0.75)  # кнопка отменить
        time.sleep(1)
        pyg.click(1386, 732, duration=0.75)  # забрать ордер
        pyg.click(1270, 870, duration=0.75)  # забрать все
        time.sleep(2)
        auc_sell()
    print('Зелья все еще есть')
    pyg.click(1215, 708, duration=0.75)  # редактировать
    time.sleep(2)
    try:
        check_pixel = pyg.pixelMatchesColor(1083, 374, (105, 117, 34))
        if not check_pixel:
            raise pyg.ImageNotFoundException
    except pyg.ImageNotFoundException:
        print('Ордер не на первом месте, получаю актуальную цену')
        pyg.click(933, 309, duration=0.75)  # закрыть окно
        pyg.click(1385, 333, duration=0.75)  # окно купить
        pyg.click(645, 270, duration=0.75)  # окно поиска
        time.sleep(1)
        name = 'зелье гиганта'
        pyperclip.copy(name)
        pyg.hotkey('ctrl', 'v')
        time.sleep(1)
        pyg.click(951, 278, duration=0.75)  # окно тиров
        pyg.click(959, 482, duration=0.75)  # тир 7
        time.sleep(1)
        pyg.click(1264, 426, duration=0.75)  # 1 ордер
        pyg.click(653, 515, duration=0.75)  # заказ на продажу
        pyg.click(562, 632, duration=0.75)  # демпим на 1 серебро
        pyg.click(646, 633, duration=0.75)  # окошко цены
        time.sleep(1)
        pyg.hotkey('ctrl', 'c')  # копируем ценник
        pyg.click(939, 309)  # закрыть ордер
        print('Получил актуальную цену, демплю')
        pyg.click(1383, 576, duration=0.75)  # мои заказы
        time.sleep(1)
        pyg.click(1215, 708, duration=0.75)  # редактировать
        time.sleep(1)
        pyg.click(847, 578, duration=0.75)  # клик по кол-ву на продажу
        pyg.write('100')  # пишем кол-во на продажу
        time.sleep(1)
        pyg.click(646, 633, duration=0.75)  # окошко цены
        pyg.hotkey('ctrl', 'v')  # вставляем ценник
        pyg.click(880, 730, duration=0.75)  # обновить/сделать заказ
        print('Задемплено')
        auc_check(60)
    print('Наш ордер не нужно демпить')
    pyg.click(933, 309, duration=0.75)


def auc_sell():
    print('Делаю ордер')
    time.sleep(0.5)
    pyg.click(1383, 410, duration=0.75)  # меню продать
    pyg.click(1263, 429, duration=0.75)  # клик по кнопке продать
    pyg.click(562, 632, duration=0.75)  # демпим на 1 серебро
    pyg.click(847, 578, duration=0.75)  # клик по кол-ву на продажу
    pyg.write('100')  # пишем кол-во на продажу
    time.sleep(1)
    pyg.click(880, 730, duration=0.75)  # клик по сделать заказ
    auc_check(60)


check_button = False
print('Открой аук во вкладке продать и открой инвентарь')
while not check_button:
    start_button = input('Нажми Y для старта \n')
    if start_button == 'y' or start_button == "Y":
        check_button = True
        check_items()
