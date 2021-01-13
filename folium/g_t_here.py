# author: 杭导
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple folium

import folium
Map=folium.Map(location=[30.5,114.3],
            zoom_start=14,
            tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={x}&y={y}&z={z}',
            attr='default'
        )
Map.add_child(folium.LatLngPopup())
Map.save('gettogether.html')



