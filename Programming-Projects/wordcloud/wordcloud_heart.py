from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import random

# -------------------------
# 1️⃣ 定义词频字典
# -------------------------
frequencies = {
    "mind my own business": 10,
    "get the hint": 7,
    "make a scene": 8,
    "fed up with": 5,
    "cold calls": 6,
    "in the mood for it": 4,
    "patience was wearing thin": 3,
    "Learn": 5,
    "Project": 4,
    "Data": 6
}

# -------------------------
# 2️⃣ 生成心形 mask（无需图片文件）
# -------------------------
# 创建一个简单的心形轮廓函数
x, y = np.ogrid[-1:1:800j, -1:1:800j]
mask_image = ((x**2 + y**2 - 0.3)**3 - x**2 * y**3) <= 0

# -------------------------
# 3️⃣ 自定义随机颜色函数
# -------------------------
def random_color(word, font_size, position, orientation, random_state=None, **kwargs):
    h = random.randint(0, 360)       # 色相
    s = random.randint(60, 100)      # 饱和度
    l = random.randint(30, 70)       # 明度
    return f"hsl({h}, {s}%, {l}%)"

# -------------------------
# 4️⃣ 创建词云
# -------------------------
wc = WordCloud(
    width=800,
    height=800,
    background_color="white",
    mask=mask_image,
    contour_width=1,
    contour_color="red",
    max_words=100,
    prefer_horizontal=1.0  # 全部文字水平
)

wc.generate_from_frequencies(frequencies)
wc.recolor(color_func=random_color)  # 应用随机颜色

# -------------------------
# 5️⃣ 显示词云
# -------------------------
plt.figure(figsize=(8, 8))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()

# -------------------------
# 6️⃣ 保存为图片
# -------------------------
wc.to_file("heart_wordcloud.png")
