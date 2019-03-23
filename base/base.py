class base():
    def __init__(self, driver):
        self.driver = driver

    # 定位元素
    def base_find_element(self, loc):
        return self.driver.find_element(*loc)

    # 定位一组
    def base_find_elements(self, loc):
        return self.driver.find_elements(*loc)

    # 点击定位一个
    def base_click(self, ele):
        self.base_find_element(ele).click()

    # 点击定位一组
    def base_clicks(self, ele, num):
        self.base_find_elements(ele)[num].click()

    # 输入
    def base_input(self, ele, values):
        el = self.base_find_element(ele)
        el.clear()
        el.send_keys(values)

    # 从左往右滑动
    def base_left_to_right(self):
        self.driver.swipe(83,1248,1200,1248)