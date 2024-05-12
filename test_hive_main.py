from flask import Flask, request
from beem import Hive
from beem.nodelist import NodeList

app = Flask(__name__)


client_id = "your.app"
client_secret = "your_secret"
from beem import Hive
from beem.nodelist import NodeList
from beem.blockchain import Blockchain
from beem.block import Block
from beem.account import Account
from beem.instance import set_shared_blockchain_instance
from beem.vote import Vote 
from beem.vote import AccountVotes
from beem.comment import Comment 
from beem.market import Market 
from beem.witness import Witness
from beem.account import Account



nodelist = NodeList()
nodelist.update_nodes()
nodes = nodelist.get_hive_nodes()
hive = Hive(node=nodes)
print(hive.is_hive)


hive = Hive()
# account = Account("test", blockchain_instance=hive)
# print(account)

# from beem.instance import set_shared_blockchain_instance
# hive = Hive()
# set_shared_blockchain_instance(hive)
# account = Account("test1")
# print(account)

# hive.wallet.wipe(True)
# hive.wallet.unlock("wallet-passphrase")
# hive.wallet.addPrivateKey("5nKgT99u2xjLsVRXaiwX3i4ccHDryrfVpo2pMoown")
# hive.wallet.addPrivateKey("5XrzppWL25yE9cMG8TgtmPcyQzxeWVcqq9WxVfxzK")
# hive.wallet.addPrivateKey("5JynQR7KaFnDGmNzi31rfiB6osruR1vWns9wAdth")
# hive.wallet.addPrivateKey("5KEQtm3CDAbYA1ZCWVU2FKLGUvANVVxCH52KC")
# hive.wallet.addPrivateKey("Prg2W3ZTwn4iZ2JkMLfY2fepWAgLzX38aYnDPCxvf")
# keys are modified for security reasons 
account = Account("theringmaster", blockchain_instance=hive)
# account.transfer("<to>", "<asset>", "<memo>")
# account.transfer("null", 1, "SBD", "suraj210321")
# print(account)
blockchain = Blockchain()

# for op in blockchain.stream():
#     print(op)

# print(Block[1])

print(account.balances)
for i in account.history():
    print(i)
# vote = Vote(u"@steevc/follow-friday-lets-split")
# print(vote.json())


# allVotes = AccountVotes('@suraj210321')
# print(allVotes)

# comment = Comment("@gtg/ffdhu-gtg-witness-log")
# print(comment["active_votes"])

# market = Market("HBD:HIVE")
# print(market)

# witness = Witness("gtg")
# print(witness.is_active)



# uncomment the lines to enable the other required functionalities. 

nodelist = NodeList()
nodelist.update_nodes()
nodes = nodelist.get_hive_nodes()
hive = Hive(node=nodes)
print(hive.is_hive)

c = Client(client_id=client_id, client_secret=client_secret)


@app.route('/')
def index():
    login_url = c.get_login_url(
        "http://localhost:5000/welcome",
        "login",
    )
    return "<a href='%s'>Login with SteemConnect</a>" % login_url


@app.route('/welcome')
def welcome():
    c.access_token = request.args.get("access_token")
    return "Welcome <strong>%s</strong>!" % c.me()["name"]

if __name__ == '__main__':
    app.run(debug=True, port=5005)