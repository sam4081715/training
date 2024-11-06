import pygame.font
from pygame.sprite import Group
from ship import Ship
from bullet import Bullet

class Scoreboard():
    def __init__(self, screen, stats, ai_settings, ammo):
        # 讀取視窗
        self.screen = screen
        # 抓取視窗的長方形
        self.screen_rect = screen.get_rect()
        # 讀取遊戲數據
        self.stats = stats
        self.ammo = ammo
        # 讀取遊戲設置
        self.ai_settings = ai_settings
        # 設定分數的文字顏色
        self.text_color = (30, 30, 30)
        # 設定字體大小
        self.font = pygame.font.SysFont(None, 48)
        # 產生分數、最高分、難度等級、殘機數的圖像
        self.prep_score()
        self.prep_highest_score()
        self.prep_level()
        self.prep_ships()
        self.prep_ammo()
        
    def prep_score(self):
        # 將分數取整到第十位，轉成整數避免小數點
        rounded_score = int(round(self.stats.score, -1))
        # 將取整後的分數透過format功能轉成格式化的字串
        score_str = "{:,}".format(rounded_score)
        # 將分數渲染成圖像，長方形的顏色設定成背景顏色
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        # 從分數圖像抓取長方形
        self.score_rect = self.score_image.get_rect()
        # 將分數長方形的右側設定在視窗右側減20
        self.score_rect.right = self.screen_rect.right - 20
        # 將分數長方形的頂端設定在視窗頂端加20
        self.score_rect.top = 20
    
    def prep_highest_score(self):
        # 將最高分取整到第十位，轉成整數避免小數點
        rounded_highest_score = int(round(self.stats.highest_score, -1))
        # 將取整後的最高分透過format功能轉成格式化的字串
        highest_score_str = "{:,}".format(rounded_highest_score)
        # 將最高分渲染成圖像，長方形的顏色設定成背景顏色
        self.highest_score_image = self.font.render(highest_score_str, True, self.text_color, self.ai_settings.bg_color)
        # 從最高分圖像抓取長方形
        self.highest_score_rect = self.highest_score_image.get_rect()
        # 將最高分長方形的右側設定在視窗右側減20
        self.highest_score_rect.right = self.screen_rect.right - 20
        # 將最高分長方形的頂端設定在視窗頂端加20再加上分數長方形的高度
        self.highest_score_rect.top = 20 + self.score_rect.height
        
    def prep_level(self):
        # 設定等級的字串
        level_str = "level "+ str(self.stats.level)
        # 將等級渲染成圖像
        self.level_image = self.font.render(level_str, True, self.text_color, self.ai_settings.bg_color)
        # 抓取等級圖像的長方形
        self.level_rect = self.level_image.get_rect()
        # 將等級長方形放置在視窗水平中間
        self.level_rect.centerx = self.screen_rect.centerx
        # 將等級長方形放置在視窗頂部加20
        self.level_rect.top = 20
        
    def prep_ships(self):
        # 建立飛船群組
        self.ships = Group()
        # 根據殘機數的數量跑for迴圈
        for ship_number in range(self.stats.ships_left):
            # 建立飛船的實例
            ship = Ship(self.screen, self.ai_settings)
            # 將飛船的座標放在左上角，同時根據第幾個飛船，再往右位移飛船寬度
            ship.rect.x = 10 + ship_number*ship.rect.width
            ship.rect.y = 10
            # 將飛船實例放入飛船群組
            self.ships.add(ship)
            
    def prep_ammo(self):
        # 產生彈夾子彈的空集合
        self.bullet_ammo = []
        # 跑for迴圈，次數為彈夾子彈數量
        for bullet_number in range(self.ammo.bullet_amount):
            # 產生長方形物件作為子彈
            bullet = pygame.Rect(0, 0, self.ai_settings.bullet_width, self.ai_settings.bullet_height)
            # 將子彈的座標設定在左下角，且水平方向間隔為2
            bullet.x = 10 + bullet_number*(bullet.width + 2)
            bullet.bottom = self.screen_rect.bottom - 10
            # 將子彈加入彈夾子彈的集合
            self.bullet_ammo.append(bullet)
        

    def show_score(self):
        # 在視窗上根據分數長方形的位置繪製分數圖像
        self.screen.blit(self.score_image, self.score_rect)
        # 在視窗上根據最高分長方形的位置繪製最高分圖像
        self.screen.blit(self.highest_score_image, self.highest_score_rect)
        # 再視窗上繪製等級圖像
        self.screen.blit(self.level_image, self.level_rect)
        # Group.draw()來在視窗上繪置群組中所有的精靈圖
        self.ships.draw(self.screen)
        # 跑for迴圈，繪出彈夾子彈集合底下的所有子彈
        for bullet in self.bullet_ammo:
            pygame.draw.rect(self.screen, self.ai_settings.bullet_color, bullet)
        
        
        
        
    