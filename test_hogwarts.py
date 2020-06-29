import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os


class TestHogwarts:
    def setup(self):
        print("abc")
        self.driver = webdriver.Chrome()  # 实例化driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        pass
        print("aaa")

    def teatdown(self):
        self.driver.quit()
        pass
        print("quit")

    # def teardown(self):
    #     self.driver.quit() #回收掉driver
    #     pass
    def test_hogwarts(self):  # 开始编写测试用例
        """

        :return:
        """
        self.driver.get('https://www.autohome.com.cn/beijing/')
        print("bbb")

        def wait(x):
            """
            显示等待
            :param x:
            :return:
            """
            return len(self.driver.find_elements(By.XPATH, '//*[@class="monkey__iconmini"]')) >= 1

        WebDriverWait(self.driver, 10).until(wait)
        print("ccc")
        self.driver.find_element(By.XPATH, '//*[@class="athm-btn athm-btn--blue"]').click()

if __name__ == "__main__":
    pytest.main(['-v', '-s', 'test_hogwarts.py'])
