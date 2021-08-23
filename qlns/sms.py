import os
from twilio.rest import Client

def send_sms():


    account_sid = "AC6832d5698a2315c87f87b94f2aa94fb7"
    auth_token = "d25d9aa95d016469d2697f3ae62847d3"
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Xin Chúc Mừng Bạn Đã Trúng 142 tỷ Đồng Từ Bitcon sway ",
                        from_='+14157636068',
                        to='+84947588971',
                    )

    print(message.sid)
