'''
Seit doma likt visadas fukncijas kas neder citur
'''
import sendgrid

def is_credit(T, account):
    if T.account_from == account:
        T.credit=False
    else:
         T.credit=True
    return T

# naudu no centiem uz eiro parveido
def decimalize(ones):
    hundreds = float(ones) / 100
    return hundreds

#Epasta pazinojuma nosutisanai
def send_email_notification(target_email, amount, bilance):
    print("Target Email is: " + str(target_email) + " Amount is: " + str(amount), " and Bilance is: " + str(bilance))
    clientID = sendgrid.SendGridClient("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",
                                   None, raise_errors=True)
    message = sendgrid.Mail()#Define mail object
    message.add_to(str(target_email))
    message.set_from("raivis.rugelis@va.lv")#Sis gan bus janomaina! :D
    message.set_subject("Konta bilances maina")
    message.set_html("""<!DOCTYPE HTML>

    <html>

    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <title>Your Website</title>
    </head>

    <style>
        #cirvbank_logo_header{
            width:204px;
            height:128px;
            padding-left: 25px;
            padding-top: 5px;
        }

        #adress_field_header{
            padding-left: 32px;
            font-family: "Century Gothic", "Arial", "sans-serif";
            font-size: 12pt;
        }

        #container_letter{
            padding-left: 32px;
            padding-top: 25px;
            font-family: "Century Gothic", "Arial", "sans-serif";
        }

        #announcement{
            font-size: 15pt;
        }

        #footer_letter{
            padding-left: 32px;
            padding-top: 15px;
            font-family: "Century Gothic", "Arial", "sans-serif";
            font-size: 10pt;
        }
    </style>

    <body>

        <div id = "header_letter">
            <img src="http://178.62.72.32/random_pictures/cirvbank_letter_logo_2.png" alt="CirvBank logo" id="cirvbank_logo_header">

            <p id = "adress_field_header">
                LIEPU IELA 5-3<br />
                RIGA<br />
                LV-1050<br />
            </p>
        </div><!-- End of header_letter -->
        <div id = "container_letter">
            <p id = "announcement"><strong><i>Pazinojums</i></strong></p>

            <p>Pazinojums par kontas bilances mainu: +""" + str(amount) + "&euro;, konta atlikums: " + str(bilance) +
                    "&euro;" +"""</p>
        </div><!-- End of container_letter -->
        <div id = "footer_letter">
            <p>CirvBank Latvia<br />
            Talrunis: <i>+ 371 67 444 444</i><br />
            E-pasts: cirvbank@inbox.lv<br />
            </p>
        </div>

    </body>

    </html>""")
    #message.set_text("Sveiki! Pazinojums par konta bilances mainu!")

    try:
        clientID.send(message)
    except sendgrid.SendGridClientError:
        print("Kluda klienta puse")
    except sendgrid.SendGridServerError:
        print("Kluda servera puse")