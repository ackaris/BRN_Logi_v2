container_mem=[]
class container:
    def __init__(self,width,len,height):
        self.width=width
        self.len=len
        self.height=height
        self.coulmn_layers=[]
        self.coulmn_heights=[]
        self.active_coulmn=0
        self.coulms_mem=[]
        self.coulmns_per_container=0
        self.cont_occ_lenth=0
        container_mem.append(self)
def create_continer(w,l,h):

    container(w,l,h)