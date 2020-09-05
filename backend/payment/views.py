import requests
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.conf import settings
from .models import paymentdata
from django.template import loader, Context

# from .paytm import generate_checksum, verify_checksum
from. import PaytmChecksum


def initiate_payment(request):
    if request.method == "POST":

        data = json.loads(request.body)
        orderid = data['orderid']
        paytmParams = dict()

        paytmParams["body"] = {
            "requestType": "Payment",
            "mid": "odqOQb08807102424906",
            "websiteName": "WEBSTAGING",
            "orderId": data['orderid'],
            "callbackUrl": "https://merchant.com/callback",
            "txnAmount": {
                "value": data['amount'],
                "currency": "INR",
            },
            "userInfo": {
                "custId": data['custid'],
            },
        }

        # Generate checksum by parameters we have in body
        # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
        checksum = PaytmChecksum.generateSignature(
            json.dumps(paytmParams["body"]), "b58ZJ%yf3kdWs!xE")

        paytmParams["head"] = {
            "signature"	: checksum
        }

        post_data = json.dumps(paytmParams)

        # for Staging
        url = "https://securegw-stage.paytm.in/theia/api/v1/initiateTransaction?mid=odqOQb08807102424906&orderId="+orderid

        response1 = requests.post(url, data=post_data, headers={
            "Content-type": "application/json"}).json()
        print(response1)
        body = response1['body']
        token = body['txnToken']
        paymentdata.objects.create(order=orderid, token=token)
    return JsonResponse(orderid, safe=False)

    # return JsonResponse(response, safe=False)


def paydata(request):
    if request.mehtod == "POST":
        data = json.loads(request.body)
        orderid = data['orderid']
        token = list(paydata.objects.filter(order=orderid).values('token'))
    return JsonResponse(token['token'], safe=False)


def callback(request):
    if request.method == 'POST':
        received_data = dict(request.POST)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]
        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                paytm_checksum = value[0]
            else:
                paytm_params[key] = str(value[0])
        # Verify checksum
        is_valid_checksum = verify_checksum(
            paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
        if is_valid_checksum:
            received_data['message'] = "Checksum Matched"
        else:
            received_data['message'] = "Checksum Mismatched"
            return render(request, 'callback.html', context=received_data)
# #for send otp  api
# paytmParams = dict()

# paytmParams["body"] = {
#     "mobileNumber" : "7777777777"
# }

# paytmParams["head"] = {
#     "txnToken"     : token
# }

# post_data = json.dumps(paytmParams)

# # for Staging
# url = "https://securegw-stage.paytm.in/login/sendOtp?mid=YOUR_MID_HERE&orderId=ORDERID_98765"


# #for validiation of otp
# paytmParams = dict()

# paytmParams["body"] = {
# "otp"      : "888888,"
# }

# paytmParams["head"] = {
# "txnToken" : token
# }

# post_data = json.dumps(paytmParams)

# # for Staging
# url = "https://securegw-stage.paytm.in/login/validateOtp?mid=YOUR_MID_HERE&orderId=ORDERID_98765"

# #for pcf deatials

# import requests
# import json

# paytmParams = dict()

# paytmParams["body"] = {
#     "payMethods"    : [{
#         "payMethod" : "CREDIT_CARD",
#         "instId"    : "VISA",
#     }],
# }

# paytmParams["head"] = {
#     "txnToken"	    : token
# }

# post_data = json.dumps(paytmParams)

# # for Staging
# url = "https://securegw-stage.paytm.in/theia/api/v1/fetchPcfDetails?mid=YOUR_MID_HERE&orderId=ORDERID_98765"


# response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"}).json()
# print(response)

# # transaction status api

# import requests
# import json

# # import checksum generation utility
# # You can get this utility from https://developer.paytm.com/docs/checksum/
# import PaytmChecksum

# # initialize a dictionary
# paytmParams = dict()

# # body parameters
# paytmParams["body"] = {

#     # Find your MID in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
#     "mid" : "YOUR_MID_HERE",

#     # Enter your order id which needs to be check status for
#     "orderId" : "YOUR_ORDER_ID",
# }

# # Generate checksum by parameters we have in body
# # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
# checksum = PaytmChecksum.generateSignature(json.dumps(paytmParams["body"]), "YOUR_MERCHANT_KEY")

# # head parameters
# paytmParams["head"] = {

#     # put generated checksum value here
#     "signature"	: checksum
# }

# # prepare JSON string for request
# post_data = json.dumps(paytmParams)

# # for Staging
# url = "https://securegw-stage.paytm.in/v3/order/status"

# response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"}).json()
