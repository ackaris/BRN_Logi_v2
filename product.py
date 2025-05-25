product_lib=[]
class product:
    def __init__(self,model):
        self.model=model
        product_lib.append(self)
def create(model,amount):
    for i in range(0,amount):
        product(model)
