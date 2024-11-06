import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_events(ship, screen, ai_settings, bullets, button, stats, ammo, aliens, sb, laser):
    # 抓取所有輸入
    for event in pygame.event.get():
        # 偵測到離開按鈕
        if event.type == pygame.QUIT:
            # 關閉視窗
            sys.exit()
            break
        # 偵測到有按下鍵盤按鈕
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, ship, screen, ai_settings, bullets, ammo, laser, sb)
        # 偵測到有鬆開鍵盤按鈕
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship, laser)
        # 偵測滑鼠按鍵有沒有按下
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 擷取鼠標的位置
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # 確認鼠標與按鈕的重疊
            check_play_button(button, mouse_x, mouse_y, stats, aliens, bullets, ship, screen, ai_settings, sb)

                
def check_play_button(button, mouse_x, mouse_y, stats, aliens, bullets, ship, screen, ai_settings, sb):
    # 確認鼠標與按鈕的重疊
    button_clicked = button.rect.collidepoint(mouse_x, mouse_y)
    # 若按鈕按下且遊戲暫停
    if button_clicked and not stats.game_active:
        # 重置速度設定
        ai_settings.init_dynamic_settings()
        # 將鼠標設定成不可見
        pygame.mouse.set_visible(False)
        # 重置遊戲數據:殘機數
        stats.reset_stats()
        # 產生記分板、等級、殘機數圖像
        sb.prep_score()
        sb.prep_level()
        sb.prep_ships()
        # 讓遊戲開始運行
        stats.game_active = True
        # 清空外星人、子彈群組
        aliens.empty()
        bullets.empty()
        # 重置飛船位置
        ship.reset_ship()
        # 產生新的外星人艦隊
        create_fleet(screen, ai_settings, aliens, ship)
        
def check_key_down_events(event, ship, screen, ai_settings, bullets, ammo, laser, sb):
    # 偵測到按下右方向鍵
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    # 偵測到按下左方向鍵
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    # 偵測到按下上方向鍵
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    # 偵測到按下下方向鍵
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    # 偵測到按下開火鍵(z)
    elif event.key == pygame.K_z:
        # 子彈開火
        fire_bullet(bullets, ai_settings, screen, ship, ammo, sb)
    # 按下x
    elif event.key ==pygame.K_x:
        # 雷射打開
        laser.laser_on = True
        
def fire_bullet(bullets, ai_settings, screen, ship, ammo, sb):
    # 判斷子彈數量是否達到上限
    if ammo.bullet_amount > 0:
        # 產生一個子彈的物件
        new_bullet = Bullet(screen, ship, ai_settings)
        # 將彈夾子彈數量減一
        ammo.bullet_amount -=1
        # 更新彈夾子彈的圖像
        sb.prep_ammo()
        # 將新產生的子彈放入子彈群組
        bullets.add(new_bullet)

def check_key_up_events(event, ship, laser):
    # 偵測到鬆開右方向鍵
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    # 偵測到鬆開左方向鍵
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    # 偵測到鬆開上方向鍵
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    # 偵測到鬆開下方向鍵
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    # 放開x
    elif event.key == pygame.K_x:
        # 雷射關閉
        laser.laser_on = False

def update_screen(screen, ai_settings, ship, bullets, aliens, stats, button, sb, laser):
    # 將視窗填滿背景色
    screen.fill(ai_settings.bg_color)
    # 繪製飛船
    ship.blitme()
    # 跑迴圈遍歷子彈群組裡的所有物件
    for bullet in bullets:
        # 繪出子彈
        bullet.draw_bullet()
    # 繪出雷射
    laser.draw_laser()
    # 在視窗上繪製整群外星人
    aliens.draw(screen)
    # 檢查遊戲是否暫停
    if not stats.game_active:
        # 畫出按鈕
        button.draw_button()
    # 繪製記分板
    sb.show_score()
    # 更新視窗畫面
    pygame.display.flip()
    
# 更新子彈群組
def update_bullets(bullets, aliens, screen, ai_settings, ship, stats, sb):
    # 更新子彈群組中所有物件的位置
    bullets.update()
    # 檢查碰撞
    check_bullets_aliens_collisions(bullets, aliens, screen, ai_settings, ship, stats, sb)
    # 產生子彈群組的複本，然後遍歷複本中的所有元素
    for bullet in bullets.copy():
        # 當子彈的底部超出視窗上方時
        if bullet.rect.bottom <= 0:
            # 從子彈群組移出該子彈
            bullets.remove(bullet)
            
def update_laser(laser, aliens, stats, ai_settings, sb):
    # 更新雷射的位置及高度
    laser.update()
    # 處理雷射群組與外星人群組的碰撞
    collision_list = pygame.sprite.spritecollide(laser, aliens, True)
    if collision_list:
        # 將得分加上外星人點數乘以外星人數量
        stats.score += ai_settings.alien_point*len(collision_list)
        # 將分數繪製成圖像
        sb.prep_score()
        # 確認最高分數的更新
        update_highet_score(stats, sb)

def check_bullets_aliens_collisions(bullets, aliens, screen, ai_settings, ship, stats, sb):
    # 處理子彈群組與外星人群組的碰撞，兩個True表示子彈碰上外星人時兩者都會消滅
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
    # 確認字典collisions裡面有沒有東西
    if collisions:
        # 遍歷不同子彈碰到的外星人群組
        for aliens_b in collisions.values():
            # 將得分加上外星人點數乘以外星人數量
            stats.score += ai_settings.alien_point*len(aliens_b)
        # 將分數繪製成圖像
        sb.prep_score()
        # 確認最高分數的更新
        update_highet_score(stats, sb)
    # 確認外星人的數量是否為0
    if len(aliens) == 0:
        # 增加速度(難度)
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        # 清空視窗上的子彈
        bullets.empty()
        # 產生新的外星人艦隊
        create_fleet(screen, ai_settings, aliens, ship)
        
def update_highet_score(stats, sb):
    # 判斷當前分數有無大於最高分數
    if stats.score > stats.highest_score:
        # 更新最高分數
        stats.highest_score = stats.score
        # 更新最高分數的圖像
        sb.prep_highest_score()
            
def update_aliens(aliens, ai_settings, ship, stats, screen, bullets, sb):
    # 確認外星人群組有沒有碰到視窗邊界
    check_fleet_edge(aliens, ai_settings)
    # 透過Group.update()來更新所有外星人的位置
    aliens.update()
    # 確認飛船有無與任何外星人碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        # 處理飛船被碰到後要做的事
        ship_hitted(stats, screen, ai_settings, aliens, ship, bullets, sb)
    # 處理外星人碰到視窗底部
    check_aliens_bottom(screen, aliens, stats, ai_settings, ship, bullets, sb)

def check_aliens_bottom(screen, aliens, stats, ai_settings, ship, bullets, sb):
    # 抓取視窗之長方形
    screen_rect = screen.get_rect()
    # 遍歷外星人群組中的所有外星人
    for alien in aliens.sprites():
        # 確認外星人的底部有無超出視窗底部
        if alien.rect.bottom >= screen_rect.bottom:
            # 若有就像飛船被外星人碰到一樣處理
            ship_hitted(stats, screen, ai_settings, aliens, ship, bullets, sb)
            # 跳出迴圈
            break

def ship_hitted(stats, screen, ai_settings, aliens, ship, bullets, sb):
    # 確認殘機數是否大於零
    if stats.ships_left > 0:
        # 殘機數減一
        stats.ships_left -= 1
        # 更新殘機數的圖像
        sb.prep_ships()
        # 清空外星人、子彈群組
        aliens.empty()
        bullets.empty()
        # 重置飛船位置
        ship.reset_ship()
        # 產生新的外星人艦隊
        create_fleet(screen, ai_settings, aliens, ship)
        # 時間暫停05秒
        sleep(0.5)
    else:
        # 將遊戲暫停
        stats.game_active = False
        # 將鼠標設定成可見
        pygame.mouse.set_visible(True)
    
def check_fleet_edge(aliens, ai_settings):
    # 遍歷aliens底下的所有alien
    for alien in aliens.sprites():
        # alien會確認自己有無碰到邊界
        if alien.check_edge():
            # 改變外星人群組的方向並下落一段距離
            change_alien_direction_drop(aliens, ai_settings)
            break
        
def change_alien_direction_drop(aliens, ai_settings):
    # 遍歷aliens底下的所有alien
    for alien in aliens.sprites():
        # 外星人往下落一個drop_speed
        alien.rect.y += ai_settings.alien_drop_speed
    # 改變設置內的外星人方向
    ai_settings.alien_direction *= -1
            
def create_fleet(screen, ai_settings, aliens, ship):
    # 計算一排外星人的數量
    number_alien_x = get_number_alien_x(screen, ai_settings)
    # 計算外星人排數
    number_rows = get_number_rows(screen, ai_settings, ship)
    # 跑for迴圈產生多排外星人
    for row_number in range(number_rows):
        # 跑for迴圈產生一排外星人
        for alien_number in range(number_alien_x):
            # 依據alien_number產生外星人並加入外星人群組
            create_alien(screen, ai_settings, alien_number, row_number, aliens)
        
def get_number_alien_x(screen, ai_settings):
    # 產生外星人實例，並抓取外星人寬度。
    alien = Alien(screen, ai_settings)
    alien_width = alien.rect.width
    # 將視窗的寬度左邊減去一個外星人寬度，右邊也減去外星人寬度，剩下可以擺放外星人的空間
    avaliable_space_x = ai_settings.screen_width - 2*alien_width
    # 計算一排外星人的數量
    number_alien_x = int(avaliable_space_x / (2*alien_width))
    return number_alien_x

def get_number_rows(screen, ai_settings, ship):
    # 產生外星人實例並抓取其高度
    alien = Alien(screen, ai_settings)
    alien_height = alien.rect.height
    # 計算垂直方向可以使用的空間
    avalible_space_y = ai_settings.screen_height - ship.rect.height - (3*alien_height)
    # 計算垂直方向可以允許的外星人排數
    number_rows = int(avalible_space_y / (2*alien_height))
    return number_rows

def create_alien(screen, ai_settings, alien_number, row_number, aliens):
    # 產生外星人實例，並抓取外星人寬度、高度。
    alien = Alien(screen, ai_settings)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    # 安排外星人位置
    alien.x = alien_width + alien_number*(2*alien_width)
    alien.rect.x = alien.x
    alien.rect.y = alien_height + row_number*(2*alien_height)
    # 將外星人加入外星人群組
    aliens.add(alien)
    

    
    
    
    
    
        
    
            

    
    
    
