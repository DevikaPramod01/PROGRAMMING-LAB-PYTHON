class Publisher:
    def __init__(self,bname):
        self.bname=bname
    def view_detail(self):
        print("name of publisher ",self.bname)
class Book(Publisher):
    def __init__(self,title,author,bname):
        self.title=title
        self.author=author
        super().__init__(bname)
    def view_detail(self):
        print("Book Title ",self.title)
        print("Book Author ",self.author)
        super().view_detail()
class Python(Book):
    def __init__(self,title,author,publisher,price,pnum):
        self.price=price
        self.pnum=pnum
        super().__init__(title,author,publisher)
    def view_detail(self):
        super().view_detail()
        print("Book Price ",self.price)
        print("Total Pages ",self.pnum)
p=Python("C","Balaguruswamy","DC Books",1000,850)
p.view_detail()
