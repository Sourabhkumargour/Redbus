# import datetime
# from Library.config import Configuration
# from POM.Help_module import RedbusHelpPage
#
# def test_help_btn(self, init_driver):
#         global driver
#         try:
#             driver = init_driver
#             hp = RedbusHelpPage(driver)
#             hp.click_icon_close()
#             hp.click_i_frame()
#             hp.click_english_btn()
#             hp.click_eng_checkbox()
#             hp.click_set_lang_btn()
#             hp.click_faqs_bustickets()
#             hp.click_bustickets_que()
#             hp.click_bustickets_helpful_yes()
#             hp.click_bustickets_window_back()
#             hp.click_faqs_bustickets_que2()
#             hp.click_bustickets_helpful_yes()
#             hp.click_bustickets_window_back()
#             hp.click_bustickets_window_back()
#             hp.click_faqs_traintickets()
#             hp.click_faqs_traintickets_Question1()
#             hp.click_trainickets_helpful_yes()
#             hp.click_trainickets_window_back()
#             hp.click_faqs_traintickets_question2()
#             hp.click_trainickets_helpful_yes()
#             hp.click_trainickets_window_back()
#             hp.click_trainickets_window_back()
#             hp.click_faqs_cabs_bushire()
#             hp.click_general_faqs()
#             hp.click_general_faqs_question()
#             hp.click_general_faqs_yes()
#             hp.click_general_window_back()
#             hp.click_general_window_back()
#             hp.click_driver_related_faqs()
#             hp.click_driver_related_faqs_question()
#             hp.click_driver_related_faqs_yes()
#             hp.click_driver_related_faqs_window_back()
#             hp.click_driver_related_faqs_window_back()
#             hp.click_vehicle_related_faqs()
#             hp.click_vehicle_related_faqs_question()
#             hp.click_vehicle_related_faqs_yes()
#             hp.click_vehicle_related_faqs_window_back()
#             hp.click_vehicle_related_faqs_window_back()
#
#         except BaseException as err_msg:
#             td = datetime.datetime.now()
#             name = f"screenshot1_{td.hour}_{td.minute}_{td.second}.png"
#             driver.save_screenshot(Configuration.SCREENSHOTS_PATH+name)
#             raise err_msg