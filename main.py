
import pygame
import os

# 1. Pygame'i Başlatma
pygame.init()

# 2. Ekran Ayarları
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Zıplama Eklendi - Mario Tarzı")

# 3. Renkler
white = (255, 255, 255)
red = (255, 0, 0)
blue = (135, 206, 250) # Gökyüzü mavisi

# 4. Oyuncu Görselini Yükleme
try:
    player_image_filename = "assets/characters/hero.png"
    player_image = pygame.image.load(player_image_filename).convert_alpha()
    map_image_filename = "assets/maps/map-forrest.png"
    map_image = pygame.image.load(map_image_filename).convert_alpha()
except pygame.error as e:
    print(f"Oyuncu görseli yüklenemedi: {player_image_filename} - Hata: {e}")
    print(f"Map görseli yüklenemedi: {map_image_filename} - Hata: {e}")
    pygame.quit()
    exit()

# 5. Oyuncu Ayarları ve Fizik Değişkenleri
player_rect = player_image.get_rect()
map_rect = map_image.get_rect()

# Fizik/Hareket Değişkenleri
player_speed = 5        # Yatay hız
player_y_velocity = 0   # Dikey hız (başlangıçta 0)
gravity = 0.8           # Yerçekimi ivmesi (arttıkça daha hızlı düşer)
jump_height = -18       # Zıplama kuvveti (negatif çünkü y yukarı doğru azalır)
is_on_ground = True     # Oyuncu yerde mi?
ground_level = screen_height - 50 # Zeminin y koordinatı (görselin altı bu seviyede olacak)

# Başlangıç pozisyonunu ayarla (tam zeminde)
player_rect.bottom = ground_level


# 6. Oyun Döngüsü
running = True
clock = pygame.time.Clock() # FPS kontrolü için Clock nesnesi

while running:
    # 7. Olayları (Events) Kontrol Etme
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Zıplama Kontrolü (Sadece tuşa BASILDIĞI AN tetiklenir)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and is_on_ground: # Boşluk tuşu VE yerdeyse
                player_y_velocity = jump_height
                is_on_ground = False # Zıplayınca yerden kalkar

    # 8. Klavye Girdilerini Kontrol Etme (Yatay Hareket - Basılı tutulduğu sürece)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.right < screen_width:
        player_rect.x += player_speed

    # 9. Fizik Güncellemeleri (Her karede çalışır)
    # Yerçekimini uygula
    player_y_velocity += gravity
    # Dikey hıza göre konumu güncelle
    player_rect.y += player_y_velocity

    # Zemin Kontrolü / Yere İniş
    if player_rect.bottom >= ground_level:
        player_rect.bottom = ground_level # Tam zemine oturt
        player_y_velocity = 0           # Dikey hızı sıfırla
        is_on_ground = True             # Artık yerde

    # --- Oyun Mantığı Güncellemeleri Bitti ---

    # 10. Ekranı Çizme
    screen.fill(blue)

    
    #image resize yapılcak width height hatalı
    screen.blit(map_image, map_rect) 
    
    screen.blit(player_image, player_rect)
    # 11. Ekranı Güncelleme
    pygame.display.flip()

    # FPS (Kare Hızı) Sınırlaması
    clock.tick(60) # Saniyede 60 kare

# 12. Pygame'den Çıkış
pygame.quit()