import container
import product
import layer


def calc(container1,model1):

    vurducounter=0
    for i in product.product_lib:
        max_product_per_layer = round(container1.width / (i.model.r * 2))
        if container.container_mem[-1].cont_occ_lenth<=container.container_mem[-1].len:
            if container.container_mem[-1].active_coulmn==0:
                layer.create_coulumn(i,max_product_per_layer,container.container_mem[-1])
            layer.add_product_to_layer(i,max_product_per_layer,container.container_mem[-1])
        else:
            print('vurdu1')
            vurducounter+=1
            if vurducounter==0:
                layer.create_coulumn(i, max_product_per_layer, container.container_mem[-1])
            if len(container.container_mem[-1].coulmn_layers)<3:
                print('geldi')
                layer.add_product_to_layer(i, max_product_per_layer, container.container_mem[-1])
                print(container.container_mem[-1].coulmn_layers)
            else:
                container.container_mem[-1].coulms_mem.append(container.container_mem[-1].coulmn_layers)
                container.create_continer(container.container_mem[-1].width,container.container_mem[-1].len,container.container_mem[-1].height)
                if container.container_mem[-1].active_coulmn==0:
                    layer.create_coulumn(i,max_product_per_layer,container.container_mem[-1])
                layer.add_product_to_layer(i, max_product_per_layer, container.container_mem[-1])


    container.container_mem[-1].coulms_mem.append(container.container_mem[-1].coulmn_layers)
    '''container_mem[-1].coulms_mem.pop(0)'''
    for cont in container.container_mem:
        cont.coulms_mem.pop(0)
def dynamic_fontsize(n_cols, min_size=6, max_size=12):
    return max(min_size, min(max_size, int(40 / n_cols)))
def showplot(container1):
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches

    # Get the max number of columns across all containers
    max_columns = max(len(cont.coulms_mem) for cont in container.container_mem)
    num_rows = len(container.container_mem)

    fig_width = max_columns * 4  # 4 inches per column
    fig, ax = plt.subplots(num_rows, max_columns, figsize=(fig_width, num_rows * 4))

    # Make ax 2D even if 1 row or 1 column
    if num_rows == 1:
        ax = [ax]  # wrap into a list
    if max_columns == 1:
        ax = [[col] for col in ax]

    total_product = 0

    for row_idx, cont in enumerate(container.container_mem):
        total_product_in_cont = 0
        for col_idx, i in enumerate(cont.coulms_mem):
            rect = patches.Rectangle((0, 0), container1.width, container1.height, linewidth=2, edgecolor='black',
                                     facecolor='none')
            ax[row_idx][col_idx].add_patch(rect)

            for j in i:
                layer_prodcount = 0
                x_coord = 0
                for prod in j.products:
                    if j.type == 1 and layer_prodcount == 0:
                        x_coord += prod.model.r
                    elif j.type == 1:
                        x_coord += prod.model.r * 2
                    elif j.type == 2:
                        x_coord += prod.model.r * 2
                    circle = patches.Circle((x_coord, j.height), prod.model.r, linewidth=2, edgecolor='blue',
                                            facecolor='none')
                    ax[row_idx][col_idx].add_patch(circle)
                    layer_prodcount += 1
                    total_product_in_cont += 1
                    total_product += 1

            font_size = dynamic_fontsize(max_columns)

            # Inside your plotting loop:
            ax[row_idx][col_idx].set_title(
                f'CONTAINER: {row_idx + 1}\nCOULMN: {col_idx + 1}\nIN CONTAINER: {total_product_in_cont}\n TOTAL: {total_product}\n OCC Length: {cont.cont_occ_lenth}',
                fontsize=font_size
            )
            ax[row_idx][col_idx].set_xlim(0, container1.width)
            ax[row_idx][col_idx].set_ylim(0, container1.height)
            ax[row_idx][col_idx].set_aspect('equal')

    # Hide unused subplots
    for row_idx in range(num_rows):
        for col_idx in range(len(container.container_mem[row_idx].coulms_mem), max_columns):
            fig.delaxes(ax[row_idx][col_idx])  # Remove unused axes

    plt.subplots_adjust(hspace=0.7)

    # Optional: draw line in middle of figure
    line = plt.Line2D([0.05, 0.95], [0.55, 0.55], transform=fig.transFigure,
                      color='black', linewidth=4)
    fig.add_artist(line)

    plt.show()
def print_stats():
    '''layer.layer_lib_memory.append(layer.layer_lib)
    layer.layer_lib = []'''

    for cont in container.container_mem:
        for i in cont.coulms_mem:
            print(i)
            for j in i:
                print(len(j.products))
