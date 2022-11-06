import time

from behave import *
from selenium import webdriver


@given('launch chrome browser')
def launch_website(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.redbus.in/info/redcare")
    context.driver.maximize_window()


@When('close the close icon')
def close_icon(context):
    context.driver.find_element("xpath", '//div[@class="modalCloseSmall"]//i').click()


@Then('enter into the frame')
def switch_iframe(context):
    iframe = context.driver.find_element("xpath",
                                         '''//div//iframe[contains(@src, '//www.redbus.in/help?hideLayout=true')]''')
    context.driver.switch_to.frame(iframe)


@when(u'click on english_btn')
def english_btn(context):
    context.driver.find_element("xpath", '//span[@class="languagePreference"]').click()
    time.sleep(2)


@when(u'select english_checkbox')
def english_checkbox(context):
    context.driver.find_element("xpath", '(//span[text()="English"])[2]/..//input[@id="checkmark"]').click()
    time.sleep(2)


@then(u'click on set_language')
def set_language(context):
    context.driver.find_element("xpath", '//button[text()="SET LANGUAGE"]').click()
    time.sleep(2)


@when(u'click on faqs_bustickets')
def faqs_bustickets(context):
    context.driver.find_element("xpath", '(//img[@class="image"])[1]').click()
    time.sleep(2)


@when(u'click on bustickets_que1')
def bustickets_que1(context):
    context.driver.find_element("xpath", '//p[text()="How to book a bus ticket on redBus?"]').click()
    time.sleep(2)


@when(u'click on bustickets_helpful_yes1')
def bustickets_helpful_yes(context):
    context.driver.find_element("xpath", '//button[@class="followupPrimaryButton"]').click()
    time.sleep(2)


@when(u'click on bustickets_window_back1')
def bustickets_window_back(context):
    context.driver.find_element("xpath", '//div[@class="ripple"]').click()
    time.sleep(2)


@when(u'click on faqs_bustickets_que2')
def faqs_bustickets_que2(context):
    context.driver.find_element("xpath", '//p[text()="How to cancel a ticket?"]').click()
    time.sleep(2)


@when(u'click on bustickets_helpful_yes2')
def bustickets_helpful_yes(context):
    context.driver.find_element("xpath", '//button[@class="followupPrimaryButton"]').click()
    time.sleep(2)


@when(u'click on bustickets_window_back2')
def bustickets_window_back1(context):
    context.driver.find_element("xpath", '//div[@class="ripple"]').click()
    time.sleep(2)


@then(u'click on bustickets_window_back3')
def bustickets_window_back2(context):
    context.driver.find_element("xpath", '//div[@class="ripple"]').click()
    time.sleep(2)


@when(u'click on faqs_traintickets')
def faqs_traintickets(context):
    context.driver.find_element("xpath", '(//img[@class="image"])[2]').click()
    time.sleep(2)


@when(u'click on faqs_traintickets_question1')
def faqs_traintickets_question1(context):
    context.driver.find_element("xpath", '//p[text()="How to book a train ticket on redBus App?"]').click()
    time.sleep(2)


@when(u'click on trainickets_helpful_yes1')
def trainickets_helpful_yes1(context):
    context.driver.find_element("xpath", '//button[@class="followupPrimaryButton"]').click()
    time.sleep(2)


@when(u'click on trainickets_window_back1')
def trainickets_window_back1(context):
    context.driver.find_element("xpath", '//div[@class="ripple"]').click()
    time.sleep(2)


@when(u'click on faqs_traintickets_question2')
def faqs_traintickets_question2(context):
    context.driver.find_element("xpath", '//p[text()="How to cancel a train ticket on redBus App?"]').click()
    time.sleep(2)


@when(u'click on trainickets_helpful_yes2')
def trainickets_helpful_yes2(context):
    context.driver.find_element("xpath", '//button[@class="followupPrimaryButton"]').click()
    time.sleep(2)


@when(u'click on trainickets_window_back2')
def trainickets_window_back2(context):
    context.driver.find_element("xpath", '//div[@class="ripple"]').click()
    time.sleep(2)


@then(u'click on trainickets_window_back3')
def trainickets_window_back3(context):
    context.driver.find_element("xpath", '//div[@class="ripple"]').click()
    time.sleep(2)


@when(u'click on faqs_cabs_bushire')
def cabs_bushire(context):
    context.driver.find_element("xpath", '(//img[@class="image"])[3]').click()
    time.sleep(2)


@when(u'click on general_faqs')
def general_faqs(context):
    context.driver.find_element("xpath", '//span[text()="General FAQs"]').click()
    time.sleep(2)


@when(u'click on general_faqs_question1')
def general_faqs_question1(context):
    context.driver.find_element("xpath", '//p[text()="What are the different vehicle hire services offered?"]').click()
    time.sleep(2)


@when(u'click on general_faqs_yes1')
def general_faqs_yes1(context):
    context.driver.find_element("xpath", '//button[@class="followupPrimaryButton"]').click()
    time.sleep(2)


@when(u'click on general_window_back1')
def general_window_back1(context):
    context.driver.find_element("xpath", '//div[@class="ripple"]').click()
    time.sleep(2)


@when(u'click on general_faqs_question2')
def general_faqs_question2(context):
    context.driver.find_element("xpath", '//p[text()="What are Ryde Assured vehicles?"]').click()
    time.sleep(2)


@when(u'click on general_faqs_yes2')
def general_faqs_yes2(context):
    context.driver.find_element("xpath", '//button[@class="followupPrimaryButton"]').click()
    time.sleep(2)


@when(u'click on general_window_back2')
def general_window_back1(context):
    context.driver.find_element("xpath", '//div[@class="ripple"]').click()
    time.sleep(2)


@when(u'click on general_window_back3')
def general_window_back2(context):
    context.driver.find_element("xpath", '//div[@class="ripple"]').click()
    time.sleep(2)


@when(u'click on driver_related_faqs')
def driver_related_faqs(context):
    context.driver.find_element("xpath", '//span[text()="Driver Related FAQs"]').click()
    time.sleep(2)


@when(u'click on driver_related_faqs_question1')
def driver_related_faqs_question1(context):
    context.driver.find_element("xpath",
                                '//p[text()="When & how will I receive the vehicle and driver details?"]').click()
    time.sleep(2)


@when(u'click on driver_related_faqs_yes1')
def driver_related_faqs_yes(context):
    context.driver.find_element("xpath", '//button[@class="followupPrimaryButton"]').click()
    time.sleep(2)


@when(u'click on driver_related_faqs_window_back1')
def driver_related_faqs_window_back1(context):
    context.driver.find_element("xpath", '//div[@class="ripple"]').click()
    time.sleep(2)


@when(u'click on driver_related_faqs_question2')
def driver_related_faqs_question2(context):
    context.driver.find_element("xpath",
                                '//p[text()="How experienced is the driver?  Is he familiar with the route?"]').click()
    time.sleep(2)


@when(u'click on driver_related_faqs_yes2')
def driver_related_faqs_yes2(context):
    context.driver.find_element("xpath", '//button[@class="followupPrimaryButton"]').click()
    time.sleep(2)


@when(u'click on driver_related_faqs_window_back2')
def driver_related_faqs_window_back1(context):
    context.driver.find_element("xpath", '//div[@class="ripple"]').click()
    time.sleep(2)


@when(u'click on driver_related_faqs_window_back3')
def driver_related_faqs_window_back2(context):
    context.driver.find_element("xpath", '//div[@class="ripple"]').click()
    time.sleep(2)


@when(u'click on vehicle_related_faqs')
def vehicle_related_faqs(context):
    context.driver.find_element("xpath", '//span[text()="Vehicle Related FAQs"]').click()
    time.sleep(2)


@when(u'click on vehicle_related_faqs_question1')
def vehicle_related_faqs_question1(context):
    context.driver.find_element("xpath",
                                '//p[text()="When & how will I receive the vehicle and driver details?"]').click()
    time.sleep(2)


@when(u'click on vehicle_related_faqs_yes1')
def vehicle_related_faqs_yes1(context):
    context.driver.find_element("xpath", '//button[@class="followupPrimaryButton"]').click()
    time.sleep(2)


@when(u'click on vehicle_related_faqs_window_back1')
def vehicle_related_faqs_window_back1(context):
    context.driver.find_element("xpath", '//div[@class="ripple"]').click()
    time.sleep(2)


@when(u'click on vehicle_related_faqs_question2')
def vehicle_related_faqs_question2(context):
    context.driver.find_element("xpath", '//p[text()="How many people can travel in a vehicle?"]').click()
    time.sleep(2)


@when(u'click on vehicle_related_faqs_yes2')
def vehicle_related_faqs_yes2(context):
    context.driver.find_element("xpath", '//button[@class="followupPrimaryButton"]').click()
    time.sleep(2)


@when(u'click on vehicle_related_faqs_window_back2')
def vehicle_related_faqs_window_back2(context):
    context.driver.find_element("xpath", '//div[@class="ripple"]').click()
    time.sleep(2)


@when(u'click on vehicle_related_faqs_window_back3')
def vehicle_related_faqs_window_back3(context):
    context.driver.find_element("xpath", '//div[@class="ripple"]').click()
    time.sleep(2)


@then(u'click on vehicle_related_faqs_window_back4')
def vehicle_related_faqs_window_back4(context):
    context.driver.find_element("xpath", '//div[@class="ripple"]').click()
    time.sleep(2)
