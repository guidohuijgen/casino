#casinowalk
import play
import random

achtergrond = play.new_box(color = "dark red", width = 800, height = 800, transparency=0)

beginscherm = play.new_box (color = "light blue", width= 800, height = 1000)

roulette = play.new_image("roullette.png", size  = 100, x = -300, y = -200, transparency= 0)

coinflip = play.new_image("image.png", size = 60, x = -300, y = 200, transparency= 0)

player = play.new_image("zwerver.png", size = 30, transparency=0)

shop = play.new_image("shop.png", size = 25, transparency= 0, x = 350, y = 260)

shop_achtergrond = play.new_box(color = "light blue", width = 800,height = 800, transparency=0)

pijltje_terug = play.new_image("pijl.png", size = 20, transparency=0, x = 350, y = 260)

coin = play.new_image("munt.png", size = 10, transparency = 0, y = 244, x = 235)

start_box = play.new_box(color = 'red',width=250, height=85)

start_button = play.new_text('START',color ='white',y= -8, font_size=70)

welcoming_text = play.new_text('Welcome to Casino Walk!', color = 'black', y = 52, font_size = 20)

press_start_to_start_text = play.new_text('Press start to start the game',size = 10, color = 'black', y= -55, font_size = 20)

reset_button = play.new_text('RESET',color = 'black', font_size = 20, x = 270, y = 270)
reset_button.hide()

money = 20
money_button = play.new_text (f'{money} ', color = 'black', font_size = 25, x = 270, y = 240)
money_button.hide() 

game_over = play.new_text("JE BENT BLUT...", color = "red",font_size = 60, transparency=0)

press_e_start_roulette = play.new_text("Press E to start the roulette game!", color= "black", font_size = 25)
press_e_start_roulette.hide()
press_f_start_coinflip = play.new_text("Press F to start the coinflip game!", color= "black", font_size = 25)
press_f_start_coinflip.hide()

shop_text_welcome = play.new_text("Welcome to the shop!",color="black",font_size=35,y=225, x =0)
shopt_text_explain = play.new_text("Here you can buy outfit upgrades to level up", color = "black", font_size = 20, y = 190, x = 0)
shop_text_welcome.hide()
shopt_text_explain.hide()

shop_text_geld_upgrade1 = play.new_text("20", color = "black", font_size= 20 , y = -25, x = -225)
shop_text_geld_upgrade1.hide()
shop_text_geld_upgrade2 = play.new_text("80", color = "black", font_size = 20, y = -25, x = -75)
shop_text_geld_upgrade2.hide()
shop_text_geld_upgrade3 = play.new_text("150", color = "black", font_size = 20, y = -25, x = 75)
shop_text_geld_upgrade3.hide()
shop_text_geld_upgrade4 = play.new_text("250", color = "black", font_size = 20, y = -25, x = 225)
shop_text_geld_upgrade4.hide()

upgrade_1 = play.new_image("zwerverboi.png", size = 32, transparency = 0, x = -225, y = 30)
upgrade_2 = play.new_image("niet meer straatarm.png", size = 10, transparency = 0, x = -75, y = 30)
upgrade_3 = play.new_image("soort van rijk.png", size = 33, transparency = 0, x = 75, y = 30)
upgrade_4 = play.new_image("best rijk.png", size = 30, transparency= 0, x = 225, y = 30)

kiezen = play.new_text("Klik rood of zwart om te kiezen", y = 70, transparency=0)
kies = play.new_text("Kies je",color  = "white", x = -160, transparency=0)
rood = play.new_text("rood", color = "red", transparency=0)
of  = play.new_text("of",color = "white", x = 90, transparency=0)
black = play.new_text("zwart?", x = 220, transparency=0)

kiezen_coinflip = play.new_text("Klik kop of munt om te kiezen", y=70, font_size=30, transparency= 0)
kies_tekst = play.new_text("Kies je", color="white", x=-160, transparency=0)
kop = play.new_text("kop", color="red", x=-20, transparency= 0)
of_tekst = play.new_text("of", color="white", x=50, transparency=0)
munt = play.new_text("munt", color="green", x=150, transparency=0)

winst = 0
keuze_roul = ''
win = play.new_text(f"Je {winst} hebt gewonnen!")
win.hide()
keuze_coin = ''
loss = play.new_text("Je hebt verloren...")
loss.hide()

@start_box.when_clicked
def start_function():
    start_button.hide()
    start_box.hide()
    achtergrond.transparency = 100
    money_button.show()
    reset_button.show()
    beginscherm.transparency = 0
    shop.transparency = 100
    player.transparency = 100
    coin.transparency = 100
    player.y = 0
    player.x = 0
    welcoming_text.transparency = 0
    press_start_to_start_text.transparency = 0
    roulette.transparency = 100
    coinflip.transparency = 100
    if money <= 0:
        game_over.transparency = 100
        play.stop_program

@reset_button.when_clicked
def reset_function():
    start_button.show()
    start_box.show()
    reset_button.hide()
    money_button.hide()
    beginscherm.transparency = 100
    achtergrond.transparency = 0
    shop.transparency = 0
    player.transparency = 0
    coin.transparency = 0
    welcoming_text.transparency = 100
    press_start_to_start_text.transparency = 100
    roulette.transparency = 0
    coinflip.transparency = 0
    game_over.transparency = 0
    
@play.when_key_pressed("w","up")
def vooruit_function():
    player.y = player.y + 6
@play.when_key_pressed("a","left")
def links_function():
    player.x = player.x -6
@play.when_key_pressed("s","down")
def achteruit_function():
    player.y = player.y -6
@play.when_key_pressed("d","right") 
def rechts_function():
    player.x = player.x +6

@player.when_clicked
def draai_function():
    @play.when_key_pressed("a", "left")
    def loop_links_function():
        player.angle = 90
    @play.when_key_pressed("s","down")
    def loop_naarbeneden_function():
        player.angle = 180
    @play.when_key_pressed("d","right")
    def loop_rechts_function():
        player.angle = 270
    @play.when_key_pressed("w","up")
    def loop_naarvoren_function():
        player.angle = 0

@shop.when_clicked
def shop_open_function():
    upgrade_1.transparency = 100
    shop_text_geld_upgrade1.show()
    upgrade_2.transparency = 100
    shop_text_geld_upgrade2.show()
    upgrade_3.transparency = 100
    shop_text_geld_upgrade3.show()
    upgrade_4.transparency = 100
    shop_text_geld_upgrade4.show()
    achtergrond.transparency = 0
    player.transparency = 0
    reset_button.transparency = 0
    money_button.transparency = 0
    shop.transparency = 0
    shop_achtergrond.transparency = 100
    pijltje_terug.transparency = 100
    coin.transparency = 0
    roulette.transparency = 0
    coinflip.transparency = 0
    game_over.transparency = 0
    shop_text_welcome.show()
    shopt_text_explain.show()


@pijltje_terug.when_clicked
def shop_sluiten_function():
    achtergrond.transparency = 100
    player.transparency = 100
    reset_button.transparency =100
    money_button.transparency = 100
    shop.transparency = 100
    shop_achtergrond.transparency = 0
    pijltje_terug.transparency = 0
    coin.transparency = 100
    roulette.transparency = 100
    coinflip.transparency = 100
    shop_text_welcome.hide()
    shopt_text_explain.hide()
    upgrade_1.transparency = 0
    shop_text_geld_upgrade1.hide()
    shop_text_geld_upgrade2.hide()
    shop_text_geld_upgrade3.hide()
    shop_text_geld_upgrade4.hide()
    upgrade_2.transparency = 0
    upgrade_3.transparency = 0
    upgrade_4.transparency = 0
    if money <= 0:
        game_over.transparency = 100
        play.stop_program

@play.repeat_forever
def doorloop_function():
    if player.x > 415:
        player.x = -415
    if player.x < -415:
        player.x = 415
    if player.y > 315:
        player.y = -315
    if player.y < -315:
        player.y = 315
    if player.is_touching(roulette):
        press_e_start_roulette.show()
        @play.when_key_pressed("e", "E")
        def roulette_function():
            global keuze_roul
            press_e_start_roulette.hide() 
            rood.transparency =100
            black.transparency = 100
            of.transparency = 100
            kiezen.transparency = 100
            kies.transparency = 100           
            @rood.when_clicked
            def rood_keuze_function():
                keuze_roul = 'rood'
            @black.when_clicked
            def zwart_keuze_function():
                keuze_roul = 'zwart'
            keuzes_roul = ['rood', 'zwart']
            resultaat_roul = random.choice(keuzes_roul)
            if keuze_roul == resultaat_roul:
                win.show()
                rood.transparency = 0
                of.transparency = 0
                black.transparency = 0
                kies.transparency = 0 
                kiezen.transparency = 0
            elif keuze_roul != resultaat_roul:
                loss.show()
                rood.transparency = 0
                of.transparency = 0
                black.transparency = 0
                kies.transparency = 0 
                kiezen.transparency = 0
            else:
                press_e_start_roulette.hide()  
    else:
        press_e_start_roulette.hide()
        win.hide()
        loss.hide()
             
    if player.is_touching(coinflip):
        press_f_start_coinflip.show()
        @play.when_key_pressed("f", "F")
        def coinflip_function():
            global keuze_coin
            kiezen_coinflip.transparency= 100 
            kies_tekst.transparency = 100
            kop.transparency =100
            of_tekst.transparency =100
            munt.transparency = 100
            @kop.when_clicked
            def kies_kop():
                keuze_coin = 'kop'
            @munt.when_clicked
            def kies_munt():
                keuze_coin = 'munt'
            resultaat_coin = random.choice(['kop', 'munt'])
            if keuze_coin == resultaat_coin:
                win.show()
                kiezen_coinflip.transparency = 0
                kies_tekst.transparency = 0
                of_tekst.transparency = 0
                kop.transparency = 0
                munt.transparency = 0
            else:
                loss.show()
                kiezen_coinflip.transparency = 0
                kies_tekst.transparency = 0
                of_tekst.transparency = 0
                kop.transparency = 0
                munt.transparency = 0
             
        

            # def inzet_function():
          
    else:
        press_f_start_coinflip.hide()
        win.hide()
        loss.hide()
        

play.start_program()
