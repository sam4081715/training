import pygame
from time import sleep

class Ammo():
    def __init__(self, bullet_amount = 5, bullet_max = 5, reload_time = 1000):
        # 彈夾數量
        self.bullet_amount = bullet_amount
        # 彈夾上限
        self.bullet_max = bullet_max
        # 裝填時間
        self.reload_time = reload_time
        # 計算delay_time使用之時間參數
        self.tmp1_time = 0
        self.tmp2_time = 0
        self.sum_time = 0
    
    def update(self, sb):
        # 在update開頭抓取時間，表示當前時間
        self.tmp1_time = pygame.time.get_ticks()
        if self.bullet_amount < self.bullet_max:
            # 這次迴圈跟上一次迴圈的間隔
            delay_time = self.tmp1_time - self.tmp2_time
            # 累計時間
            self.sum_time += delay_time
            # 當累計時間大於裝填時間
            if self.sum_time >= self.reload_time:
                # 彈夾數量加一
                self.bullet_amount += 1
                # 更新彈夾子彈的圖像
                sb.prep_ammo()
                # 累計時間歸零
                self.sum_time = 0
        elif self.bullet_amount == self.bullet_max:
            # 累計時間歸零
            self.sum_time = 0
        # 在update結尾抓取時間，表示上一次迴圈的時間
        self.tmp2_time = pygame.time.get_ticks()
            
            
# pygame.init()
# clock = pygame.time.Clock()
# ammo = Ammo(bullet_max=5, bullet_amount=1)
# for i in range(150):
#     ammo.update()
#     print(ammo.bullet_amount)
#     clock.tick(50)
    
    

