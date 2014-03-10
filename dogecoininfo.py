# Dogecoin Information Centre, version 0.1.
# I don't know why I made this. Looked cool.
# Such fun. Much API.
import requests

d = requests.get("http://dogechain.info/chain/Dogecoin/q/")

print "Dogecoin Information Centre, version 0.1a"
print "Current statistics according to dogechain.info:\n"

# Requests current block number.
d = requests.get("http://dogechain.info/chain/Dogecoin/q/getblockcount")
d = d.text
print "Current block: " + d

# Requests difficulty.
d = requests.get("http://dogechain.info/chain/Dogecoin/q/getdifficulty")
d = d.text
print "Current difficulty: " + d

# Requests total Dogecoin mined.
d = requests.get("http://dogechain.info/chain/Dogecoin/q/totalbc")
d = d.text
print "Total Dogecoin available: " + d

print "Wow. Much amaze."
