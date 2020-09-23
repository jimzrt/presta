import requests
from lxml import etree
from io import StringIO, BytesIO

URL="https://fursandmore.com/api"
TOKEN=""
session = requests.Session()
session.auth = (TOKEN,"")
parser = etree.XMLParser(remove_blank_text=True)

def get_xml(response):
    root = etree.fromstring(response.content, parser)
    return root

def print_xml(xml_element):
    print(etree.tostring(xml_element, pretty_print=True,encoding='unicode'))

def get_categories(session):
    response = session.get(URL+"/categories")
    root = get_xml(response)
    return root

def get_product_image_ids(session):
    response = session.get(URL+"/images/products")
    xml = get_xml(response)
    images = xml.find("images")
    ids = [int(image.get("id")) for image in images]
    return ids

def delete_product_images(session, image_id):
    response = session.get(URL+"/images/products/" + str(image_id))
    xml = get_xml(response)
    images = xml.find("image")
    ids = [int(image.get("id")) for image in images]
    for _id in ids:
        response = session.delete(URL+"/images/products/" + str(image_id) + "/" + str(_id))
        print(response.status_code)

def get_product_ids(session):
    response = session.get(URL+"/products")
    xml = get_xml(response)
    products = xml.find("products")
    product_ids = [int(product.get("id")) for product in products]
    return product_ids

def delete_products(session, ids):
    for _id in ids:
        response = session.delete(URL + "/products/" + str(_id))
        print(response.status_code)

product_ids = get_product_ids(session)
print(product_ids)
delete_products(session, product_ids)
product_ids = get_product_ids(session)
print(product_ids)

# image_ids = get_product_image_ids(session)
# print(image_ids)
# for image_id in image_ids:
#     delete_product_images(session, image_id)
# image_ids = get_product_image_ids(session)
# print(image_ids)




