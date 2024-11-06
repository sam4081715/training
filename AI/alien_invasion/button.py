import pygame.font

class Button():
    def __init__(self, screen, msg):
        # 讀取視窗
        self.screen = screen
        # 讀取視窗長方形
        self.screen_rect = screen.get_rect()
        # 設定按鈕的長、寬
        self.width, self.height = 200, 50
        # 設定按鈕顏色
        self.button_color = (0, 255, 0)
        # 設定文字顏色
        self.text_color = (255, 255, 255)
        # 呼叫字形物件
        self.font = pygame.font.SysFont(None, 48)
        # 呼叫長方形物件，長寬是由前面定義
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # 將長方形的中心點置於視窗中心點
        self.rect.center = self.screen_rect.center
        # 將文字渲染成圖
        self.prep_msg(msg)
        
    def prep_msg(self, msg):
        # 呼叫SysFont.render來將msg轉化成圖片物件(Surface)
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        # 抓取文字圖片的長方形
        self.msg_rect = self.msg_image.get_rect()
        # 將文字圖片的中心點置於視窗的中心點
        self.msg_rect.center = self.screen_rect.center
        
    def draw_button(self):
        # 將長方形塗滿顏色作為按鈕畫出
        self.screen.fill(self.button_color, self.rect)
        # 將文字圖片畫出
        self.screen.blit(self.msg_image, self.msg_rect)
        
    
        
        