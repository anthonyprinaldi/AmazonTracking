from AmazonProduct import AmazonProdcut
import json
from datetime import datetime
from SendText import sendMsg

if __name__ == "__main__":
    with open("product_info.json", "r") as f:
        data = json.load(f)

    product = AmazonProdcut(data["ASIN"])

    try:
        price = product.get_price()

        with open(f"history-{data['product']}.txt", "a+") as f:
            f.seek(0)
            last_line = f.readlines()[-1]
            f.write(f"{datetime.now().strftime('%d/%m/%Y')}, {price}\n")

        last_price = float(last_line.split(",")[-1].replace("\n", "").strip())

        if price < last_price:
            sendMsg(
                f'Subject: NEW LOW PRICE\n{data["product"]} reached a new low price of ${price}.'
            )

        print(f'Completed day {datetime.now().strftime("%d/%m/%Y")} success')

    except Exception as e:
        print(f"ERROR: {e}")
