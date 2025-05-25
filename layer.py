import math
import container as con_gen
coulmn_counter=0
class layer:
    def __init__(self,type,container,height):
        self.type=type
        self.products=[]
        self.height=height
        self.length=0
        self.layer_occ_width=0
        container.coulmn_layers.append(self)
def create(i,container):
    if i.model.pack_type==0:
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

            create_coulumn(i,container)
    elif i.model.pack_type==1:
        if math.floor(
                container.coulmn_heights[container.active_coulmn - 1] + i.model.r) < container.height:

            if len(container.coulmn_layers) > 0:
                if container.coulmn_layers[-1].type == 1:
                    container.coulmn_heights[container.active_coulmn - 1] = math.floor(
                        container.coulmn_heights[container.active_coulmn - 1] +i.model.r)
                    layer(2, container, container.coulmn_heights[container.active_coulmn - 1] - i.model.r)
                else:

                    container.coulmn_heights[container.active_coulmn - 1] = math.floor(
                        container.coulmn_heights[container.active_coulmn - 1] +i.model.r)
                    layer(1, container, container.coulmn_heights[container.active_coulmn - 1] - i.model.r)
            else:

                container.coulmn_heights[container.active_coulmn - 1] = i.model.r
                layer(1, container, container.coulmn_heights[container.active_coulmn - 1] - i.model.r)
            print(f'Cont occ height: {con_gen.container_mem[-1].coulmn_heights[-1]}')
        else:

            create_coulumn(i, container)

def add_product_to_layer(i,container):
    if i.model.pack_type==0:
        if container.coulmn_layers[-1].type == 1:
            if container.coulmn_layers[-1].layer_occ_width + i.model.r*2 < con_gen.container_mem[-1].width:
                container.coulmn_layers[-1].products.append(i)
                container.coulmn_layers[-1].length = max(container.coulmn_layers[-1].length, i.model.h)
                container.coulmn_layers[-1].layer_occ_width  += i.model.r*2
            else:
                create(i,container)
                container.coulmn_layers[-1].products.append(i)
                container.coulmn_layers[-1].length = max(container.coulmn_layers[-1].length, i.model.h)
                container.coulmn_layers[-1].layer_occ_width  += i.model.r * 2
        elif container.coulmn_layers[-1].type == 2:

            if container.coulmn_layers[-1].layer_occ_width + i.model.r *4< con_gen.container_mem[-1].width:
                container.coulmn_layers[-1].products.append(i)
                container.coulmn_layers[-1].length = max(container.coulmn_layers[-1].length, i.model.h)
                container.coulmn_layers[-1].layer_occ_width += i.model.r * 2
            else:
                create(i,container)
                container.coulmn_layers[-1].products.append(i)
                container.coulmn_layers[-1].length = max(container.coulmn_layers[-1].length, i.model.h)
                container.coulmn_layers[-1].layer_occ_width += i.model.r * 2
    elif i.model.pack_type==1:

        if con_gen.container_mem[-1].width - container.coulmn_layers[-1].layer_occ_width > i.model.r and layerfirst(container,container.coulmn_layers[-1]):
            container.coulmn_layers[-1].products.append(i)
            container.coulmn_layers[-1].length = max(container.coulmn_layers[-1].length, i.model.h,i.model.r)
            container.coulmn_layers[-1].layer_occ_width += i.model.r
        if container.coulmn_layers[-1].layer_occ_width + i.model.long_Egde < con_gen.container_mem[-1].width:
            container.coulmn_layers[-1].products.append(i)
            container.coulmn_layers[-1].length = max(container.coulmn_layers[-1].length, i.model.h)
            container.coulmn_layers[-1].layer_occ_width += i.model.long_Egde
        else:
            create(i, container)
            container.coulmn_layers[-1].products.append(i)
            container.coulmn_layers[-1].length = max(container.coulmn_layers[-1].length, i.model.h)
            container.coulmn_layers[-1].layer_occ_width += i.model.long_Egde
def create_coulumn(i,container):

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

def layerfirst(container,layer):
    return container.coulmn_layers.index(layer)==0
