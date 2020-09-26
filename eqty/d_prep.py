#!bin/python
def main(show=0):
    '''show=number of colorscheme;


    return (train_x,train_y,test_x,test_y)'''

    # new functionality:
    # TODO: 

    import matplotlib.pyplot as plt
    import datetime as dt
    import pandas as pd
    import tx,ty,plt_heatmap as hmap
    import numpy as np

    # get data
    try:
        dataX = tx.load_local_x()
    except:
        tx.fetch()
        dataX = tx.load_local_x()

    dataY = ty.load_y() # np.array(23,12), Jan1998 : Dec2020

    # write a procedure to automate pre-processing. 
    #
    # find shortest dataset, identify its start date? , cut all train_x and train_y from the back. 
    for idx,dset in dataX.items():
        print(dset.loc[:,'Date'].min())
    
    #TESTED:
    train_x = dataX['rub.csv'].iloc[1:,1:]['Close'].to_numpy()[:-1] # check if the dates are right
    train_x = np.nan_to_num(train_x, nan=27)# procedure to impute missing data!!! 
    train_y = dataY.reshape(-1)[12*(2004-1998):-4] # Jan'04: Aug'20 

    adjst_usd = np.multiply(train_y,1/train_x)
    if show!=0:

        def fit_grid(plot):
            ''' input: here must come a np.array, 
            DO: move to another module
            ??
            '''
            import numpy as np

            plot = plot.reshape(1,-1)  
            plot = np.append(plot,np.ones(12-plot.shape[1]%12))
            plot = plot.reshape((plot.shape[0]//12,12))
            return plot

        plot = fit_grid(adjst_usd)

        def wrap(scheme_number=25,init_year= 2004):
            '''Rename'''

            import calendar
            
            colors = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']
            years = list(range(init_year,2021))
            months = [calendar.month_abbr[i] for i in range(1,13)]
            fig, ax = plt.subplots()
            im, cbar = hmap.heatmap(plot.T,months,years, ax=ax,
                               cmap=colors[scheme_number],
                               cbarlabel=" colorscheme:{}".format(colors[scheme_number]))

            fig.tight_layout()
            plt.show()
            

        wrap(show)

    test_x,test_y = None, None
    return (train_x,train_y,test_x,test_y)

main()
