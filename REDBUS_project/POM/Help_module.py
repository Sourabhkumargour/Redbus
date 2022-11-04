import re
import time

from Library.excle_lib import ReadExcel
from Library.config import Configuration



class RedbusHelpPage:

        obj_1 = ReadExcel()
        locator_reg = obj_1.read_locator(Configuration.HELP_LOCATOR_SHEET)

        def __init__(self, driver):
            self.driver = driver

        def click_icon_close(self):
            locator = self.locator_reg["icon_close"]
            self.driver.find_element(*locator).click()

        def click_i_frame(self):
            locator = self.locator_reg["iframe"]
            iframe = self.driver.find_element(*locator)
            self.driver.switch_to.frame(iframe)
            # self.driver.find_element(*locator).click()

        def click_english_btn(self):
            locator = self.locator_reg["english_btn"]
            self.driver.find_element(*locator).click()
            time.sleep(2)

        def click_eng_checkbox(self):
            locator = self.locator_reg["Eng_checkbox"]
            self.driver.find_element(*locator).click()

        def click_set_lang_btn(self):
            locator = self.locator_reg["set_lang_btn"]
            self.driver.find_element(*locator).click()
            time.sleep(2)

        def click_faqs_bustickets(self):
            locator = self.locator_reg["FAQs_Bustickets"]
            self.driver.find_element(*locator).click()
            time.sleep(2)

        def click_bustickets_que(self):
            locator = self.locator_reg["Bustickets_Que"]
            self.driver.find_element(*locator).click()
            time.sleep(3)

        def click_bustickets_helpful_yes(self):
            locator = self.locator_reg["bustickets_helpful_yes"]
            self.driver.find_element(*locator).click()
            time.sleep(5)

        def click_bustickets_window_back(self):
            locator = self.locator_reg["bustickets_window_back"]
            self.driver.find_element(*locator).click()
            time.sleep(3)


        def click_faqs_bustickets_que2(self):
            locator = self.locator_reg["faqs_bustickets_que2"]
            self.driver.find_element(*locator).click()
            time.sleep(3)

        def click_bustickets_helpful_yes(self):
            locator = self.locator_reg["bustickets_helpful_yes"]
            self.driver.find_element(*locator).click()
            time.sleep(3)

        def click_bustickets_window_back(self):
            locator = self.locator_reg["bustickets_window_back"]
            self.driver.find_element(*locator).click()
            time.sleep(3)

        def click_bustickets_window_back(self):
            locator = self.locator_reg["bustickets_window_back"]
            self.driver.find_element(*locator).click()
            time.sleep(3)

        def click_faqs_traintickets(self):
            locator = self.locator_reg["faqs_traintickets"]
            self.driver.find_element(*locator).click()
            time.sleep(3)

        def click_faqs_traintickets_Question1(self):
            locator = self.locator_reg["faqs_traintickets_Question1"]
            self.driver.find_element(*locator).click()
            time.sleep(3)

        def click_trainickets_helpful_yes(self):
            locator = self.locator_reg["trainickets_helpful_yes"]
            self.driver.find_element(*locator).click()
            time.sleep(3)
        #
        def click_trainickets_window_back(self):
            locator = self.locator_reg["trainickets_window_back"]
            self.driver.find_element(*locator).click()
            time.sleep(3)

        def click_faqs_traintickets_question2(self):
            locator = self.locator_reg["faqs_traintickets_question2"]
            self.driver.find_element(*locator).click()
            time.sleep(3)

        def click_trainickets_helpful_yes(self):
            locator = self.locator_reg["trainickets_helpful_yes"]
            self.driver.find_element(*locator).click()
            time.sleep(3)

        def click_trainickets_window_back(self):
            locator = self.locator_reg["trainickets_window_back"]
            self.driver.find_element(*locator).click()
            time.sleep(3)

        def click_trainickets_window_back(self):
            locator = self.locator_reg["trainickets_window_back"]
            self.driver.find_element(*locator).click()
            time.sleep(3)

        def click_faqs_cabs_bushire(self):
            locator = self.locator_reg["faqs_cabs_bushire"]
            self.driver.find_element(*locator).click()
            time.sleep(3)

        def click_general_faqs(self):
            locator = self.locator_reg["general_faqs"]
            self.driver.find_element(*locator).click()
            time.sleep(3)

        def click_general_faqs_question(self):
            locator = self.locator_reg["general_faqs_question"]
            self.driver.find_element(*locator).click()
            time.sleep(3)

        def click_general_faqs_yes(self):
            locator = self.locator_reg["general_faqs_yes"]
            self.driver.find_element(*locator).click()
            time.sleep(3)

        def click_general_window_back(self):
            locator = self.locator_reg["general_window_back"]
            self.driver.find_element(*locator).click()
            time.sleep(3)

        def click_general_window_back(self):
            locator = self.locator_reg["general_window_back"]
            self.driver.find_element(*locator).click()
            time.sleep(3)

        def click_driver_related_faqs(self):
            locator = self.locator_reg["driver_related_faqs"]
            self.driver.find_element(*locator).click()
            time.sleep(3)

        def click_driver_related_faqs_question(self):
            locator = self.locator_reg["driver_related_faqs_question"]
            self.driver.find_element(*locator).click()
            time.sleep(3)

        def click_driver_related_faqs_yes(self):
            locator = self.locator_reg["driver_related_faqs_yes"]
            self.driver.find_element(*locator).click()
            time.sleep(3)

        def click_driver_related_faqs_window_back(self):
            locator = self.locator_reg["driver_related_faqs_window_back"]
            self.driver.find_element(*locator).click()
            time.sleep(3)

        def click_driver_related_faqs_window_back(self):
            locator = self.locator_reg["driver_related_faqs_window_back"]
            self.driver.find_element(*locator).click()
            time.sleep(3)

        def click_vehicle_related_faqs(self):
            locator = self.locator_reg["vehicle_related_faqs"]
            self.driver.find_element(*locator).click()
            time.sleep(3)

        def click_vehicle_related_faqs_question(self):
            locator = self.locator_reg["vehicle_related_faqs_question"]
            self.driver.find_element(*locator).click()
            time.sleep(3)

        def click_vehicle_related_faqs_yes(self):
            locator = self.locator_reg["vehicle_related_faqs_yes"]
            self.driver.find_element(*locator).click()
            time.sleep(3)

        def click_vehicle_related_faqs_window_back(self):
            locator = self.locator_reg["vehicle_related_faqs_window_back"]
            self.driver.find_element(*locator).click()
            time.sleep(3)

        def click_vehicle_related_faqs_window_back(self):
            locator = self.locator_reg["vehicle_related_faqs_window_back"]
            self.driver.find_element(*locator).click()
            time.sleep(3)