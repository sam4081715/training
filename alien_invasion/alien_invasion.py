import pygame
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf
from pygame.sprite import Group
from ammo import Ammo
from laser import Laser


def run_game():
    # pygame模組初始化
    pygame.init()
    # 實例化Settings
    ai_settings = Settings()
    # 產生視窗，解析度1200*720
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # 產生飛船的實例
    ship = Ship(screen, ai_settings)
    # 建立外星人群組
    aliens = Group()
    # 建立按鈕實例
    play_button = Button(screen, "Play")
    # 建立彈夾實例
    ammo = Ammo(ai_settings.bullets_allowed, ai_settings.bullets_allowed, ai_settings.reload_time)
    # 產生遊戲數據的實例
    stats = GameStats(ai_settings)
    # 產生記分板的實例
    sb = Scoreboard(screen, stats, ai_settings, ammo)
    # 創建外星人艦隊
    gf.create_fleet(screen, ai_settings, aliens, ship)
    # 新創一個子彈群組
    bullets = Group()
    # 建立雷射實例
    laser = Laser(screen, ship, ai_settings)
    # 設定視窗的標題
    pygame.display.set_caption("Alien_Invasion")
    # 主迴圈
    while True:
        # 監控所有輸入
        gf.check_events(ship, screen, ai_settings, bullets, play_button, stats, ammo, aliens, sb, laser)
        # 遊戲是否運行
        if stats.game_active:
            # 更新飛船的位置
            ship.update()
            # 隨時間更新子彈數量
            ammo.update(sb)
            # 更新雷射及處理碰撞
            gf.update_laser(laser, aliens, stats, ai_settings, sb)
            # 更新子彈群組
            gf.update_bullets(bullets, aliens, screen, ai_settings, ship, stats, sb)
            # 更新外星人群組
            gf.update_aliens(aliens, ai_settings, ship, stats, screen, bullets, sb)
        # 更新視窗
        gf.update_screen(screen, ai_settings, ship, bullets, aliens, stats, play_button, sb, laser)
# 運行主要功能
run_game()
    