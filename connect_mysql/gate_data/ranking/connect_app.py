from appium import webdriver
# "com.huawei.appmarket/.MarketActivity:"


def connect_app():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '8.0.0',
        'deviceName': 'UEUNW16C29005125',
        'appPackage': 'com.huawei.appmarket',
        'appActivity': "com.huawei.MarketActivity",
        'unicodeKeyboard': True,
        'resetKeyboard': True,
        'noReset': True,
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver


driver = connect_app()