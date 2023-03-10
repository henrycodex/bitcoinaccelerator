from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        tx_id = request.form["tx_id"]
        result = accelerate_transaction(tx_id)
        if result:
            message = "Transaction acceleration successful"
        else:
            message = "Transaction acceleration failed"
        return render_template("index.html", message=message)
    return render_template("index.html")

def accelerate_transaction(tx_id):
    acceleration_services = ['https://bitcoinfees.earn.com/api/v1/accelerate/', 
                             'https://pushtx.btc.com/',
                             'https://pool.viabtc.com/tools/txaccelerator/',
                             'https://btc.com/tools/txaccelerator',
                             'https://pusher.bitspill.net/',
                             'https://bitcoin.com/transaction-accelerator',
                             'https://confirmtx.com/',
                             'https://accelerate.blockchair.com/',
                             'https://push.btc.com/',
                             'https://btc.tokenview.com/tools/transactionaccelerator/',
                             'https://viabtc.com/tools/txaccelerator/',
                             'https://txaccelerator.best/',
                             'https://pushtx.bch.sx/',
                             'https://pushtx.bcash.technology/',
                             'https://accelerator.altcointech.net/',
                             'https://txaccelerator.bitpie.com/',
                             'https://bch.btc.com/tools/txaccelerator',
                             'https://bch.tokenview.com/tools/transactionaccelerator/',
                             'https://bch-push.altcointech.net/',
                             'https://bch.bitspill.net/',
                             'https://bch.earn.com/transaction-accelerator/']

    for service_url in acceleration_services:
        try:
            response = requests.post(service_url + tx_id)
            if response.status_code == 200:
                return True
        except requests.exceptions.RequestException as e:
            continue
    return False

if __name__ == "__main__":
    app.run(debug=True)
