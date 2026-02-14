import os
import json
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0923",
    database="phonepe"
)
cursor = conn.cursor()

path = "pulse/data/aggregated/transaction/country/india/state"

for state in os.listdir(path):
    state_path = path + "/" + state
    for year in os.listdir(state_path):
        year_path = state_path + "/" + year
        for file in os.listdir(year_path):
            with open(year_path + "/" + file) as f:
                data = json.load(f)

                quarter = int(file.strip(".json"))

                for item in data["data"]["transactionData"]:
                    name = item["name"]
                    for payment in item["paymentInstruments"]:
                        count = payment["count"]
                        amount = payment["amount"]

                        cursor.execute("""
                            INSERT INTO aggregated_transaction
                            VALUES (%s,%s,%s,%s,%s,%s)
                        """,(state, year, quarter, name, count, amount))

conn.commit()
path = "pulse/data/aggregated/user/country/india/state"

for state in os.listdir(path):
    for year in os.listdir(f"{path}/{state}"):
        for file in os.listdir(f"{path}/{state}/{year}"):

            with open(f"{path}/{state}/{year}/{file}") as f:
                data = json.load(f)

            quarter = int(file.strip(".json"))

            try:
                for brand in data["data"]["usersByDevice"]:
                    cursor.execute("""
                        INSERT INTO aggregated_user
                        VALUES (%s,%s,%s,%s,%s,%s)
                    """, (
                        state, year, quarter,
                        brand["brand"],
                        brand["count"],
                        brand["percentage"]
                    ))
            except:
                pass
path = "pulse/data/aggregated/insurance/country/india/state"

for state in os.listdir(path):
    for year in os.listdir(f"{path}/{state}"):
        for file in os.listdir(f"{path}/{state}/{year}"):

            with open(f"{path}/{state}/{year}/{file}") as f:
                data = json.load(f)

            quarter = int(file.strip(".json"))

            for item in data["data"]["transactionData"]:
                ins_type = item["name"]

                for ins in item["paymentInstruments"]:
                    cursor.execute("""
                        INSERT INTO aggregated_insurance
                        VALUES (%s,%s,%s,%s,%s,%s)
                    """, (
                        state, year, quarter,
                        ins_type,
                        ins["count"],
                        ins["amount"]
                    ))
path ="pulse/data/map/transaction/hover/country/india/state"

for state in os.listdir(path):
    for year in os.listdir(f"{path}/{state}"):
        for file in os.listdir(f"{path}/{state}/{year}"):

            with open(f"{path}/{state}/{year}/{file}") as f:
                data = json.load(f)

            quarter = int(file.strip(".json"))

            for dist in data["data"]["hoverDataList"]:
                cursor.execute("""
                    INSERT INTO map_transaction
                    VALUES (%s,%s,%s,%s,%s,%s)
                """, (
                    state, year, quarter,
                    dist["name"],
                    dist["metric"][0]["count"],
                    dist["metric"][0]["amount"]
                ))
path = "pulse/data/map/user/hover/country/india/state"

for state in os.listdir(path):
    for year in os.listdir(f"{path}/{state}"):
        for file in os.listdir(f"{path}/{state}/{year}"):

            with open(f"{path}/{state}/{year}/{file}") as f:
                data = json.load(f)

            quarter = int(file.strip(".json"))

            for dist in data["data"]["hoverData"].items():
                cursor.execute("""
                    INSERT INTO map_user
                    VALUES (%s,%s,%s,%s,%s,%s)
                """, (
                    state, year, quarter,
                    dist[0],
                    dist[1]["registeredUsers"],
                    dist[1]["appOpens"]
                ))
path ="pulse/data/map/insurance/hover/country/india/state"

for state in os.listdir(path):
    for year in os.listdir(f"{path}/{state}"):
        for file in os.listdir(f"{path}/{state}/{year}"):

            with open(f"{path}/{state}/{year}/{file}") as f:
                data = json.load(f)

            quarter = int(file.strip(".json"))

            for dist in data["data"]["hoverDataList"]:
                cursor.execute("""
                    INSERT INTO map_insurance
                    VALUES (%s,%s,%s,%s,%s,%s)
                """, (
                    state, year, quarter,
                    dist["name"],
                    dist["metric"][0]["count"],
                    dist["metric"][0]["amount"]
                ))
path = "pulse/data/top/transaction/country/india/state"

for state in os.listdir(path):
    for year in os.listdir(f"{path}/{state}"):
        for file in os.listdir(f"{path}/{state}/{year}"):

            with open(f"{path}/{state}/{year}/{file}") as f:
                data = json.load(f)

            quarter = int(file.strip(".json"))

            for item in data["data"]["pincodes"]:
                cursor.execute("""
                    INSERT INTO top_transaction
                    VALUES (%s,%s,%s,%s,%s,%s)
                """, (
                    state, year, quarter,
                    item["entityName"],
                    item["metric"]["count"],
                    item["metric"]["amount"]
                ))
path = "pulse/data/top/user/country/india/state"

for state in os.listdir(path):
    for year in os.listdir(f"{path}/{state}"):
        for file in os.listdir(f"{path}/{state}/{year}"):

            with open(f"{path}/{state}/{year}/{file}") as f:
                data = json.load(f)

            quarter = int(file.strip(".json"))

            for item in data["data"]["pincodes"]:
                cursor.execute("""
                    INSERT INTO top_user
                    VALUES (%s,%s,%s,%s,%s)
                """, (
                    state, year, quarter,
                    item["name"],
                    item["registeredUsers"]
                ))
path = "pulse/data/top/user/country/india/state"

for state in os.listdir(path):
    for year in os.listdir(f"{path}/{state}"):
        for file in os.listdir(f"{path}/{state}/{year}"):

            with open(f"{path}/{state}/{year}/{file}") as f:
                data = json.load(f)

            quarter = int(file.strip(".json"))

            for item in data["data"]["pincodes"]:
                cursor.execute("""
                    INSERT INTO top_user
                    VALUES (%s,%s,%s,%s,%s)
                """, (
                    state, year, quarter,
                    item["name"],
                    item["registeredUsers"]
                ))
conn.commit()
cursor.close()
conn.close()

