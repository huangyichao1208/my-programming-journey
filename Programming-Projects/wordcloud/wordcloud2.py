from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import random

# -------------------------
# 1️⃣ 定义更丰富的词频字典 (根据右侧图片的风格进行扩展)
# -------------------------
frequencies = {
    "all the rage": 30, # 最大的词
    "polular": 25, # 第二大的词 (注意: 如果是想写 "popular", 请更正)
    "take a peek at": 20,
    "catch up with my friends": 18,
    "share life updates": 15,
    "start with": 12,
    "give or take": 10,
    "stay in the loop": 10,
    "share silly jokes": 8,
    "connect/ reconnect with people": 7,
    "trending/ on trend": 7,
    "become interested in": 6,
    "social media user": 6,
    "get into sth.": 5,
    "keep in touch with my friends": 5,
    "post random things": 5,
    "online community": 4, # 添加一些新词来填充
    "digital trends": 4,
    "viral content": 3,
    "current events": 3
}

# -------------------------
# 2️⃣ 移除心形 mask，创建简单的矩形 mask（如果需要的话，或者直接不使用mask）
#    如果想要更自由的布局，可以完全移除mask参数。
#    这里我移除了 mask，让词云自动填充。
# -------------------------
# mask_image = None # 不使用mask

# -------------------------
# 3️⃣ 自定义颜色函数，使用更鲜明的蓝色和粉色系
# -------------------------
def vibrant_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    # 定义几种鲜明的蓝色和粉色系的HSL值
    blue_hues = [200, 210, 220] # 蓝色系
    pink_hues = [330, 340, 350] # 粉色系

    # 随机选择一个色系
    if random.random() > 0.5: # 大约一半的词是蓝色，一半是粉色
        h = random.choice(blue_hues)
    else:
        h = random.choice(pink_hues)

    s = random.randint(80, 100) # 保持高饱和度
    l = random.randint(40, 70)  # 适中的亮度
    return f"hsl({h}, {s}%, {l}%)"

# -------------------------
# 4️⃣ 创建词云 (移除 mask 和 contour 相关参数)
# -------------------------
wc = WordCloud(
    width=1000,  # 可以适当增大尺寸，以容纳更多词
    height=600,  # 调整宽高比
    background_color="white",
    # mask=mask_image, # 不使用mask，让词云填充整个区域
    # contour_width=0, # 不使用轮廓
    # contour_color="red", # 不使用轮廓
    max_words=len(frequencies), # 尝试显示所有词
    prefer_horizontal=0.9, # 允许少量非水平词，增加紧凑感
    min_font_size=10, # 设置最小字体大小，防止太小的词不显示
    relative_scaling=0.7 # 调整词的大小相对缩放比例，可以使大小差异更明显
)

wc.generate_from_frequencies(frequencies)
wc.recolor(color_func=vibrant_color_func)  # 应用新的颜色函数

# -------------------------
# 5️⃣ 显示词云
# -------------------------
plt.figure(figsize=(10, 6)) # 调整显示尺寸以匹配生成尺寸
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()

# -------------------------
# 6️⃣ 保存为图片
# -------------------------
wc.to_file("vibrant_wordcloud.png")