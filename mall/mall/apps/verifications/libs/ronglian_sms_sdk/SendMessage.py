from ronglian_sms_sdk import SmsSDK

accId = '8a216da87955ba1901795adf854c02b1'
accToken = '682e0896a3804e6c913f35fe07208b93'
appId = '8a216da87955ba1901795adf86b902b8'

def send_message():
    sdk = SmsSDK(accId, accToken, appId)
    tid = '容联云通讯创建的模板'
    mobile = '手机号1,手机号2'
    datas = ('变量1', '变量2')
    resp = sdk.sendMessage(tid, mobile, datas)
    print(resp)

send_message()
