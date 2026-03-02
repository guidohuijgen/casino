#casinowalk
import play
import random
 
achtergrond = play.new_box(color = "dark red", width = 800, height = 800, transparency=0)
 
beginscherm = play.new_box (color = "light blue", width= 800, height = 1000)
 
slot_machine = play.new_image("slotmachinebegin.png",size = 80, x = 260, y = 150, transparency=0 )
slot_machine_game = play.new_image("slotmachinegame.png", size = 80, y = 148, x = 260, transparency=0 )
 
appel_slot1= play.new_image("appel.png", size = 30, transparency= 0)
appel_slot2= play.new_image("appel.png", size = 30, transparency= 0)
appel_slot3= play.new_image("appel.png", size = 30, transparency= 0)
bar_slot1 = play.new_image("bar.png", size = 30, transparency= 0)
bar_slot2 = play.new_image("bar.png", size = 30, transparency= 0)
bar_slot3 = play.new_image("bar.png", size = 30, transparency= 0)
bel_slot1 = play.new_image("bel.png", size  =30, transparency= 0 )
bel_slot2 = play.new_image("bel.png", size  =30, transparency= 0 )
bel_slot3 = play.new_image("bel.png", size  =30, transparency= 0 )
druif_slot1  = play.new_image("druif.png", size = 30, transparency=0)
druif_slot2  = play.new_image("druif.png", size = 30, transparency=0)
druif_slot3  = play.new_image("druif.png", size = 30, transparency=0)
hart_slot1 = play.new_image("hart.png", size = 30,transparency=0)
hart_slot2 = play.new_image("hart.png", size = 30,transparency=0)
hart_slot3 = play.new_image("hart.png", size = 30,transparency=0)
kers_slot1 = play.new_image("kers.png", size = 30, transparency=0 )
kers_slot2 = play.new_image("kers.png", size = 30, transparency=0 )
kers_slot3 = play.new_image("kers.png", size = 30, transparency=0 )
limoen_slot1 = play.new_image("peer.png", size = 30, transparency=0)
limoen_slot2 = play.new_image("peer.png", size = 30, transparency=0)
limoen_slot3 = play.new_image("peer.png", size = 30, transparency=0)
zeven_slot1 = play.new_image("slot7.png",size = 30, transparency=0)
zeven_slot2 = play.new_image("slot7.png",size = 30, transparency=0)
zeven_slot3 = play.new_image("slot7.png",size = 30, transparency=0)
 
roulette = play.new_image("roulette plaatje.png", size  = 80, x = -300, y = -200, transparency= 0)
 
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
doorgaan_coin = play.new_text('DOORGAAN ->', y = -200)
doorgaan_coin.hide()
doorgaan_roul = play.new_text('DOORGAAN ->', y = -200)
doorgaan_roul.hide()
doorgaan_slot = play.new_text('DOORGAAN ->', y = -200)
doorgaan_slot.hide()
doorgaan_rr = play.new_text('DOORGAAN ->', y = -200)
doorgaan_rr.hide()
doorgaan_cc = play.new_text('DOORGAAN ->', y = -200)
doorgaan_cc.hide()
 
money = 20
money_button = play.new_text (f'{money}', color = 'black', font_size = 25, x = 280, y = 240, transparency=0)
inzet = 0
 
game_over = play.new_text("JE BENT BLUT...", color = "red",font_size = 60, transparency=0)
 
press_e_start_roulette = play.new_text("Press E to start the roulette", color = "black", font_size = 25, x = 0, y = -100,)
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
 
kleuren = {0: "green",1: "red", 2: "black", 3: "red", 4: "black", 5: "red",6: "black", 7: "red", 8: "black", 9: "red",10: "black", 11: "red", 12: "black", 13: "red",14: "black", 15: "red", 16: "black", 17: "red", 18: "black", 19: "red", 20: "black", 21: "red", 22: "black", 23: "red", 24: "black", 25: "red", 26: "black", 27: "red", 28: "black", 29: "red", 30: "black", 31: "red", 32: "black", 33: "red",34: "black", 35: "red", 36: "black"}
 
roulette_0 = play.new_text("0", x=-300, y=-50, transparency=0, color="green", font_size=30)
roulette_1 = play.new_text("1", x=-265, y=-50, transparency=0, color="red", font_size=30)
roulette_2 = play.new_text("2", x=-230, y=-50, transparency=0, color="black", font_size=30)
roulette_3 = play.new_text("3", x=-195, y=-50, transparency=0, color="red", font_size=30)
roulette_4 = play.new_text("4", x=-160, y=-50, transparency=0, color="black", font_size=30)
roulette_5 = play.new_text("5", x=-125, y=-50, transparency=0, color="red", font_size=30)
roulette_6 = play.new_text("6", x=-90, y=-50, transparency=0, color="black", font_size=30)
roulette_7 = play.new_text("7", x=-55, y=-50, transparency=0, color="red", font_size=30)
roulette_8 = play.new_text("8", x=-20, y=-50, transparency=0, color="black", font_size=30)
roulette_9 = play.new_text("9", x=15, y=-50, transparency=0, color="red", font_size=30)
roulette_10 = play.new_text("10", x=50, y=-50, transparency=0, color="black", font_size=30)
roulette_11 = play.new_text("11", x=85, y=-50, transparency=0, color="red", font_size=30)
roulette_12 = play.new_text("12", x=120, y=-50, transparency=0, color="black", font_size=30)
roulette_13 = play.new_text("13", x=155, y=-50, transparency=0, color="red", font_size=30)
roulette_14 = play.new_text("14", x=190, y=-50, transparency=0, color="black", font_size=30)
roulette_15 = play.new_text("15", x=225, y=-50, transparency=0, color="red", font_size=30)
roulette_16 = play.new_text("16", x=260, y=-50, transparency=0, color="black", font_size=30)
roulette_17 = play.new_text("17", x=295, y=-50, transparency=0, color="red", font_size=30)
roulette_18 = play.new_text("18", x=330, y=-50, transparency=0, color="black", font_size=30)
roulette_19 = play.new_text("19", x=-300, y=-100, transparency=0, color="red", font_size=30)
roulette_20 = play.new_text("20", x=-265, y=-100, transparency=0, color="black", font_size=30)
roulette_21 = play.new_text("21", x=-230, y=-100, transparency=0, color="red", font_size=30)
roulette_22 = play.new_text("22", x=-195, y=-100, transparency=0, color="black", font_size=30)
roulette_23 = play.new_text("23", x=-160, y=-100, transparency=0, color="red", font_size=30)
roulette_24 = play.new_text("24", x=-125, y=-100, transparency=0, color="black", font_size=30)
roulette_25 = play.new_text("25", x=-90, y=-100, transparency=0, color="red", font_size=30)
roulette_26 = play.new_text("26", x=-55, y=-100, transparency=0, color="black", font_size=30)
roulette_27 = play.new_text("27", x=-20, y=-100, transparency=0, color="red", font_size=30)
roulette_28 = play.new_text("28", x=15, y=-100, transparency=0, color="black", font_size=30)
roulette_29 = play.new_text("29", x=50, y=-100, transparency=0, color="red", font_size=30)
roulette_30 = play.new_text("30", x=85, y=-100, transparency=0, color="black", font_size=30)
roulette_31 = play.new_text("31", x=120, y=-100, transparency=0, color="red", font_size=30)
roulette_32 = play.new_text("32", x=155, y=-100, transparency=0, color="black", font_size=30)
roulette_33 = play.new_text("33", x=190, y=-100, transparency=0, color="red", font_size=30)
roulette_34 = play.new_text("34", x=225, y=-100, transparency=0, color="black", font_size=30)
roulette_35 = play.new_text("35", x=260, y=-100, transparency=0, color="red", font_size=30)
roulette_36 = play.new_text("36", x=295, y=-100, transparency=0, color="black", font_size=30)


roulette_knoppen = [roulette_0, roulette_1, roulette_2, roulette_3, roulette_4,roulette_5, roulette_6, roulette_7, roulette_8, roulette_9,roulette_10, roulette_11, roulette_12, roulette_13, roulette_14,roulette_15, roulette_16, roulette_17, roulette_18, roulette_19,roulette_20, roulette_21, roulette_22, roulette_23, roulette_24,roulette_25, roulette_26, roulette_27, roulette_28, roulette_29,roulette_30, roulette_31, roulette_32, roulette_33, roulette_34,roulette_35, roulette_36]

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
upgrade_5 = play.new_image("koning5.png", size = 12, transparency= 0, x = -225, y = -110)
upgrade_6 = play.new_image("koning zes.png", size = 30, transparency= 0, x = -75, y = -105)
upgrade_7 = play.new_image("7.png", size = 13, transparency = 0, x = 75, y = -105, angle = 180)
upgrade_8 = play.new_image("8.png", size = 13, transparency= 0, x =225, y = -98, angle = 180)
 
kiezen = play.new_text("Klik rood of zwart om te kiezen of kies een nummer", y = 70, transparency=0, font_size = 30)
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
win = play.new_text("Je hebt gewonnen!", font_size=25)
win.hide()
super_win = play.new_text("Je hebt 3x hetzelfde symbool, dus GEWONNEN!!", font_size= 25)
super_win.hide()
partial_win = play.new_text("Je hebt 2x hetzelfde symbool, dus gewonnen!!", font_size = 25)
partial_win.hide()
verlies = 0
loss = play.new_text("Je hebt verloren...", font_size=25)
loss.hide()
 
kies_inzet = play.new_text("Kies je inzet, door te klikken!", color = 'black', y = 100, font_size=25, transparency= 0)
vijf_inzet = play.new_text("€5,-", color = 'black', font_size= 25, x = -300,transparency=0 )
tien_inzet = play.new_text ("€10,-", color= 'black', font_size=25,x = -240, transparency=0 )
twintig_inzet = play.new_text("€20,-", color = 'black', font_size=25, x = -170, transparency=0)
vijftig_inzet = play.new_text ("€50,-", color = 'black', font_size = 25, x = -100, transparency=0)
honderd_inzet = play.new_text("€100,-", color = "black", font_size = 25, x = -20, transparency=0)
vijfhonderd_inzet = play.new_text ("€500,-", color = 'black', font_size=25, x = 80, transparency=0)
duizend_inzet = play.new_text ("€1000,-", color = 'black', font_size=25, x = 180, transparency= 0)
tweeduizend_inzet = play.new_text ("€2000,-",color= 'black',font_size=25, x = 300, transparency=0)
 
in_game = False
inzet_ingevoerd = False

uitslag = play.new_text("", font_size = 25, y =200)
uitslag.hide()

uitslag_tonen = play.new_text("", font_size = 25, y = 100)
uitslag_tonen.hide()
 
niet_genoeg = play.new_text("Niet genoeg geld!", y=150, font_size=30, transparency=0)
opnieuw = play.new_text ("Klik opnieuw", y = 50, font_size = 30, transparency=0)
 
foto_slot1 = None
foto_slot2 = None
foto_slot3 = None

uitleg_text1 = play.new_text('Je bent een hopeloze zwerver die net een briefje', color = 'black', y = 250, font_size = 25)
uitleg_text2 = play.new_text('van 20 euro op straat heeft gevonden.', color = 'black', y = 220, font_size = 25)
uitleg_text3 = play.new_text('De casino om de hoek is je laatste hoop om'  , color = 'black', y = 190, font_size = 25)
uitleg_text4 = play.new_text('weer op het goede pad te komen!', color = 'black', y = 160, font_size = 25)
uitleg_tex5 = play.new_text('Je loopt naar binnen om je geluk te testen. Wees voorzichtig,' , color = 'black', y = 130, font_size = 25)
uitleg_text6 = play.new_text('want als je geen geld meer hebt is het game over.', color = 'black', y = 100, font_size = 25)
uitleg_text7 = play.new_text("Er zijn ook hulpmiddelen zoals de risicoknop en de kist.",color = 'black', y = -100, font_size = 25)
uitleg_text8 = play.new_text("Maar de kans is groter dat je verliest dan dat je wint dus kijk uit!",color = 'black', y = -130, font_size = 25)


chest = play.new_image("chest closed.png", size=40, x=250, y=-200, transparency=0)
chest_open = play.new_image("chest open.png", size = 40, x= 250,y= -200, transparency=0 )
kost_20 = play.new_text("Deze kist kost 20,-",color = 'black', y = -150,x =250, font_size = 25, transparency=0)

def begintekst():
    uitleg_text1.transparency = 0
    uitleg_text2.transparency = 0
    uitleg_text3.transparency = 0
    uitleg_text4.transparency = 0
    uitleg_tex5.transparency = 0
    uitleg_text6.transparency = 0
    uitleg_text7.transparency = 0
    uitleg_text8.transparency = 0
 
 
@chest.when_clicked
async def open_kist():
    global money
    global money_button
    chest.hide()
    chest_open.transparency = 100
    if money >= 20:
        money -= 20  
        if random.randint(1, 10) <= 3:
            money += 150
        money_button.hide()
        money_button = play.new_text(f"{money}", color ='black', font_size =25, x= 280, y = 240, transparency = 100)
        money_button.show()
        chest.x = random.randint(-400, 400)
        chest.y = random.randint(-300, 300)
        await play.timer(seconds= 2)
        chest_open.hide()
        kost_20.hide()

risico_knop = play.new_image("risicoknop.png", size=25, x=-200, y=-50, transparency=0)

@play.repeat_forever
async def risico():
    if risico_knop.transparency == 100:
        risico_knop.x = random.randint(-414,414)
        risico_knop.y = random.randint(-314,314)
        await play.timer(seconds = 1)
        risico_knop.transparency = 0
        risico_knop.x = random.randint(-414,414)
        risico_knop.y = random.randint(-314,314)
        await play.timer(seconds = 1)
        risico_knop.transparency = 100
@risico_knop.when_clicked
def druk_op_knop():
    global money
    global money_button
    if random.randint(1, 2) == 1:
        money *= 2
    else:
        money //= 2
    money_button.hide()
    money_button = play.new_text(f"{money}", color='black', font_size= 25, x =280, y= 240, transparency= 100)
    money_button.show()
    risico_knop.hide()
 
def roulette_show():
    for i in roulette_knoppen:
        i.transparency = 100
def roulette_hide():
    for i in roulette_knoppen:
        i.transparency = 0

@start_box.when_clicked
def start_function():
    begintekst()
    kost_20.transparency = 100
    chest.transparency = 100
    risico_knop.transparency = 100
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
    kost_20.transparency = 0
    chest.transparency = 0
    risico_knop.transparency = 0
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
    begintekst()
   
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
    kost_20.transparency = 0
    chest.transparency= 0
    risico_knop.transparency = 0
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
    kost_20.transparency = 0
    chest.transparency = 100
    risico_knop.transparency = 100
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
    else:
        press_e_start_roulette.hide()
    if player.is_touching(coinflip):
        press_f_start_coinflip.show()          
    else:
        press_f_start_coinflip.hide()
    if player.is_touching(slot_machine):
        press_g_start_slotmachine.show()  
    else:
        press_g_start_slotmachine.hide()

@play.when_key_pressed('g','G')
def slot_machine_function():
    if player.is_touching(slot_machine):
        press_e_start_roulette.hide()
        press_f_start_coinflip.hide()
        press_g_start_slotmachine.hide()
        global in_game
        in_game =  True
        inzet_function()
        doorgaan_slot.show()
@doorgaan_slot.when_clicked
def echte_slot_function():
    doorgaan_slot.hide()
    if inzet_ingevoerd == True:
        slot_machine.transparency = 0
        slot_machine_game.transparency = 100
        slot_combo_function()
def slot_combo_function():
    global foto_slot1
    global foto_slot2
    global foto_slot3
    keuzen = ["kers1","kers2", "kers3", "appel1","appel2", "appel3", "druif1","druif2", "druif3","hart1","hart2","hart3", "limoen1", "limoen2","limoen3", "bar1","bar2", "bar3", "bel1","bel2","bel3", "zeven1", "zeven2","zeven3"]
    keuzen_naar_image  = {"kers1": kers_slot1,"kers2":kers_slot2,"kers3":kers_slot3, "appel1":appel_slot1,"appel2":appel_slot2, "appel3":appel_slot3, "druif1": druif_slot1,"druif2":druif_slot2, "druif3":druif_slot3, "hart1": hart_slot1, "hart2":hart_slot2, "hart3":hart_slot3,"limoen1": limoen_slot1,"limoen2": limoen_slot2,"limoen3":limoen_slot3, "bar1": bar_slot1,"bar2":bar_slot2,"bar3": bar_slot3,"bel1": bel_slot1,"bel2":bel_slot2, "bel3":bel_slot3, "zeven1": zeven_slot1, "zeven2": zeven_slot2,"zeven3":zeven_slot3}
    for i in keuzen_naar_image.values():
        i.transparency = 0
    slot_1 = random.choice(keuzen)
    keuzen.remove(slot_1)
    slot_1_foto = keuzen_naar_image[slot_1]
    del keuzen_naar_image[slot_1]
    slot_2 = random.choice(keuzen)
    keuzen.remove(slot_2)
    slot_2_foto = keuzen_naar_image[slot_2]
    del keuzen_naar_image[slot_2]
    slot_3 = random.choice(keuzen)
    keuzen.remove(slot_3)
    slot_3_foto = keuzen_naar_image[slot_3]
    del keuzen_naar_image[slot_3]
    slot_1_foto.x = 223
    slot_2_foto.x= 260
    slot_3_foto.x = 297
    slot_1_foto.y =145
    slot_2_foto.y = 145
    slot_3_foto.y = 145
    slot_1_foto.transparency = 100
    slot_2_foto.transparency =100
    slot_3_foto.transparency = 100
    foto_slot1 = slot_1_foto
    foto_slot2 = slot_2_foto
    foto_slot3 = slot_3_foto
    resultaat_slot_function(slot_1, slot_2, slot_3)
def resultaat_slot_function(slot_1,slot_2,slot_3):
    if slot_1[:3] == slot_2[:3] ==  slot_3[:3]:
        super_win.show()
        doorgaan_rr.show()
        if slot_1[:3] == "zev":
            slotwinst_function(1000)
        elif slot_1[:3] == "bar":
            slotwinst_function(500)
        elif slot_1[:3] == "har" or slot_1 == "bel":
            slotwinst_function(250)
        else:
            slotwinst_function(100)
    elif slot_1[:3] == slot_2[:3]:
        partial_win.show()
        doorgaan_rr.show()
        if slot_1[:3] == "zev":
            slotwinst_function(100)
        elif slot_1[:3] == "bar":
            slotwinst_function(50)
        elif slot_1[:3] == "har" or slot_1[:3] == "bel":
            slotwinst_function(25)
        else:
            slotwinst_function(10)
    elif slot_2[:3] == slot_3[:3]:        
        partial_win.show()
        doorgaan_rr.show()
        if slot_2[:3] == "zev": 
            slotwinst_function(100)
        elif slot_2[:3] == "bar":
            slotwinst_function(50)
        elif slot_2[:3] == "har" or slot_2[:3] == "bel":
            slotwinst_function(25)
        else:
            slotwinst_function(10)
    elif slot_1[:3] == slot_3[:3]:
        partial_win.show()
        doorgaan_rr.show()
        if slot_1[:3] == "zev":
            slotwinst_function(100)
        elif slot_1[:3] == "bar":
            slotwinst_function(50)
        elif slot_1[:3] == "har" or slot_1[:3] == "bel":
            slotwinst_function(25)
        else:
            slotwinst_function(10)
    else:
        loss.show()
        doorgaan_rr.show()
@doorgaan_rr.when_clicked
def reset_na_uitslag():
    global foto_slot1
    global foto_slot2
    global foto_slot3
    global in_game
    global inzet_ingevoerd
    global inzet
    super_win.hide()
    uitslag_tonen.hide()
    loss.hide()
    partial_win.hide()
    in_game = False
    inzet_ingevoerd = False
    inzet = 0
    doorgaan_rr.hide()
    foto_slot1.transparency = 0
    foto_slot2.transparency = 0
    foto_slot3.transparency = 0
    slot_machine.transparency = 100
    slot_machine_game.transparency = 0
    foto_slot1 = None
    foto_slot2 = None
    foto_slot3 = None
def slotwinst_function(multiplier):
    global money
    global inzet
    global money_button
    global uitslag_tonen
    money += inzet
    inzet *= multiplier
    money += inzet
    uitslag_tonen.hide()
    uitslag_tonen = play.new_text(f"Je hebt €{inzet},- erbij gekregen", font_size = 25, y = 100)
    uitslag_tonen.show()
    money_button.hide()
    money_button = play.new_text(f"{money}",color = 'black', font_size = 25, x = 280, y = 240, transparency=100)
    money_button.show()

def min_geld_function(bedrag):
    global money
    if money>= bedrag:
        global money_button
        global inzet_ingevoerd
        money-= bedrag
        money_button.hide()
        money_button= play.new_text (f'{money}', color = 'black', font_size = 25, x = 280, y = 240, transparency=0)
        money_button.show()
        money_button.transparency = 100
        kies_inzet.transparency = 0
        vijf_inzet.transparency =0
        tien_inzet.transparency = 0
        twintig_inzet.transparency = 0
        vijftig_inzet.transparency = 0
        honderd_inzet.transparency = 0
        vijfhonderd_inzet.transparency = 0
        duizend_inzet.transparency = 0
        tweeduizend_inzet.transparency = 0
        inzet_ingevoerd = True
    else:
        check_genoeg_geld(bedrag)
def inzet_function():
    kies_inzet.transparency = 100
    vijf_inzet.transparency =100
    tien_inzet.transparency = 100
    twintig_inzet.transparency = 100
    vijftig_inzet.transparency = 100
    honderd_inzet.transparency = 100
    vijfhonderd_inzet.transparency = 100
    duizend_inzet.transparency = 100
    tweeduizend_inzet.transparency = 100
    win.hide()
    loss.hide()
@vijf_inzet.when_clicked
def inzet_vijf_function():
    if vijf_inzet.transparency ==100:
        global money
        global inzet
        global inzet_ingevoerd
        inzet += 5
        check_genoeg_geld(5)
        min_geld_function(5)
@tien_inzet.when_clicked
def inzet_tien_function():
    if tien_inzet.transparency == 100:
        global money
        global inzet_ingevoerd
        global inzet
        inzet += 10
        check_genoeg_geld(10)
        min_geld_function(10)
@twintig_inzet.when_clicked
def inzet_twintig_function():
    if twintig_inzet.transparency == 100:
        global money
        global inzet_ingevoerd
        global inzet
        inzet += 20
        check_genoeg_geld(20)
        min_geld_function(20)
@vijftig_inzet.when_clicked
def inzet_vijftig_function():
    if vijftig_inzet.transparency == 100:
        global money
        global inzet_ingevoerd
        global inzet
        inzet += 50
        check_genoeg_geld(50)
        min_geld_function(50)
@honderd_inzet.when_clicked
def inzet_honderd_function():
    if honderd_inzet.transparency == 100:
        global money
        global inzet_ingevoerd
        global inzet
        inzet += 100
        check_genoeg_geld(100)
        min_geld_function(100)
@vijfhonderd_inzet.when_clicked
def inzet_vijfhonderd_function():
    if vijfhonderd_inzet.transparency == 100:
        global money
        global inzet_ingevoerd
        global inzet
        inzet += 500
        check_genoeg_geld(500)
        min_geld_function(500)
@duizend_inzet.when_clicked
def inzet_duizend_function():
    if duizend_inzet.transparency == 100:
        global money
        global inzet_ingevoerd
        global inzet
        inzet += 1000
        check_genoeg_geld(1000)
        min_geld_function(1000)
@tweeduizend_inzet.when_clicked
def inzet_tweeduizend_function():
    if tweeduizend_inzet.transparency == 100:
        global money
        global inzet_ingevoerd
        global inzet
        inzet += 2000
        check_genoeg_geld(2000)
        min_geld_function(2000)
def check_genoeg_geld(inzet):
    if money<inzet:
        niet_genoeg.transparency = 100
        opnieuw.transparency = 100
    else:
        opnieuw.transparency = 0
        niet_genoeg.transparency = 0
 
@play.repeat_forever
async def game_over_function():
    global in_game
    if in_game == False:
        if money <= 0:
                for i in range(0,4):
                    game_over.transparency = 100
                    await play.timer(seconds = 1)
                    game_over.transparency = 0
                    await play.timer(seconds = 1)
                play.stop_program()
 
@play.when_key_pressed("e", "E")
def roulette_function():
    if player.is_touching(roulette):
        press_e_start_roulette.hide()
        press_f_start_coinflip.hide()
        press_g_start_slotmachine.hide()
        global in_game
        global inzet_ingevoerd
        in_game = True
        inzet_function()
        doorgaan_roul.show()
def roullete_when_clicked(getal, nummer):
    @getal.when_clicked
    def getallen():
        if getal.transparency == 100:
            if inzet_ingevoerd == True:
                resultaat_roul_nummers(nummer)
roullete_when_clicked(roulette_0, '0')
roullete_when_clicked(roulette_1, '1')
roullete_when_clicked(roulette_2, '2')
roullete_when_clicked(roulette_3, '3')
roullete_when_clicked(roulette_4, '4')
roullete_when_clicked(roulette_5, '5')
roullete_when_clicked(roulette_6, '6')
roullete_when_clicked(roulette_7, '7')
roullete_when_clicked(roulette_8, '8')
roullete_when_clicked(roulette_9, '9')
roullete_when_clicked(roulette_10, '10')
roullete_when_clicked(roulette_11, '11')
roullete_when_clicked(roulette_12, '12')
roullete_when_clicked(roulette_13, '13')
roullete_when_clicked(roulette_14, '14')
roullete_when_clicked(roulette_15, '15')
roullete_when_clicked(roulette_16, '16')
roullete_when_clicked(roulette_17, '17')
roullete_when_clicked(roulette_18, '18')
roullete_when_clicked(roulette_19, '19')
roullete_when_clicked(roulette_20, '20')
roullete_when_clicked(roulette_21, '21')
roullete_when_clicked(roulette_22, '22')
roullete_when_clicked(roulette_23, '23')
roullete_when_clicked(roulette_24, '24')
roullete_when_clicked(roulette_25, '25')
roullete_when_clicked(roulette_26, '26')
roullete_when_clicked(roulette_27, '27')
roullete_when_clicked(roulette_28, '28')
roullete_when_clicked(roulette_29, '29')
roullete_when_clicked(roulette_30, '30')
roullete_when_clicked(roulette_31, '31')
roullete_when_clicked(roulette_32, '32')
roullete_when_clicked(roulette_33, '33')
roullete_when_clicked(roulette_34, '34')
roullete_when_clicked(roulette_35, '35')
roullete_when_clicked(roulette_36, '36')
@doorgaan_roul.when_clicked
def echte_roul_function():
    doorgaan_roul.hide()
    if inzet_ingevoerd == True:
        rood.transparency = 100
        black.transparency = 100
        of.transparency = 100
        kiezen.transparency = 100
        kies.transparency = 100  
        roulette_show()
@rood.when_clicked
def rood_keuze_function():
    if rood.transparency == 100:
        if inzet_ingevoerd == True:
            resultaat_roul_kleur('red')
@black.when_clicked
def zwart_keuze_function():
    if black.transparency == 100:
        if inzet_ingevoerd == True:
            resultaat_roul_kleur('black')
def resultaat_roul_nummers(keuze_roul):
    global uitslag
    resultaat_roul_nummer = random.randint(0,36)
    resultaat_kleur = kleuren[resultaat_roul_nummer]
    uitslag.hide()
    uitslag =  play.new_text(f"Het balletje is geland op {resultaat_roul_nummer}", font_size = 25, y = 200)
    uitslag.color = resultaat_kleur
    uitslag.show()
    if int(keuze_roul) == resultaat_roul_nummer:
        win.show()
        loss.hide()
        cijfer_winst_berekening()
    else:
        if resultaat_kleur == kleuren[int(keuze_roul)]:
            winst_berekening_function()
            win.show()
            loss.hide()
        else:
            loss.show()
            win.hide()
    rood.transparency = 0
    of.transparency = 0
    black.transparency = 0
    kies.transparency = 0
    kiezen.transparency = 0
    roulette_hide()
    doorgaan.show()
def resultaat_roul_kleur(keuze_kleur):
    global uitslag
    resultaat_roul_nummer = random.randint(0,36)
    resultaat_kleur = kleuren[resultaat_roul_nummer]
    uitslag.hide()
    uitslag =  play.new_text(f"Het balletje is geland op {resultaat_roul_nummer}", font_size = 25, y = 200)
    uitslag.color = resultaat_kleur
    uitslag.show()
    if keuze_kleur == resultaat_kleur:
        win.show()
        loss.hide()
        winst_berekening_function()
    else:
        loss.show()
        win.hide()
    rood.transparency = 0
    of.transparency = 0
    black.transparency = 0
    kies.transparency = 0
    kiezen.transparency = 0
    roulette_hide()
    doorgaan.show()
@doorgaan.when_clicked
def reset_na_uitslag():
    global in_game
    global uitslag
    global inzet_ingevoerd
    global inzet
    global uitslag_tonen
    uitslag_tonen.hide()
    win.hide()
    loss.hide()
    uitslag.hide()
    in_game = False
    inzet_ingevoerd = False
    inzet = 0
    doorgaan.hide()
def cijfer_winst_berekening():
    global money
    global inzet
    global uitslag_tonen
    global money_button
    money += inzet
    inzet *= 50
    money += inzet
    uitslag_tonen.hide()
    uitslag_tonen = play.new_text(f"Je hebt €{inzet},- erbij gekregen", font_size = 25, y = 100)
    uitslag_tonen.show()
    money_button.hide()
    money_button = play.new_text(f"{money}",color = 'black', font_size = 25, x = 280, y = 240, transparency=100)
    money_button.show()

@play.when_key_pressed("f", "F")
def coinflip_function():
    if player.is_touching(coinflip):
        press_e_start_roulette.hide()
        press_f_start_coinflip.hide()
        press_g_start_slotmachine.hide()
        global in_game
        in_game = True
        inzet_function()
        win.hide()
        loss.hide()
        doorgaan_coin.show()
@doorgaan_coin.when_clicked
def echte_coin_function():
    doorgaan_coin.hide()
    if inzet_ingevoerd == True:
        kiezen_coinflip.transparency= 100
        kies_tekst.transparency = 100
        kop.transparency =100
        of_tekst.transparency =100
        munt.transparency = 100
    else:
        press_f_start_coinflip.hide()  
@kop.when_clicked
def kies_kop():
    if kop.transparency == 100:
        resultaat_coin_function('kop')
@munt.when_clicked
def kies_munt():
    if munt.transparency == 100:
        resultaat_coin_function('munt')
def resultaat_coin_function(keuze_coin):
    resultaat_coin = random.choice(['kop','munt'])
    if keuze_coin == resultaat_coin:
        win.show()
        loss.hide()
        kiezen_coinflip.transparency = 0
        kies_tekst.transparency = 0
        of_tekst.transparency = 0
        kop.transparency = 0
        munt.transparency = 0
        winst_berekening_function()
        doorgaan_cc.show()
    else:
        loss.show()
        win.hide()
        kiezen_coinflip.transparency = 0
        kies_tekst.transparency = 0
        of_tekst.transparency = 0
        kop.transparency = 0
        munt.transparency = 0
        doorgaan_cc.show()
@doorgaan_cc.when_clicked
def reset_na_uitslag():
    global in_game
    global inzet_ingevoerd
    global inzet
    global uitslag_tonen
    win.hide()
    loss.hide()
    in_game = False
    inzet_ingevoerd = False
    uitslag_tonen.hide()
    inzet = 0
    doorgaan_cc.hide()
    kiezen_coinflip.transparency = 0
    kies_tekst.transparency = 0
    of_tekst.transparency = 0
    kop.transparency = 0
    munt.transparency = 0
def winst_berekening_function():
    global inzet
    global money
    global money_button
    global uitslag_tonen
    money+= inzet
    inzet *= 2
    money += inzet
    uitslag_tonen.hide()
    uitslag_tonen = play.new_text(f"Je hebt €{inzet},- erbij gekregen", font_size = 25, y = 100)
    uitslag_tonen.show()
    money_button.hide()
    money_button = play.new_text(f"{money}",color = 'black', font_size = 25, x = 280, y = 240, transparency=100)
    money_button.show()

@upgrade_1.when_clicked
async def buy_upgrade1():
    if upgrade_1.transparency == 100:  
        global gekocht_1
        global player
        if not gekocht_1:
            await koop_character(20)
            if gelukt == True:
                gekocht_1 = True
                player.hide()
                player= play.new_image("zwerverboi.png", size = 32, transparency = 0)
                player.show()
            else:
                niet_genoeg.transparency =100
                await play.timer(seconds = 2)
                niet_genoeg.transparency =0
        else:
            player.hide()
            player =play.new_image("zwerverboi.png", size = 32, transparency = 0)
            player.show()
@upgrade_2.when_clicked
async def buy_upgrade2():
    if upgrade_2.transparency == 100:
        global gekocht_2
        global player
        if not gekocht_2:
            await koop_character(80)
            if gelukt == True:
                gekocht_2 = True
                player.hide()
                player= play.new_image("niet meer straatarm.png", size = 10, transparency = 0)
                player.show()
            else:
                niet_genoeg.transparency =100
                await play.timer(seconds = 2)
                niet_genoeg.transparency =0
        else:
            player.hide()
            player= play.new_image("niet meer straatarm.png", size = 10, transparency = 0)
            player.show()
@upgrade_3.when_clicked
async def buy_upgrade3():
    if upgrade_3.transparency == 100:
        global gekocht_3
        global player
        if not gekocht_3:
            await koop_character(150)
            if gelukt == True:
                gekocht_3 = True
                player.hide()
                player= play.new_image("soort van rijk.png", size = 33, transparency = 0)
                player.show()
            else:
                niet_genoeg.transparency =100
                await play.timer(seconds = 2)
                niet_genoeg.transparency =0
        else:
            player.hide()
            player= play.new_image("soort van rijk.png", size = 33, transparency = 0)
            player.show()
@upgrade_4.when_clicked
async def buy_upgrade4():
    if upgrade_4.transparency == 100:
        global gekocht_4
        global player
        if not gekocht_4:
            await koop_character(250)
            if gelukt == True:
                gekocht_4 = True
                player.hide()
                player= play.new_image("best rijk.png", size = 30, transparency= 0)
                player.show()
            else:
                niet_genoeg.transparency =100
                await play.timer(seconds = 2)
                niet_genoeg.transparency =0
        else:
            player.hide()
            player = play.new_image("best rijk.png", size = 30, transparency= 0, x = 225, y = 30)
            player.show()
@upgrade_5.when_clicked
async def buy_upgrade5():
    if upgrade_5.transparency == 100:
        global gekocht_5
        global player
        if not gekocht_5:
            await koop_character(450)
            if gelukt == True:
                gekocht_5 = True
                player.hide()
                player= play.new_image("koning5.png", size = 12, transparency= 0)
                player.show()
            else:
                niet_genoeg.transparency =100
                await play.timer(seconds = 2)
                niet_genoeg.transparency =0
        else:
            player.hide()
            player= play.new_image("koning5.png", size = 12, transparency= 0)
            player.show() 
@upgrade_6.when_clicked
async def buy_upgrade6():
    if upgrade_6.transparency == 100:
        global gekocht_6
        global player
        if not gekocht_6:
            await koop_character(650)
            if gelukt == True:
                gekocht_6 = True
                player.hide()
                player=play.new_image("koning zes.png", size = 40, transparency=0)
                player.show()
            else:
                niet_genoeg.transparency =100
                await play.timer(seconds = 2)
                niet_genoeg.transparency =0
        else:
            player.hide()
            player=play.new_image("koning zes.png", size = 30, transparency= 0)
            player.show()
@upgrade_7.when_clicked
async def buy_upgrade7():
    if upgrade_7.transparency == 100:
        global gekocht_7
        global player
        if not gekocht_7:
            await koop_character(1000)
            if gelukt == True:
                gekocht_7 = True
                player.hide()
                player = play.new_image("7.png", size = 20, transparency= 0)
                player.show()
                player.angle  = 180
            else:
                niet_genoeg.transparency =100
                await play.timer(seconds = 2)
                niet_genoeg.transparency =0
        else:
            player.hide()
            player= play.new_image( "7.png",transparency= 0, size = 20)
            player.show()
            player.angle  = 180
@upgrade_8.when_clicked
async def buy_upgrade8():
    if upgrade_8.transparency == 100:
        global gekocht_8
        global player
        if not gekocht_8:
            await koop_character(2000)
            if gelukt == True:
                gekocht_8 = True
                player.hide()
                player = play.new_image( "8.png", size =20, transparency= 0)
                player.show()
                player.angle = 180
            else:
                niet_genoeg.transparency =100
                await play.timer(seconds = 2)
                niet_genoeg.transparency =0
        else:
            player.hide()
            player=play.new_image("8.png", size = 20, transparency= 0)
            player.show()
            player.angle = 180
async def koop_character(prijs):
    global money
    global gelukt
    global money_button
    if money > prijs:
        money -= prijs
        money_button.hide()
        money_button = play.new_text (f"{money}", color = 'black', font_size = 25, x = 280, y = 240, transparency=100)
        money_button.show()
        gelukt = True
    else:
        niet_genoeg.transparency=100
        await play.timer(seconds = 2)
        niet_genoeg.transparency=0
        gelukt = False
 
@play.repeat_forever
def stop_presstostart_function():
    if in_game == True:
        press_f_start_coinflip.hide()
        press_e_start_roulette.hide()
        press_g_start_slotmachine.hide()
 
play.start_program()