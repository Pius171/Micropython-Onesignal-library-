from Onesignal import Notifier, SMS_Messenger

# messenger =SMS_Messenger ("4be64729-ab93-4fac-8e41-fd124b8bc880",
#                           "ODgzM2IyODMtNzQ1NC00M2VlLThlNjktODMzY2Y5ZTkyNDE2",
#                           ["+13512473112"],
#                           "Pius",
#                           "en"
#                           )

notifier= Notifier("dbe9d90b-3455-4947-98f2-f27cc387e826","ZmJhMDBkMjMtNDdjZC00Y2Q3LTllMDItYTA4MTA1ZjZhZThj","en")
notifier.notify_segment("Subscribed Users","hello")

notifier.notify_user("b8396160-e893-453b-b475-46d4641a1122","hi pius")

#messenger.send_text("Hello",["+2349056149453"]) #make sure phone number is added to your onesignal subcribers##