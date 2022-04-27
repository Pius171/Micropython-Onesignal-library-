from Onesignal import  SMS_Messenger
messenger =SMS_Messenger ("app id",
                          "api key",
                          ["Twilo phone number"],
                          "Pius",
                          "en"
                          )

messenger.send_text("Hello",["recepient phone number"]) #make sure phone number is added to your onesignal subcribers##
