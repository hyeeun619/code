import matplotlib.pyplot as plt
from matplotlib import font_manager

# Matplotlib
# 폰트 경로
path = "Pretendard-Medium.ttf"

font = font_manager.FontProperties(fname=path).get_name()
plt.rc("font", family=font)



# 기본사용법
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title("맷플롯립")

plt.show()
