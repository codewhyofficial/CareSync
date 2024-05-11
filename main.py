from flask import Flask, render_template,request

from flask_mysqldb import MySQL
import json
from random import choice as r_c
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


app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Ekansh@04'
app.config['MYSQL_DB'] = 'users_db'

# app.config['MYSQL_DB'] = 'doctors_db'

mysql = MySQL(app)
hive = Hive()
hive.wallet.wipe(True)
hive.wallet.unlock("wallet-passphrase")
account = Account("suraj210321", blockchain_instance=hive)

for account_history in account.history():
    formatted_json = json.dumps(account_history, indent=1)
    print(formatted_json)


balance = account.balances

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        username = request.form['username']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        phone=request.form['phone']
        email=request.form['email']
        # dob1=request.form['dob1']

        
         

        
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users_db(username, firstname, lastname, phone, email) VALUES (%s, %s, %s, %s, %s)",
                        (username, firstname, lastname, phone, email))
        mysql.connection.commit()
        cur.close()

        return "success" 

    return render_template('index.html')
@app.route('/doctor_reg', methods=['GET', 'POST'])
def doctor_reg():

    return render_template('doctor_reg.html')
@app.route('/chat_caresync', methods=['GET', 'POST'])
def chat_caresync():

    return render_template('chat_caresync.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile():

    balance = account.balances

    balance_dict = {
        'available': str(balance['available']),
        'savings': str(balance['savings']),
        'rewards': str(balance['rewards']),
        'total': str(balance['total'])
    }


    return render_template('profile.html',balance=balance_dict)

if __name__ == "__main__":
    app.run(debug=True)