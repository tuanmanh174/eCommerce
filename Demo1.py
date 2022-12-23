import Connection
class Product:
    def __init__(self, productName, productCode, Price):
        self.productName = productName
        self.productCode = productCode
        self.Price = Price

   

    def InsertData(self):
        cnn = Connection.getConnection()
        response = ''
        try:
            cursor = cnn.cursor()
            sql = 'insert into product (ProductName, ProductCode, Price) values ("'+ self.productName +'", "'+ self.productCode +'", '+ self.Price +')'
            cursor.execute(sql)
            cnn.commit()
        except:
            response = 'Hệ thống đang lỗi, vui lòng liên hệ với admin'
            return response
        finally:
            cnn.close()
            response = 'Bạn đã khởi tạo thành công'
            return response

    def getData(self):
        cnn = Connection.getConnection()
        response = ''
        try:
            cursor = cnn.cursor()
            sql = 'select * from product'
            cursor.execute(sql)
            for row in cursor:
                print(row)
        finally:
            cnn.close()
    
  

    
        