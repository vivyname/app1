from page.Page import BaiduPage
import time


class testbaidu:
    def test_baidu_search(self,driver):
        
        page = BaiduPage(driver)
        page.search("我喜欢软件测试")
        time.sleep(5)
        driver.implicitly_wait(10)


        assert "我喜欢软件测试" in driver.title

    def test_click_title(self,driver):
        
        page = BaiduPage(driver)
        page.click_title()
        time.sleep(5)
        driver.implicitly_wait(10)
        # pysonar --sonar-host-url=http://localhost:9000 --sonar-token=sqp_9564ac88ec4d631c4c9bedd4e5fcf2a8940e9e70 --sonar-project-key=a3mall
        #

        # assert "我喜欢软件测试" in driver.title

# pysonar --sonar-host-url=http://localhost:9000 --sonar-token=sqp_9564ac88ec4d631c4c9bedd4e5fcf2a8940e9e70 --sonar-project-key=a3mall
# pysonar \
#   --sonar-host-url=http://localhost:9000 \
#   --sonar-token=sqp_9564ac88ec4d631c4c9bedd4e5fcf2a8940e9e70 \
#   --sonar-project-key=a3mall