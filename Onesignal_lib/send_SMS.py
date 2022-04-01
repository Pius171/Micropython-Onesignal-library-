from Onesignal import  SMS_Messenger
messenger =SMS_Messenger ("4be64729-ab93-4fac-8e41-fd124b8bc880",
                          "ODgzM2IyODMtNzQ1NC00M2VlLThlNjktODMzY2Y5ZTkyNDE2",
                          ["+13512473112"],
                          "Pius",
                          "en"
                          )

messenger.send_text("Hello",["+2349056149453"]) #make sure phone number is added to your onesignal subcribers##