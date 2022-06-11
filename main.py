import json
import time

from PhantomBot import PhantomBot
from Scraper import Scraper

CONFIG = json.load(open('config.json'))

BOT = PhantomBot(CONFIG)
SCRAPER = Scraper(CONFIG)

COOLDOWN = 60 * CONFIG['cooldown']

if __name__ == "__main__":
    driver = BOT.setupDriver()

    driver.get("https://www.magiceden.io/")

    BOT.initWallet(driver)
    BOT.selectWallet(driver)

    collections = SCRAPER.getCollections()
    while True:
        listings = list()
        for collection in collections:
            if CONFIG['collectionName'] == collection['name']:
                listings = SCRAPER.getListing(collection['symbol'])
                print(f"Found: {collection['symbol']}")
        eligibleListings, listingPrices = SCRAPER.getEligibleListings(listings)

        if len(listingPrices) > 0:
            lowestPrice = min(listingPrices)
            bestOffer = str()
            for listing in eligibleListings:
                if lowestPrice == listing['price']:
                    bestOffer = f'https://www.magiceden.io/item-details/{listing["tokenMint"]}'

            if len(bestOffer) > 0:
                print(f'Found the best offer - {bestOffer}')
                try:
                    pass
                    BOT.makePurchase(driver, bestOffer)
                except Exception as err:
                    print(f'Unable to purchase: {err}')
                finally:
                    break
            else:
                print("Couldn't find a suitable offer")
        else:
            print("Couldn't find a suitable offer")

        print(f"Next try in {COOLDOWN / 60} minutes")
        time.sleep(COOLDOWN)

    if CONFIG['closeBrowser']:
        print("Stop working...")
        driver.quit()
