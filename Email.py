import smtplib
try:
    #Create your SMTP session
    smtp = smtplib.SMTP('smtp.gmail.com', 587)

   #Use TLS to add security
    smtp.starttls()

    #User Authentication
    smtp.login("amitkumar841994@gmail.com","bantbnxhxttuhoty")

    #Defining The Message
    message = "Message_you_need_to_send"

    #Sending the Email
    smtp.sendmail("amitpal9445@gmail.com", "apal453@gmail.com",message)

    #Terminating the session
    smtp.quit()
    print ("Email sent successfully!")

except Exception as ex:
    print("Something went wrong....",ex)