# Colors
For a list of allowed colors names and their associated hex values see the file colors.csv. To see the colors themselves see the file  matploblib_csscolors.png, which was taken from from https://matplotlib.org/gallery/color/named_colors.html

# Plotnine

Plotnine (and its source ggplot) are my go to when it comes to plotting, as the code is simple intuitive and built in layers.  I only go to matplotlib, seaborn, or plotly when I need to plot something that plotnine can not plot.

  
For the most part you can use the ggplot cheatsheet, found [here](https://www.rstudio.com/wp-content/uploads/2015/03/ggplot2-cheatsheet.pdf) as the plotnine cheetsheat, as in most cases there is a one to one matching.  Here I am just going to review the plots and arguments I use most often as well as the other errata. 

## Plot Basics

All plots in plotnine start with the basic command `ggplot(df, aes(x='x column', y='y column', color='color column', fill='fill column')`, where `df` is the dataframe, `x column` is the name of the dataframe column used for the x-axis, `y column` is the name of the dataframe column used for the y axis.  The `color` and `fill` arguments are optional and only used when you want color or fill the data according to the values in the color or fill columns.  For example if you were making a dot plot of cars vs mpg and you wanted to fill the dots according to the manufacturer, in that case `fill=car_manufacturer` 

If you have the same data that you want to plot multiple ways, e.g., line plot and dot plot, you can declare the aesthetics, `aes`, in the ggplot call, which is then inherited by all the following code unless you explicitly change the aesthetics.  If you want to be explicit about the data used in every plotting layer, you can call the aesthetics each geom.  You can even refer to a new dataframe in a geom by setting `data=new_df`. 

## Plot Types



- Histogram
  - `geom_histogram(aes(x, y, color*, fill*, alpha*) , bins)`
- Bar
  - `geom_bar(aes(x, y, color*, alpha*, fill*), position)`
- Point / Scatterplot
  - `geom_point(aes(x, y, color*, alpha*, fill*, shape*, size*))`
- Line
  - `geom_line(aes(x, y, color*, alpha*, fill*, size*, linetype*))`
- Jitter
  - `geom_jitteraes(aes(x, y, color*, alpha*, fill*, shape*, size*))`


Starred Arguments can exist either inside and outside of the aes tuple.  Their location depends on whether or not they are variables or static values.  If they are variables, like x and y, they are inside the aes tuple, otherwise they are placed outside of it.

## Figure Adjustments
- x label / y label
  - `xlab('x-label-string')` 
  - `ylab('y-label-string')`
- figure size
  - `theme(figure_size=(width-float, length-float)))`
- zoom in 
  - `coord_cartesian(xlim=(xmin-float, xmax-float), ylim=(ymin-float, ymax-float))`
- rotate tick labels
  - `theme(axis_text_x=element_text(rotation=x-rotation-degrees, hjust=0.5))`
  - `theme(axis_text_y=element_text(rotation=x-rotation-degrees, hjust=0.5))`
- reorder x/y axis values (used for categorical x/y values)
  - `scale_x_discrete(limits=new-order-list)`
  - `scale_y_discrete(limits=new-order-list)`
- log scale x/y axis
  - `scale_x_log10()`
  - `scale_y_log10()`



