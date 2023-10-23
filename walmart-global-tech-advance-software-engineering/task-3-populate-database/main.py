
import csv
import uuid
import sqlite3
from os import listdir
from os.path import join

data_csv_files = [join('./data/', f) for f in listdir('./data')]

products = []
shipments = {}

for csv_file in data_csv_files:
    with open(csv_file) as csvfile:
        csv_content = csv.reader(csvfile, delimiter=',')

        header = next(csv_content)

        product_idx = header.index('product') if 'product' in header else -1
        product_quantity_idx = header.index('product_quantity') if 'product_quantity' in header else -1
        origin_warehouse_idx = header.index('origin_warehouse') if 'origin_warehouse' in header else -1
        destination_store_idx = header.index('destination_store') if 'destination_store' in header else -1
        shipment_identifier_idx = header.index('shipment_identifier') if 'shipment_identifier' in header else -1

        for r in csv_content:
            if product_idx >= 0:
                products.append(r[product_idx])

            if product_idx >= 0 and product_quantity_idx >= 0 and origin_warehouse_idx >= 0 and destination_store_idx >= 0:
                shipments[str(uuid.uuid4())] = {
                    'product': r[product_idx],
                    'quantity': int(r[product_quantity_idx]),
                    'origin': r[origin_warehouse_idx],
                    'destination': r[destination_store_idx]}
                continue

            if shipment_identifier_idx >= 0 and product_idx >= 0:
                if shipments.get(r[shipment_identifier_idx]) is None:
                    shipments[r[shipment_identifier_idx]] = {
                    'product': r[product_idx],
                    'quantity': 0,
                    'origin': None,
                    'destination': None}

                shipments[r[shipment_identifier_idx]]['quantity'] += 1

                continue

            if shipment_identifier_idx >= 0 and origin_warehouse_idx >= 0 and destination_store_idx >= 0:
                if shipments.get(r[shipment_identifier_idx]) is None:
                    shipments[r[shipment_identifier_idx]] = {
                    'product': None,
                    'quantity': 0,
                    'origin': r[origin_warehouse_idx],
                    'destination': r[destination_store_idx]}

                    continue
                
                shipments[r[shipment_identifier_idx]]['origin'] = r[origin_warehouse_idx]
                shipments[r[shipment_identifier_idx]]['destination'] = r[destination_store_idx]

print('number of products: ', len(list(set(products))))
print('number of shipments: ', len(shipments))

con = sqlite3.connect('./shipment_database.db')
cur = con.cursor()

cur.executemany('insert or ignore into product (name) values (?)', [(p,) for p in products])

con.commit()

products = cur.execute('select * from product')
products = products.fetchall()

# note: the provided schema does not make use of shipment id
# this might cause duplication depending on how the script is ran
# better version of this is to change it to uuid and make use of
# the shipment id
shipments = [
    (next(p_id for (p_id, p_name) in products if p_name == s['product']), s['quantity'], s['origin'], s['destination']) for s in shipments.values()]

cur.executemany('insert into shipment (product_id, quantity, origin, destination) values (?, ?, ?, ?)', shipments)

con.commit()
