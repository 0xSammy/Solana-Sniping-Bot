## EN
> This bot will help to buy NFT from the desired collection **at the lowest price**.

**This bot does not guarantee you will buy NFT**, this bot simply goes faster than humans and automates everything since you do not have to click yourself.

### Tutorial
1. Clone the repository / Download zip file:

	`git clone https://github.com/SniperNFTbot/Solana-Sniping-Bot.git`

	OR

	[Download Zip File](https://github.com/SniperNFTbot/Solana-Sniping-Bot.git)

2. Be sure you have installed Python, [here is a link to download](https://www.python.org/downloads/)
3. Open **cmd** (command prompt)
4. Install **all python module**:

   `pip install -r requirements.txt`
5. Fill in all the data in `config.json`:
```json
{
"seedPhrase": "your seed phrase from Phantom Wallet (Do Not Share This KEY)",
"password": "your password",
"collectionName" : "Collection name example: DeGods",
"willingPrice": 399 (preferred buying price),
"cooldown": 15 - minutes (How long will the bot wait for the next attempt),
"closeBrowser": true (Close browser after buying, false - No)
}
```

6. Open **CMD** and go to directory:
 `cd /path/to/directory/`

7. Run the python file:

	windows : `python main.py`

	mac : `python3 main.py`
