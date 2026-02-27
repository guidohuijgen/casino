#casinowalk
import play
import random

achtergrond = play.new_box(color = "dark red", width = 800, height = 800, transparency=0)

beginscherm = play.new_box (color = "light blue", width= 800, height = 1000)

slot_machine = play.new_image("slotmachinebegin.png",size = 80, x = 260, y = 150, transparency=0 )
slot_machine_game = play.new_image("slotmachinegame.png", size = 80, y = 148, x = 260, transparency=0 )

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

doorgaan = play.new_text('DOORGAAN ->', y = -200)
doorgaan.hide()

money = 20
money_button = play.new_text (f'{money} ', color = 'black', font_size = 25, x = 270, y = 240, transparency=0)

game_over = play.new_text("JE BENT BLUT...", color = "red",font_size = 60, transparency=0)

press_e_start_roulette = play.new_text("Press E to start the roulette game!", color= "black", font_size = 25, y = -100)
press_e_start_roulette.hide()
press_f_start_coinflip = play.new_text("Press F to start the coinflip game!", color= "black", font_size = 25, y = -100)
press_f_start_coinflip.hide()
press_g_start_slotmachine = play.new_text("Press G to start the slot machine game!",color = 'black', font_size = 25, y= -100)
press_g_start_slotmachine.hide()

shop_text_welcome = play.new_text("Welcome to the shop!",color="black",font_size=35,y=225, x =0)
shopt_text_explain = play.new_text("Here you can buy outfit upgrades to level up", color = "black", font_size = 20, y = 190, x = 0)
shop_text_welcome.hide()
shopt_text_explain.hide()

shop_text_geld_upgrade1 = play.new_text("€20,-", color = "black", font_size= 20 , y = -25, x = -225)
shop_text_geld_upgrade1.hide()
shop_text_geld_upgrade2 = play.new_text("€80,-", color = "black", font_size = 20, y = -25, x = -75)
shop_text_geld_upgrade2.hide()
shop_text_geld_upgrade3 = play.new_text("€150,-", color = "black", font_size = 20, y = -25, x = 75)
shop_text_geld_upgrade3.hide()
shop_text_geld_upgrade4 = play.new_text("€250,-", color = "black", font_size = 20, y = -25, x = 225)
shop_text_geld_upgrade4.hide()
shop_text_geld_upgrade5 = play.new_text("€400,-", color = "black", font_size = 20, y = -175, x = -225)
shop_text_geld_upgrade5.hide()
shop_text_geld_upgrade6 = play.new_text("€650,-", color = "black", font_size = 20, y = -175, x = -75)
shop_text_geld_upgrade6.hide()
shop_text_geld_upgrade7 = play.new_text("€1000,-", color = "black", font_size = 20, y = -175, x = 75)
shop_text_geld_upgrade7.hide()
shop_text_geld_upgrade8 = play.new_text("€2000,-", color = "black", font_size = 20, y = -175, x = 225)
shop_text_geld_upgrade8.hide()

#test
gekocht_1 = False
gekocht_2 = False
gekocht_3 = False
gekocht_4 = False
gekocht_5 = False
gekocht_6 = False
gekocht_7 = False
gekocht_8 = False

upgrade_1 = play.new_image("zwerverboi.png", size = 32, transparency = 0, x = -225, y = 30)
upgrade_2 = play.new_image("niet meer straatarm.png", size = 10, transparency = 0, x = -75, y = 30)
upgrade_3 = play.new_image("soort van rijk.png", size = 33, transparency = 0, x = 75, y = 30)
upgrade_4 = play.new_image("best rijk.png", size = 30, transparency= 0, x = 225, y = 30)
upgrade_5 = play.new_image("koning5.png", size = 12, transparency= 0, x = -225, y = -120)
upgrade_6 = play.new_image("koning zes.png", size = 30, transparency= 0, x = -75, y = -120)
upgrade_7 = play.new_image("7.png", size = 13, transparency = 0, x = 75, y = -112)
upgrade_8 = play.new_image("8.png", size = 13, transparency= 0, x =225, y = -98)

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
win = play.new_text(f"Je hebt €{winst},-  gewonnen!")
win.hide()
verlies = 0
loss = play.new_text(f"Je hebt €{verlies},- verloren...")
loss.hide()

in_game = False 

@play.repeat_forever
async def game_over_function():
    if money <= 0:
            game_over.transparency = 100
            await play.timer(seconds = 3)
            play.stop_program

@start_box.when_clicked
def start_function():
    start_button.hide()
    start_box.hide()
    achtergrond.transparency = 100
    money_button.transparency = 100
    reset_button.show()
    beginscherm.transparency = 0
    shop.transparency = 100
    player.transparency = 100
    coin.transparency = 100
    slot_machine.transparency = 100
    player.y = 0
    player.x = 0
    welcoming_text.transparency = 0
    press_start_to_start_text.transparency = 0
    roulette.transparency = 100
    coinflip.transparency = 100

@reset_button.when_clicked
def reset_function():
    start_button.show()
    start_box.show()
    reset_button.hide()
    money_button.transparency = 0
    beginscherm.transparency = 100
    slot_machine.transparency=0
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
    upgrade_5.transparency = 100
    shop_text_geld_upgrade5.show()
    upgrade_6.transparency = 100
    shop_text_geld_upgrade6.show()
    upgrade_7.transparency = 100
    shop_text_geld_upgrade7.show()
    upgrade_8.transparency = 100
    shop_text_geld_upgrade8.show()
    achtergrond.transparency = 0
    player.transparency = 0
    slot_machine.transparency = 0
    reset_button.transparency = 0
    money_button.transparency = 100
    shop.transparency = 0
    shop_achtergrond.transparency = 100
    pijltje_terug.transparency = 100
    coin.transparency = 100
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
    slot_machine.transparency= 100
    shop_text_welcome.hide()
    shopt_text_explain.hide()
    shop_text_geld_upgrade1.hide()
    shop_text_geld_upgrade2.hide()
    shop_text_geld_upgrade3.hide()
    shop_text_geld_upgrade4.hide()
    shop_text_geld_upgrade5.hide()
    shop_text_geld_upgrade6.hide()
    shop_text_geld_upgrade7.hide()
    shop_text_geld_upgrade8.hide()
    upgrade_1.transparency = 0
    upgrade_2.transparency = 0
    upgrade_3.transparency = 0
    upgrade_4.transparency = 0
    upgrade_5.transparency = 0
    upgrade_6.transparency = 0
    upgrade_7.transparency = 0
    upgrade_8.transparency = 0


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
            global in_game
            in_game = True
            press_e_start_roulette.hide()
            rood.transparency =100
            black.transparency = 100
            of.transparency = 100
            kiezen.transparency = 100
            kies.transparency = 100           
            @rood.when_clicked
            def rood_keuze_function():
                resultaat_roul_function('rood')
            @black.when_clicked
            def zwart_keuze_function():
                resultaat_roul_function('zwart')
            def resultaat_roul_function(keuze_roul):
                resultaat_roul = random.choice(['rood','zwart'])
                if keuze_roul == resultaat_roul:
                    win.show()
                    rood.transparency = 0
                    of.transparency = 0
                    black.transparency = 0
                    kies.transparency = 0 
                    kiezen.transparency = 0
                    doorgaan.show()
                    @doorgaan.when_clicked
                    def reset_na_uitslag():
                        global in_game
                        win.hide()
                        in_game = False
                        doorgaan.hide()
                else:
                    loss.show()
                    rood.transparency = 0
                    of.transparency = 0
                    black.transparency = 0
                    kies.transparency = 0 
                    kiezen.transparency = 0
                    doorgaan.show()
                    @doorgaan.when_clicked
                    def reset_na_uitslag():
                        global in_game
                        loss.hide()
                        in_game = False
                        doorgaan.hide()

    else:

        press_e_start_roulette.hide()
             
    if player.is_touching(coinflip):
        press_f_start_coinflip.show()
        @play.when_key_pressed("f", "F")
        def coinflip_function():
            global in_game
            in_game =  True
            kiezen_coinflip.transparency= 100 
            kies_tekst.transparency = 100
            kop.transparency =100
            of_tekst.transparency =100
            munt.transparency = 100
            @kop.when_clicked
            def kies_kop():
                resultaat_coin_function('kop')
            @munt.when_clicked
            def kies_munt():
                resultaat_coin_function('munt')
            def resultaat_coin_function(keuze_coin):
                resultaat_coin = random.choice(['kop','munt'])
                if keuze_coin == resultaat_coin:
                    win.show()
                    kiezen_coinflip.transparency = 0
                    kies_tekst.transparency = 0
                    of_tekst.transparency = 0
                    kop.transparency = 0 
                    munt.transparency = 0
                    doorgaan.show()
                    @doorgaan.when_clicked
                    def reset_na_uitslag():
                        global in_game
                        win.hide()
                        in_game = False
                        doorgaan.hide()
                else:
                    loss.show()
                    kiezen_coinflip.transparency = 0
                    kies_tekst.transparency = 0
                    of_tekst.transparency = 0
                    kop.transparency = 0 
                    munt.transparency = 0
                    doorgaan.show()
                    @doorgaan.when_clicked
                    def reset_na_uitslag():
                        global in_game
                        loss.hide()
                        in_game = False
                        doorgaan.hide()
            
            # def inzet_function():
          
    else:
        press_f_start_coinflip.hide()

    if player.is_touching(slot_machine):
        press_g_start_slotmachine.show()
        @play.when_key_pressed('g','G')
        def slot_machine_function():
            slot_machine.transparency = 0
            slot_machine_game.transparency = 100


if upgrade_1.transparency == 100:      
    @upgrade_1.when_clicked
    def buy_upgrade1():
        global gekocht_1
        if not gekocht_1:
            koop_character(20, "zwerverboi.png")
            gekocht_1 = True
        else:
            player.image = "zwerverboi.png"

if upgrade_2.transparency == 100:
    @upgrade_2.when_clicked
    def buy_upgrade2():
        global gekocht_2
        if not gekocht_2:
            koop_character(80, "niet meer straatarm.png")
            gekocht_2 = True
        else:
            player.image = "niet meer straatarm.png"
if upgrade_3.transparency == 100:
    @upgrade_3.when_clicked
    def buy_upgrade3():
        global gekocht_3
        if not gekocht_3:
            koop_character(150, "soort van rijk.png")
            gekocht_3 = True
        else:
            player.image = "soort van rijk.png"
if upgrade_4.transparency == 100:
    @upgrade_4.when_clicked
    def buy_upgrade4():
        global gekocht_4
        if not gekocht_4:
            koop_character(250, "best rijk.png")
            gekocht_4 = True
        else:
            player.image = "best rijk.png"

if upgrade_5.transparency == 100:
    @upgrade_5.when_clicked
    def buy_upgrade5():
        global gekocht_5
        if not gekocht_5:
            koop_character(450, "koning5.png")
            gekocht_5 = True
        else:
            player.image = "koning5.png"

if upgrade_6.transparency == 100:
    @upgrade_6.when_clicked
    def buy_upgrade6():
        global gekocht_6
        if not gekocht_6:
            koop_character(650, "koning zes.png")
            gekocht_6 = True
        else:
            player.image = "koning zes.png"
if upgrade_7.transparency == 100:
    @upgrade_7.when_clicked
    def buy_upgrade7():
        global gekocht_7
        if not gekocht_7:
            koop_character(1000, "7.png")
            gekocht_7 = True
        else:
            player.image = "7.png"
            player.angle = 180

if upgrade_8.transparency == 100:
    @upgrade_8.when_clicked
    def buy_upgrade8():
        global gekocht_8
        if not gekocht_8:
            koop_character(2000, "8.png")
            gekocht_8 = True
        else:
            player.image = "8.png"
            player.angle = 180

def koop_character(prijs, nieuwe_skin):
    global money
    if money >= prijs:
        money -= prijs
        money_button.text = f"{money}"
        player.image = nieuwe_skin
        if money <= 0:
            game_over.transparency = 100
    else:
        play.new_text("Niet genoeg geld!", y=150, font_size=30)

@play.repeat_forever
def stop_presstostart_function():
    if in_game == True:
        press_f_start_coinflip.hide()
        press_e_start_roulette.hide()

play.start_program()
