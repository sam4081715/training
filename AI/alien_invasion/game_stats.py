class GameStats():
    def __init__(self, ai_settings):
        # 遊戲是否運行
        self.game_active = False
        # 讀取遊戲設置
        self.ai_settings = ai_settings
        # 設置最高分數
        self.highest_score = 0
        # 執行重置數據
        self.reset_stats()

    
    def reset_stats(self):
        # 將飛船的殘機數設定為上限
        self.ships_left = self.ai_settings.ship_limit
        # 設定分數
        self.score = 0
        # 設定等級
        self.level = 1