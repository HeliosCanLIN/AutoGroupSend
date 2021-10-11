import pyautogui,time
import yaml #读取yaml配置文件
import pyperclip #获取剪切板

def readConfig(): #读取配置文件
    # 打开yaml文件
    global config
    print("***获取配置文件数据***")
    file = open('config.yaml', 'r', encoding="utf-8")
    file_data = file.read()
    file.close()
    config = yaml.safe_load(file_data)

def UpLoad_File():
    pyperclip.copy(config['filePath'])  # 复制文件路径到剪切板
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.1)
    pyautogui.click(x=m/2, y=n/2, button='left')
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.1)
    pyautogui.press('enter')

def error(msg):
    print("ERROR - "+msg)
    pyautogui.confirm('ERROR - '+msg)
    exit(0)

if __name__ == '__main__':
    readConfig()

    pyautogui.confirm('请把whatsapp打开，将需要发送的消息写在config.yaml内，如需要中断程序，请将鼠标移动到左上角')
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = config['sleep']
    X = config['pointCx']
    Y = config['pointCy']
    m, n = pyautogui.size()
    isFirst=1
    if (config['testmode'] == '1'):
        time.sleep(3)
        print('*****************************************************测试模式*****************************************************')
        print('检查加号...')
        #print((pyautogui.locateOnScreen(config['adminPng'], grayscale=True, confidence=0.98, region=(1350, 780, 560, 70))== None or pyautogui.locateOnScreen('adminEn.png', grayscale=True, confidence=0.98, region=(1350, 780, 579, 70))== None))
        #print((pyautogui.locateOnScreen(config['adminPng'], grayscale=True, confidence=0.98, region=(1350, 780, 560, 70))== None or pyautogui.locateOnScreen('adminEn.png', grayscale=True, confidence=0.98, region=(1350, 780, 579, 70))== None) and pyautogui.locateOnScreen('+86.png', grayscale=True, region=(1350, 780, 560, 70))== None)
        # pointX, pointY = pyautogui.locateCenterOnScreen('more.png', grayscale=True, confidence=0.98)
        # pyautogui.click(pointX, pointY)
        #print(pyautogui.locateOnScreen('adminEn.png', grayscale=True, confidence=0.98, region=(1350, 780, 560, 70)))
        # print(len(list(pyautogui.locateAllOnScreen(config['plusPng'], grayscale=True,confidence=0.98))))
        if (pyautogui.locateOnScreen(config['plusPng'], grayscale=True, confidence=0.98,
                                     region=(int(m*(1/4)), int(n*0.027), int(m*(1/5)), int(n*0.046))) != None):
            print('已检测到加号')
        #    print('检查信息...')
        #if(pyautogui.locateOnScreen(config['msgPng'], grayscale=True,region=(1200, 90, 720, 880)) != None):
        #    print('已检测到信息')
        else:
            print('检测失败，退出')
            time.sleep(3)
            exit(0)
        print('检测通过，退出')
        time.sleep(3)
        exit(0)

    i = 0
    #total = int(input("输入人数\n>>>"))
    total = int(pyautogui.prompt('输入人数'))
    time.sleep(3)
    while (i < total):
        try:
            pointX, pointY = pyautogui.locateCenterOnScreen('top.png', grayscale=True, confidence=0.98)
        except:
            error("找不到置顶的群")
        pyautogui.click(pointX - 200, pointY)
        #pyautogui.click(x=config['pointAx'], y=config['pointAy'], button='left')
        try:
            pointX, pointY = pyautogui.locateCenterOnScreen('test.png', grayscale=True, confidence=0.98)
        except:
            error("尝试点击群聊失败")
        pyautogui.click(pointX + 200, pointY)
        #pyautogui.click(x=config['pointBx'], y=config['pointBy'], button='left')
        pyautogui.moveTo(x=X, y=Y, duration=0.2)
        pyautogui.scroll(-1500)
        #群成员操作
        if (isFirst == 1):
            time.sleep(1.5)
            try:
                X, Y = pyautogui.locateCenterOnScreen('more.png', grayscale=True, confidence=0.98)
            except:
                error("尝试展开群聊失败")
            skipNum = len(list(pyautogui.locateAllOnScreen(config['accountplusPng'], grayscale=True, region=(int(m*(2/3)), 0, int(m/2), n))))
            total = total - skipNum - 1
            i=i-skipNum
            isFirst=0
        pyautogui.click(x=X, y=Y,button='left')
        time.sleep(1)
        if(skipNum>i):
            pyautogui.scroll(config['row'] * skipNum)
            skipNum=skipNum-1
            time.sleep(2)
        """
        if(skipNum==i):
            skipNum=0
            i=1
            pyautogui.scroll(-config['row'])
            time.sleep(1)
        """
        if (skipNum < i):
            j=0
            while(j<i):
                pyautogui.scroll(-config['row'])
                j+=1
            time.sleep(1)

        while(pyautogui.locateOnScreen(config['seletPng'], grayscale=True, region=(int(956), int(474), int(400), int(70)))== None):
            pyautogui.scroll(-config['row'])
            if (skipNum > i):
                skipNum = skipNum - 1
            i = i + 1
            time.sleep(1)

        # 发送
        if (pyautogui.locateOnScreen(config['adminPng'], grayscale=True, confidence=0.98, region=(int(956), int(474), int(400), int(70)))!= None or pyautogui.locateOnScreen('adminEn.png', grayscale=True, confidence=0.98,region=(int(956), int(474), int(400), int(70))) != None or pyautogui.locateOnScreen('+86.png', grayscale=True, region=(int(956), int(474), int(400), int(70)))!= None):
            pyautogui.click(pyautogui.locateCenterOnScreen('close.png', grayscale=True))
            i = i + 1
        else:
            # print("i"+str(i)+"total"+str(total))
            pyautogui.click()
            i = i + 1
            time.sleep(2)
        if(config['needSentMessage']==1):
            if (pyautogui.locateOnScreen(config['plusPng'], grayscale=True,
                                         region=(int(m*0.34), int(n*0.39), int(160), int(56))) != None) and (
                    pyautogui.locateOnScreen(config['msgPng'], grayscale=True) == None):
                if (config['needSentPicture'] == 1):
                    try:
                        pointX, pointY = pyautogui.locateCenterOnScreen('fujian.png', grayscale=True, confidence=0.98)
                    except:
                        error("尝试点击附件失败")
                    pyautogui.click(pointX, pointY)
                    # pyautogui.click(x=config['pointDx'], y=config['pointDy'], button='left')
                    time.sleep(1)
                    try:
                        pointX, pointY = pyautogui.locateCenterOnScreen('tupian.png', grayscale=True, confidence=0.98)
                    except:
                        error("尝试点击图片失败")
                    pyautogui.click(pointX, pointY)
                    # pyautogui.click(x=config['pointEx'], y=config['pointEy'], button='left')
                    time.sleep(1)
                    UpLoad_File()
                    while (pyautogui.locateOnScreen(config['sentPng'], grayscale=True,
                                                    region=(1257, 565, 70, 70)) == None):
                        continue
                pyperclip.copy(config['msg'])
                time.sleep(2)
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(0.5)
                pyautogui.press('enter')
                time.sleep(2)
                print('已发送')
            else:
                print('已发送，跳过...')
