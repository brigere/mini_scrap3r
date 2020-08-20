from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup as bs
import json

products= data.find_all("img",{"class":["lazyautosizes","item-image","img-absolute","img-absolute-centered","blur-up","lazyloaded"]})
print(type(products)) #<class 'bs4.element.ResultSet'>

# product = products[1]
# print(type(product)) #<class 'bs4.element.Tag'>
name = product.get('alt')
# print(type(name)) #string

productList = []
for i in range(len(products)):
    product = products[i]
    try:
        product_name = product.get('alt') #extrae string con nombre de producto
        product_imgs = product.get('srcset') #extrae un string con dos urls
        selected_img = product_imgs.split(", ")[1] #separo las urls y elijo la segunda porque tiene mejor resolucion
        product_img = selected_img[0:-5] #limpio la url
    except:
        product_name = product.get('alt')
        product_imgs = product.get('data-srcset')
        selected_img = product_imgs.split(", ")[1] 
        product_img = selected_img[0:-5] 
    productList.append({
        "name":product_name,
        "img":product_img
    })

def jointProducts(url1,url2,destination):
    lista =[]
    file1 = open(url1,'r')
    file2 = open(url2,'r')

    _file1 = json.loads(file1.read())
    _file2 = json.loads(file2.read())


    for element1 in _file1:
        for element2 in _file2:
            if element1['name']==element2['producto']:
                lista.append({
                    "id":element2["id"],
                    "producto":element2["producto"],
                    "variante":element2["variante"],
                    "precio":element2["precio"],
                    "img":element1["img"]
                })

    file3 = open(destination,'w')
    file3.write(
        json.dumps(lista)
    )
    file3.close()

jointProducts('updatedProducts.json','productos.json','final.json')


## Save into a JSON file
import json
updatedFile = open('updatedProducts.json','w')
a = json.dumps(productList)
updatedFile.write(a)
updatedFile.close()

## Listar todos los tipos de ID 
categories=[]
def findCategories(jsonFile):
    file = json.loads(open(jsonFile,'r').read())
    for product in file:
        category = product['id'][0:3]
        if not (category in categories):
            categories.append(category)

# findCategories('final.json')
print(categories)
print(len(categories))
['ACE', 'CON', 'KIO', 'FRS', 'CER', 'FRU', 'LEG', 
'END', 'SUP', 'BUD', 'DIS', 'GAL', 'UNT', 'DOY', 'FID',
 'SEM', 'VEG', 'HAR', 'JUG', 'LEC', 'MER', 'MIX', '├æO', 'PAN', 
'PRE', 'SAL', 'INF', 'YER', 'YOG'] 29 categories
        

    
    
