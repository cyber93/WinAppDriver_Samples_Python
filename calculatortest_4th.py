#******************************************************************************
#
# Copyright (c) 2016 Microsoft Corporation. All rights reserved.
#
# This code is licensed under the MIT License (MIT).
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# // LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
#******************************************************************************


import unittest
from appium import webdriver

class SimpleCalculatorTests(unittest.TestCase):

    @classmethod

    def setUpClass(self):
        #set up appium
        desired_caps = {}
        desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"

        #Appium Desired Capabilities 추가
        # - platformName으로 windows 추가
        desired_caps["platformName"] = "windows"

        #Appium Default URL로 수정합니다.
        #command_executor를 Appium이 실행되고 있는 Test Node PC IP Address로 수정하시기 바랍니다.
        self.driver = webdriver.Remote(
            command_executor='http://192.168.0.2:4723/wd/hub',
            desired_capabilities= desired_caps)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def getresults(self):
        displaytext = self.driver.find_element_by_accessibility_id("CalculatorResults").text
        displaytext = displaytext.strip("표시는 " )
        displaytext = displaytext.rstrip(' ')
        displaytext = displaytext.lstrip(' ')
        return displaytext


    def test_initialize(self):
        self.driver.find_element_by_name("지우기").click()
        self.driver.find_element_by_name("7").click()
        self.assertEqual(self.getresults(),"7")
        self.driver.find_element_by_name("지우기").click()

    def test_addition(self):
        self.driver.find_element_by_name("1").click()
        self.driver.find_element_by_name("양의 값").click()
        self.driver.find_element_by_name("7").click()
        self.driver.find_element_by_name("일치").click()
        self.assertEqual(self.getresults(),"8")

    def test_combination(self):
        self.driver.find_element_by_name("7").click()
        self.driver.find_element_by_name("곱").click()
        self.driver.find_element_by_name("9").click()
        self.driver.find_element_by_name("양의 값").click()
        self.driver.find_element_by_name("1").click()
        self.driver.find_element_by_name("일치").click()
        self.driver.find_element_by_name("나누기").click()
        self.driver.find_element_by_name("8").click()
        self.driver.find_element_by_name("일치").click()
        self.assertEqual(self.getresults(),"8")

    def test_division(self):
        self.driver.find_element_by_name("8").click()
        self.driver.find_element_by_name("8").click()
        self.driver.find_element_by_name("나누기").click()
        self.driver.find_element_by_name("1").click()
        self.driver.find_element_by_name("1").click()
        self.driver.find_element_by_name("일치").click()
        self.assertEqual(self.getresults(),"8")

    def test_multiplication(self):
        self.driver.find_element_by_name("9").click()
        self.driver.find_element_by_name("곱").click()
        self.driver.find_element_by_name("9").click()
        self.driver.find_element_by_name("일치").click()
        self.assertEqual(self.getresults(),"81") 

    def test_subtraction(self):
        self.driver.find_element_by_name("9").click()
        self.driver.find_element_by_name("음의 값").click()
        self.driver.find_element_by_name("1").click()
        self.driver.find_element_by_name("일치").click()
        self.assertEqual(self.getresults(),"8")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleCalculatorTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
