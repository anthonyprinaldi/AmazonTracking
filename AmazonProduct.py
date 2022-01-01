import requests
from bs4 import BeautifulSoup
import re

HEADER = {
    "Connection": "keep-alive",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    "Accept": "*/*",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "sec-ch-ua-platform": '"Windows"',
    "Origin": "https://www.amazon.ca",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.amazon.ca/",
    "Accept-Language": "en-US,en;q=0.9",
}


class AmazonProdcut:
    def __init__(self, id: str) -> None:
        self.product_id = id
        self.request_params = (("asinList", [self.product_id]),)
        self.url = "https://api-amazondevices.amazon.ca/mars/widget/accessory-upsell-product-view/1.0/get-product-view"

    def __get_soup(self) -> None:
        self.html = requests.get(
            self.url, headers=HEADER, params=self.request_params
        ).content
        self.soup = BeautifulSoup(self.html, "lxml")

    def get_price(self) -> float:
        self.__get_soup()
        self.price = float(
            self.soup.find_all(class_=re.compile("buying-price"))[0].text.replace(
                "$", ""
            )
        )
        return self.price


if __name__ == "__main__":
    kindle = AmazonProdcut("B08N36XNTT")
    kindle.get_price()
