Feature: Help
 Background: Common steps
   Given launch chrome browser
   When  close the close icon
   Then  enter into the frame


   Scenario: User should able to click on english_btn
     When click on english_btn
     When select english_checkbox
     Then click on set_language

   Scenario: User should able to click on FAQs_Bustickets
     When click on faqs_bustickets
     When click on bustickets_que1
     And  click on bustickets_helpful_yes1
     And  click on bustickets_window_back1
     And  click on faqs_bustickets_que2
     And  click on bustickets_helpful_yes2
     And  click on bustickets_window_back2
     Then click on bustickets_window_back3

   Scenario: User should able to click on faqs_traintickets
     When click on faqs_traintickets
     When click on faqs_traintickets_question1
     And  click on trainickets_helpful_yes1
     And  click on trainickets_window_back1
     And  click on faqs_traintickets_question2
     And  click on trainickets_helpful_yes2
     And  click on trainickets_window_back2
     Then click on trainickets_window_back3

   Scenario:User should able to click on faqs_cabs_bushire
     When click on faqs_cabs_bushire
     When click on general_faqs
     And  click on general_faqs_question1
     And  click on general_faqs_yes1
     And  click on general_window_back1
     And  click on general_faqs_question2
     And  click on general_faqs_yes2
     And  click on general_window_back1
     And  click on general_window_back3
     And  click on driver_related_faqs
     And  click on driver_related_faqs_question1
     And  click on driver_related_faqs_yes1
     And  click on driver_related_faqs_window_back1
     And  click on driver_related_faqs_question2
     And  click on driver_related_faqs_yes2
     And  click on driver_related_faqs_window_back2
     And  click on driver_related_faqs_window_back3
     And  click on vehicle_related_faqs
     And  click on vehicle_related_faqs_question1
     And  click on vehicle_related_faqs_yes1
     And  click on vehicle_related_faqs_window_back1
     And  click on vehicle_related_faqs_question2
     And  click on vehicle_related_faqs_yes2
     And  click on vehicle_related_faqs_window_back2
     And  click on vehicle_related_faqs_window_back3
     Then click on vehicle_related_faqs_window_back4




