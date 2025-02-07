#polyhedron.py
import json
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# GeoJSONファイルを読み込む
with open('measure_epsg4326.geojson', 'r', encoding='utf-8') as f:
    geojson_data = json.load(f)

# 3Dプロットの準備
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 各ポリゴンを処理
for feature in geojson_data['features']:
    if feature['geometry']['type'] == 'Polygon':
        # 座標を取得
        coordinates = np.array(feature['geometry']['coordinates'][0])
        
        # ポリゴンを3D表示用に変換
        poly3d = [coordinates]  # 3D表示用に座標をリスト化
        
        # Poly3DCollectionを作成して描画
        collection = Poly3DCollection(poly3d, alpha=0.5)
        collection.set_facecolor('blue')
        ax.add_collection3d(collection)
        
        # 座標の範囲を取得（軸の設定用）
        x = coordinates[:, 0]
        y = coordinates[:, 1]
        z = coordinates[:, 2]
        
        # 輪郭線を描画
        ax.plot(x, y, z, 'r-')

# 軸の範囲を設定
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_zlabel('Altitude')
ax.set_title('3D Polygons from GeoJSON')

# データの範囲に合わせて軸の範囲を自動調整
ax.autoscale()

# 視点の設定
ax.view_init(elev=30, azim=45)

# グリッドを表示
ax.grid(True)

# グラフの表示
plt.show()