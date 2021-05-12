from ronglian_sms_sdk import SmsSDK

accId    = '8a216da87955ba1901795adf854c02b1'
appId    = '8a216da87955ba1901795adf86b902b8'
accToken = '682e0896a3804e6c913f35fe07208b93'


def send_message():
    sdk = SmsSDK(accId, accToken, appId)
    tid = '1'
    mobile = '15555368285'
    datas = ('123456', '5')
    resp = sdk.sendMessage(tid, mobile, datas)
    print(resp)

send_message()
