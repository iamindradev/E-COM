function onScriptLoad(){
    var config = {
      "root": "",
      "flow": "DEFAULT",
      "data": {
      "orderId": "", /* update order id */
      "token": "", /* update token value */
      "tokenType": "TXN_TOKEN",
      "amount": "" /* update amount */
      },
      "handler": {
        "notifyMerchant": function(eventName,data){
          console.log("notifyMerchant handler function called");
          console.log("eventName => ",eventName);
          console.log("data => ",data);
        } 
      }
    };

    if(window.Paytm && window.Paytm.CheckoutJS){
        window.Paytm.CheckoutJS.onLoad(function excecuteAfterCompleteLoad() {
            // initialze configuration using init method 
            window.Paytm.CheckoutJS.init(config).then(function onSuccess() {
                // after successfully updating configuration, invoke Blink Checkout
                window.Paytm.CheckoutJS.invoke();
            }).catch(function onError(error){
                console.log("error => ",error);
            });
        });
    } 
}



Test Merchant ID
odqOQb08807102424906
Test Merchant Key
b58ZJ%yf3kdWs!xE
Website
WEBSTAGING
Industry Type
Retail
Channel ID (For Website)
WEB
Channel ID (For Mobile Apps)
WAP
Transaction URL
https://securegw-stage.paytm.in/order/process
Transaction Status URL
https://securegw-stage.paytm.in/order/status
Production API Details