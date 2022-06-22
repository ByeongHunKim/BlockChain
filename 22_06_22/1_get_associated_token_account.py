from solana.publickey import PublicKey
from solana.keypair import Keypair
from solana.rpc.async_api import AsyncClient
from solana.rpc.commitment import Confirmed
from solana.rpc.types import TxOpts
from solana.transaction import Transaction
import solana.system_program as sys

from spl.token.constants import TOKEN_PROGRAM_ID
from spl.token.async_client import AsyncToken
from spl.token._layouts import MINT_LAYOUT
import spl.token.instructions as spl_token
import time
from solana.rpc.api import Client
from base58 import b58encode, b58decode as b58d
import asyncio;

client = Client("https://api.devnet.solana.com")


feePayerWalletAddr = "" # feePayer's public_key
feePayerPriv = "" # feePayer's private_key
feePayerKeypair = b58d(feePayerPriv)
feePayer = Keypair.from_secret_key(feePayerKeypair)
main = PublicKey(feePayerWalletAddr)

newOwner = '' # wallet_address
newOwnerPub = PublicKey(newOwner)
mint1 = '' # mint Address
mintAddr = PublicKey(mint1)



# findnewAcc = client.get_transaction("")
# newTokenAcc = findnewAcc['result']['transaction']['message']['accountKeys'][1]
# print(newTokenAcc)



# result = client.get_token_accounts_by_owner(main, )
# print(result)

test = client.is_connected()
print("1. 솔라나 연결여부:" ,test)
resultOfTxn = ""
print(resultOfTxn)
result = client.get_transaction(resultOfTxn)
print(result)