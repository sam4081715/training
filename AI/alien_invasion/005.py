class Group():
    def __init__(self):
        self.sprites = []
    def add(self, sprite):
        self.sprites.append(sprite)
    def update(self):
        for sprite in self.sprites:
            sprite.update()
    def remove(self, sprite):
        self.sprites.remove(sprite)
        
    def draw(self, surface)
        for sprite in self.sprites:
            surface.blit(sprite.image, sprite.rect)
        
        
