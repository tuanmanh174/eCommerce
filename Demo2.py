from Demo1 import Product

 
productName = input("Nhập tên sản phẩm : ")
productCode = input("Nhập mã sản phẩm : ")
price = input("Nhập giá sản phẩm : ")

demo = Product(productName, productCode, price)

response = demo.InsertData()
manhdt

