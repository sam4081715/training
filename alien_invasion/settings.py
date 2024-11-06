class Settings():
    def __init__(self):
        # 視窗寬度
        self.screen_width = 1200
        # 視窗高度
        self.screen_height = 720
        # 視窗顏色
        self.bg_color = (230, 230, 230)
        # 殘機數上限
        self.ship_limit = 3
        # 子彈寬度
        self.bullet_width = 3
        # 子彈高度
        self.bullet_height = 15
        # 子彈顏色
        self.bullet_color = (60, 60, 60)
        # 彈夾上限
        self.bullets_allowed = 5
        # 雷射砲的寬度
        self.laser_width = 5
        # 外星人落下速度
        self.alien_drop_speed = 10
        # 外星人的方向
        self.alien_direction = 1
        # 重新裝填時間
        self.reload_time = 300
        # 加速設定
        self.speedup_factor = 1.1
        # 初始化速度設定
        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        # 飛船速度
        self.ship_speed_factor = 1.2
        # 外星人速度設定
        self.alien_speed_factor = 1
        # 子彈速度
        self.bullet_speed_factor = 2
        # 外星人分數
        self.alien_point = 50
        
    def increase_speed(self):
        # 飛船加速
        self.ship_speed_factor *= self.speedup_factor
        # 外星人加速
        self.alien_speed_factor *= self.speedup_factor
        # 子彈加速
        self.bullet_speed_factor *= self.speedup_factor
        # 增加外星人點數
        self.alien_point = int(self.alien_point*self.speedup_factor)
    

        
    
        