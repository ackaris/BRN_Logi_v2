import math
import container as cont
import container
coulmn_counter=0
class layer:
    def __init__(self,type,container,height):
        self.type=type
        self.products=[]
        self.height=height
        self.length=0
        container.coulmn_layers.append(self)
def create(i,container):
    if math.floor(container.coulmn_heights[container.active_coulmn-1]+math.sqrt(3)*i.model.r)<container.height:
        if len(container.coulmn_layers)>0:
            if container.coulmn_layers[-1].type==1:

                container.coulmn_heights[container.active_coulmn-1]=math.floor(container.coulmn_heights[container.active_coulmn-1]+math.sqrt(3)*i.model.r)
                layer(2, container,container.coulmn_heights[container.active_coulmn-1]-i.model.r)
            else:

                container.coulmn_heights[container.active_coulmn-1] = math.floor(container.coulmn_heights[container.active_coulmn-1]+math.sqrt(3)*i.model.r)
                layer(1, container,container.coulmn_heights[container.active_coulmn-1]-i.model.r)
        else:

            container.coulmn_heights[container.active_coulmn-1]=2*i.model.r
            layer(1, container, container.coulmn_heights[container.active_coulmn-1]-i.model.r)
    else:

        create_coulumn(i,0,container)

def add_product_to_layer(i,max_product_per_layer,container):
    if container.coulmn_layers[-1].type == 1:
        if len(container.coulmn_layers[-1].products) < max_product_per_layer:
            container.coulmn_layers[-1].products.append(i)
            container.coulmn_layers[-1].length = max(container.coulmn_layers[-1].length, i.model.h)
        else:
            create(i,container)
            container.coulmn_layers[-1].products.append(i)
            container.coulmn_layers[-1].length = max(container.coulmn_layers[-1].length, i.model.h)
    elif container.coulmn_layers[-1].type == 2:

        if len(container.coulmn_layers[-1].products) < max_product_per_layer - 1:
            container.coulmn_layers[-1].products.append(i)
            container.coulmn_layers[-1].length = max(container.coulmn_layers[-1].length, i.model.h)
        else:
            create(i,container)
            container.coulmn_layers[-1].products.append(i)
            container.coulmn_layers[-1].length = max(container.coulmn_layers[-1].length, i.model.h)

def create_coulumn(i,max_product_per_layer,container):

    container.coulmn_heights.append(0)

    container.coulms_mem.append(container.coulmn_layers)
    print(container.coulmn_layers)
    if len(container.coulmn_layers)>0:
        print(container.cont_occ_lenth)
        container.coulmn_layers[-1].length = 0
        container.coulmn_layers=[]

    container.cont_occ_lenth += i.model.h
    container.active_coulmn= container.active_coulmn + 1
    create(i, container)


