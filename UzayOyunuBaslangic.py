import pygame
import os.path
import random
import sys
import PowerUp, Fuze, Patlama, CanCiz, Kalkan, Ulti, GameOver

pygame.init()

# Temel ayarlar
width = 1024
height = 600
boyut = (width, height)

# Klasörler
klasor = os.path.dirname(__file__)
resimKlasoru = os.path.join(klasor, "resimler")
sesKlasoru = os.path.join(klasor, "sesler")

# Patlama Klasörü

patlamaKlasoru = os.path.join(klasor, "patlama")
patlamaResimleri = ["patlama.png"]
for i in range(1, 8):
    patlamaResimleri.append("{}.png".format(i))

####################


#####Guclendirici Resimleri#############333


powerUps = ["can.png", "guclendirme.png", "guclendirme.png", "guclendirme.png", "guclendirme.png", "kalkan.png",
            "kalkan.png", "kalkan.png", "kalkan.png", "kalkan.png", "kalkan.png",
            "deguclendirme.png", "deguclendirme.png", "deguclendirme.png", "deguclendirme.png", "deguclendirme.png", ]
# Resimler
background = pygame.image.load(os.path.join(resimKlasoru, "farback.gif"))
background2 = pygame.image.load(os.path.join(resimKlasoru, "bg2.png"))
background3 = pygame.image.load(os.path.join(resimKlasoru, "bg3.png"))
fire = pygame.image.load(os.path.join(resimKlasoru, "laser.png"))
ship = pygame.image.load(os.path.join(resimKlasoru, "ufo.png"))
ship2 = pygame.image.load(os.path.join(resimKlasoru, "ufo2.png"))
ship3 = pygame.image.load(os.path.join(resimKlasoru, "ufo3.png"))
ship4 = pygame.image.load(os.path.join(resimKlasoru, "ufo4.png"))
patlama = pygame.mixer.music.load(os.path.join(sesKlasoru, "patlama_efekti.mp3"))

# Pencere ayarı
pencere = pygame.display.set_mode(boyut)
pygame.display.set_icon(ship)
pygame.display.set_caption('Space Shooter')

###### EFEKTLER################
hitEffect = pygame.mixer.Sound(os.path.join(sesKlasoru, "laser1.ogg"))
fireEffect = pygame.mixer.Sound(os.path.join(sesKlasoru, "fire.ogg"))
speedGain = pygame.mixer.Sound(os.path.join(sesKlasoru, "powerUp.ogg"))
liveGain = pygame.mixer.Sound(os.path.join(sesKlasoru, "powerUp.ogg"))
timeGain = pygame.mixer.Sound(os.path.join(sesKlasoru, "powerUp.ogg"))
deBuff = pygame.mixer.Sound(os.path.join(sesKlasoru, "debuff.wav"))
carpmaEfekt = pygame.mixer.Sound(os.path.join(sesKlasoru, "efekt.wav"))
##########################

asteroidler = ["meteor1.png", "meteor2.png", "meteor3.png", "meteor4.png",
               "meteor1.png", "meteor2.png", "meteor3.png", "meteor4.png",
               "meteor1.png", "meteor2.png", "meteor3.png", "meteor4.png",
               "meteor1.png", "meteor2.png", "meteor3.png", "meteor4.png",
               "meteorGreen.png", "meteorGreen.png"]

# mouse nin gözüküp gözükmeyeceği
pygame.mouse.set_visible(False)

font = pygame.font.SysFont("Helvetica", 50)

clock = pygame.time.Clock()


class Parca(pygame.sprite.Sprite):
    def __init__(self, y=height / 2):
        super().__init__()
        self.image = ship.convert()  # Parçanın genişliği
        self.can = 3
        self.image.set_colorkey((0, 0, 0))
        # self.image.fill((0, 130, 255))
        self.rect = self.image.get_rect()
        self.radius = 44  # ayarla
        # pygame.draw.circle(self.image, (255, 0, 0), self.rect.center, self.radius)
        self.rect.x = 0
        self.rect.y = y
        self.kalkan = 100
        self.mermiDelay = 250
        self.sonAtes = pygame.time.get_ticks()
        self.hider_timer = 1500
        self.isHide = False
        self.lastHide = pygame.time.get_ticks()
        self.boostStart = 0

    def changeBulletSpeed(self, speed):
        self.mermiDelay = speed
        self.boostStart = pygame.time.get_ticks()

    def hide(self):
        self.isHide = True
        self.lastHide = pygame.time.get_ticks()
        self.rect.center = (-200, height / 2)

    def update(self, *args):
        up, down, right, left, shoot = args

        if self.isHide and pygame.time.get_ticks() - self.lastHide > self.hider_timer:
            self.isHide = False
            self.rect.x = 0
            self.rect.y = height / 2

        if level == 5:
            self.image = ship2.convert()
            self.image.set_colorkey((0, 0, 0))
        elif level == 10:
            self.image = ship3.convert()
            self.image.set_colorkey((0, 0, 0))
        elif level == 15:
            self.image = ship4.convert()
            self.image.set_colorkey((0, 0, 0))

        ##Güçlendirme saniye kontrol
        if pygame.time.get_ticks() - self.boostStart > 3000:
            self.changeBulletSpeed(250)

        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y + self.rect.size[1] > height:
            self.rect.y = height - self.rect.size[1]

            # KLAVYE algılama
        if up:
            self.rect.y -= 10
        if down:
            self.rect.y += 10
        if shoot:
            self.shoot()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.sonAtes > self.mermiDelay:
            self.sonAtes = now
            fireEffect.play()
            fuze = Fuze.Fuze(self.rect.y + 22)
            all_sprites.add(fuze)
            fuzeler.add(fuze)
            if level > 5:
                fuze2 = Fuze.Fuze(self.rect.y - 22)
                all_sprites.add(fuze2)
                fuzeler.add(fuze2)


class Mermi(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.secim = random.choice(asteroidler)
        asteroid = pygame.image.load(os.path.join(resimKlasoru, self.secim))
        self.image = asteroid.convert()
        self.orijinal_resim = self.image
        self.image.set_colorkey((0, 0, 0))
        # self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.radius = int((self.rect.width * 0.70) / 2)
        # pygame.draw.circle(self.image, (255, 0, 0), self.rect.center, self.radius)

        self.rect.y = random.randrange(height - self.rect.height)
        self.rect.x = random.randrange(width + 40, width + 100)
        self.speedx = random.randrange(4, 8)
        self.speedy = random.randrange(-2, 2)

        self.rot = 0
        self.rotateSpeed = random.randrange(-20, 20)
        self.lastUpdate = pygame.time.get_ticks()

    # Dönme efekti
    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.lastUpdate > 50:
            self.lastUpdate = now
            self.rot = (self.rot + self.rotateSpeed) % 360
            new_image = pygame.transform.rotate(self.orijinal_resim, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self, *args):
        self.rotate()
        self.rect.x -= self.speedx
        self.rect.y += self.speedy

        if self.rect.right < 0:
            self.rect.y = random.randrange(height - self.rect.height)
            self.rect.x = random.randrange(width + 40, width + 100)
            self.speedx = random.randrange(3, 10)
            self.speedy = random.randrange(-2, 2)
            global score
            score += 1


# Ateş etme bitiş
sayacSifirlama = True

#################################
game_over = True

while True:
    if game_over:
        level = 0
        skor = 0
        pygame.mixer.music.load(os.path.join(sesKlasoru, "Blue_Space.mp3"))
        pygame.mixer.music.play()
        GameOver.show_gameover_screen()
        game_over = False
        # Gruplar

        mermiler = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()
        fuzeler = pygame.sprite.Group()
        powerGains = pygame.sprite.Group()

        # Mermi sayısı
        for i in range(5):
            mermi = Mermi()
            all_sprites.add(mermi)
            mermiler.add(mermi)

        # Nesne ekleme
        parca1 = Parca()
        all_sprites.add(parca1)
        score = 0

    mermiSayisi = len(mermiler)
    keys = pygame.key.get_pressed()
    pencere.fill((255, 255, 255))  # Arkaplan rengi
    pencere.blit(background, background.get_rect())
    if level > 9:
        pencere.blit(background2, background2.get_rect())
    if level > 19:
        pencere.blit(background3, background3.get_rect())
    all_sprites.draw(pencere)

    clock.tick(60)  # FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    up, down, right, left, shoot = keys[pygame.K_UP], keys[pygame.K_DOWN], keys[pygame.K_RIGHT], keys[pygame.K_LEFT], \
                                   keys[pygame.K_SPACE]
    all_sprites.update(up, down, right, left, shoot)

    # EKRANA SKOR YAZDIRMA
    fontScore = font.render("Kalan Asteroid: {}".format(mermiSayisi), 1, (255, 127, 0))
    pencere.blit(fontScore, (width - fontScore.get_size()[0], 0))

    fontScore2 = font.render("Skor: {}".format(skor), 1, (255, 255, 0))
    pencere.blit(fontScore2, (height - fontScore.get_size()[0], 0))

    # Grupların çarpışmasını denetleme (MERMİLER İLE ASTROİD ÇARPIŞMASI)
    isHit = pygame.sprite.groupcollide(fuzeler, mermiler, True, True)
    if isHit:
        skor += 1
        if Ulti.ulti + 1 < 100:
            Ulti.ulti += 1
        else:
            Ulti.ulti = 100
        hitEffect.play()
        for meteorlar in isHit.values():
            for meteor in meteorlar:
                kaboom = Patlama.Patlama(meteor, patlamaKlasoru, patlamaResimleri)
                all_sprites.add(kaboom)

                if random.random() > 0.90:
                    powerGain = PowerUp.PowerUp(meteor.rect.center)
                    powerGains.add(powerGain)
                    all_sprites.add(powerGain)
                if meteor.secim == "meteorGreen.png":
                    if parca1.kalkan + 10 < 100:
                        parca1.kalkan += 10
                    else:
                        parca1.kalkan = 100

    isPowerGain = pygame.sprite.spritecollide(parca1, powerGains, True)

    if isPowerGain:
        for powerType in isPowerGain:
            if powerType.choice == "guclendirme.png":
                speedGain.play()
                parca1.changeBulletSpeed(130)
            elif powerType.choice == "kalkan.png":
                timeGain.play()
                parca1.kalkan = 100
            elif powerType.choice == "deguclendirme.png":
                deBuff.play()
                parca1.changeBulletSpeed(555)
            else:
                liveGain.play()
                parca1.can += 1

    # Çarpma işlemi
    durum = pygame.sprite.spritecollide(parca1, mermiler, True, collided=pygame.sprite.collide_circle)
    if durum:
        carpmaEfekt.play()
        for meteor in durum:
            boom = Patlama.Patlama(meteor, patlamaKlasoru, patlamaResimleri)
            all_sprites.add(boom)
            parca1.kalkan -= meteor.radius * 3

    Kalkan.kalkanCiz(pencere, 5, 5, parca1.kalkan)
    CanCiz.canCiz(pencere, 5, 25, parca1.can)
    Ulti.ultiCiz(pencere, 5, 50, Ulti.ulti)
    if Ulti.ulti == 100:
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_x:
                Ulti.ulti = 0
                parca1.changeBulletSpeed(20)
    if durum or mermiSayisi == 0:
        if parca1.kalkan <= 0:
            pygame.mixer.music.load(os.path.join(sesKlasoru, "patlama_efekti.mp3"))
            pygame.mixer.music.play()
            pygame.mixer.music.load(os.path.join(sesKlasoru, "Blue_Space.mp3"))
            pygame.mixer.music.play()
            parca1.can -= 1
            parca1.hide()
            if parca1.can == 0:
                game_over = True

            parca1.kalkan = 100

        if mermiSayisi == 0:
            if sayacSifirlama:
                bitisDegeri = pygame.time.get_ticks()
                sayacSifirlama = False
                levelYaziFont = pygame.font.SysFont("Helvetica", 50)
                yazi = levelYaziFont.render("Level :{}".format(level + 1), 1, (0, 255, 0))

            pencere.blit(yazi, (500, 0))

            if pygame.time.get_ticks() - bitisDegeri > 4000:
                sayacSifirlama = True
                level += 1

                for i in range(level * 10):
                    mermi = Mermi()
                    all_sprites.add(mermi)
                    mermiler.add(mermi)

    pygame.display.update()
