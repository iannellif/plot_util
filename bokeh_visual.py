from bokeh.models import ColumnDataSource, CategoricalColorMapper
from bokeh.transform import factor_cmap
from bokeh.palettes import Category10
from bokeh.plotting import figure

class BokehVisualizer:
    def __init__(self, data):
        self.data = data
        
    def scatter(self, x, y, color):
        source = ColumnDataSource(self.data)
        colors = Category10[10]
        color_mapper = CategoricalColorMapper(factors=source.data[color].unique(), palette=colors)
        p = figure()
        p.scatter(x=x, y=y, source=source, color={'field': color, 'transform': color_mapper})
        return p
        
    def line(self, x, y, color):
        source = ColumnDataSource(self.data)
        colors = Category10[10]
        color_mapper = CategoricalColorMapper(factors=source.data[color].unique(), palette=colors)
        p = figure()
        p.line(x=x, y=y, source=source, color={'field': color, 'transform': color_mapper})
        return p
        
    def bar(self, x, y, color):
        source = ColumnDataSource(self.data)
        colors = Category10[10]
        color_mapper = factor_cmap(field_name=color, palette=colors, factors=source.data[color].unique())
        p = figure()
        p.vbar(x=x, top=y, source=source, width=0.5, color=color_mapper)
        return p
        
    def histogram(self, x, bins=10):
        source = ColumnDataSource(self.data)
        p = figure()
        p.quad(bottom=0, top='count', left=x+'_left', right=x+'_right', source=source, bins=bins)
        return p
        
    def heatmap(self, x, y, color):
        source = ColumnDataSource(self.data)
        p = figure()
        p.rect(x=x, y=y, width=1, height=1, source=source, fill_color={'field': color}, line_color=None)
        return p
        
    def boxplot(self, x, y, color):
        source = ColumnDataSource(self.data)
        p = figure()
        p.violin(x=color, y=y, source=source, width=0.8, color=color)
        p.circle(x=color, y=y, source=source, size=5, fill_color='white')
        return p


      
      
if __name__ == '__main__':
  

    import pandas as pd
    from bokeh.io import show

    data = pd.read_csv('data.csv')
    visualizer = BokehVisualizer(data)

    scatter_plot = visualizer.scatter('x', 'y', 'color')
    show(scatter_plot)

    line_plot = visualizer.line('x', 'y', 'color')
    show(line_plot)

    bar_chart = visualizer.bar('x', 'y', 'color')
    show(bar_chart)

    histogram = visualizer.histogram('x', bins=20)
    show(histogram)

    heatmap = visualizer.heatmap('x', 'y', 'color')
    show(heatmap)

    boxplot = visualizer.boxplot('color', 'y', 'color')
    show(boxplot)
