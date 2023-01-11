import pyautogui

# マウスポインタの位置を取得する
print(pyautogui.position())

# マウスを座標に移動する
pyautogui.moveTo(300, 300)

# 持続時間付きマウスを座標に移動する
pyautogui.moveTo(300, 300, 2)

# クリック
pyautogui.leftClick()
pyautogui.rightClick()
pyautogui.doubleClick()
pyautogui.tripleClick()

# キーボード入力
pyautogui.write("contents to write")
pyautogui.typewrite("contents to write")
pyautogui.press("enter")

# スクショすると画像を保存する
pyautogui.screenshot("image.png")
pyautogui.screenshot("partial-image.png", region=(0, 0, 300, 300))

# 画像の中心位置が探そう
x, y = pyautogui.locateCenterOnScreen("image.png")  # *全てのピクセルが一致する必要があります
x, y = pyautogui.locateCenterOnScreen("image.png", confidence=0.6)  # opencvのパッケージが必要です
