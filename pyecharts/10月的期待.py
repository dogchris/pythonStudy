# author: E酱
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyecharts

from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType

initOpts = opts.InitOpts("1800px", "900px")
c = (
    Geo(initOpts)
    .add_schema(maptype="china")
    .add(
        "",
        [("肇庆", '东华'), ("武汉", '陈冉'), ("合肥", '杭导'), 
         ('通辽', '锋哥'), ('南宁', '萌、二姐'), 
         ('茂名', '钟钟孟孟康康'), ('庆阳', '星俨')],
        type_=ChartType.EFFECT_SCATTER,
        color="orange",
        blur_size=100
    )
    .add(
        "去向",
        [("肇庆", "通辽"), ("合肥", "通辽"), ("武汉", "通辽"), 
         ("南宁", "通辽"), ("南宁", "通辽"), ("茂名", "通辽"), ("庆阳", "通辽")],
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="green"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.2, color='red'),
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="10月的期待"))
    .render("10月的期待.html")
)