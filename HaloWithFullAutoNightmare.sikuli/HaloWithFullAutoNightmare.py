import random
MAX_SCROLL_TIME = 10
SUMMON_IMG = Pattern("SUMMON_IMG.png").similar(0.90)
SUMMON2_IMG = Pattern("SUMMON2_IMG.png").similar(0.90)
QUEST_BOOKMARK_IMG = Pattern("1612026925930.png").similar(0.85)
ITEM_BOOKMARK_IMG = Pattern("1612026966673.png").similar(0.90)
MAIN_EVENT_BOOKMARK_IMG = Pattern("MAIN_EVENT_BOOKMARK_IMG.png").similar(0.90)
NIGHTMARE_EVENT_BOOKMARK_IMG = Pattern("NIGHTMARE_EVENT_BOOKMARK_IMG.png").similar(0.90)
CONSUMABLES_ITEM_IMG = Pattern("1610791594396.png").similar(0.90)
AUTO_SELECT_IMG = Pattern("AUTO_SELECT_IMG.png").similar(0.90)
OK_IMG = Pattern("OK_IMG.png").similar(0.90)
QUEST_BUTTON_IMG = Pattern("QUEST_BUTTON_IMG.png").similar(0.90)
ATTACK_BUTTON_IMG = Pattern("ATTACK_BUTTON_IMG.png").exact()
ATTACK2_BUTTON_IMG = Pattern("ATTACK2_BUTTON_IMG.png").similar(0.90)
MC_AVATAR_IMG = Pattern("MC_AVATAR_IMG.png").similar(0.90)
DUAL_ARTS_SKILL_IMG = Pattern("DUAL_ARTS_SKILL.png").similar(0.90)
AURUM_FLOW_SKILL_IMG = Pattern("AURUM_FLOW_SKILL_IMG.png").similar(0.90)
STICKER_BUTTON_IMG = Pattern("STICKER_BUTTON_IMG.png").similar(0.90)
VERIFY_BUTTON_IMG = "1610788295895.png"
HOME_BUTTON_IMG = Pattern("HOME_BUTTON_IMG.png").similar(0.90)
CLAIM_BUTTON_IMG = Pattern("CLAIM_BUTTON_IMG.png").similar(0.90)
VYRN_IMG = Pattern("VYRN_IMG.png").similar(0.90)
HALF_ELIXIR_IMG = Pattern("1610791829494.png").similar(0.90)
FULL_ELIXIR_IMG = Pattern("FULL_ELIXIR_IMG.png").similar(0.90)
USE_BUTTON_IMG = Pattern("USE_BUTTON_IMG.png").similar(0.90)
QUEST_RESULTS_IMG = Pattern("QUEST_RESULTS_IMG.png").similar(0.90)
NIGHTMARE_QUEST_IMG = Pattern("NIGHTMARE_QUEST_IMG.png").similar(0.90)

X_RANGE = 7;
Y_RANGE = 7;

WAIT_TIME_RANGE = 500.0
MAX_ERROR_COUNT = 1
MAX_HALF_ELIXIR = 1000
MAX_FULL_ELIXIR = 1000
LOAD_BATTLE_TIME = 9
LOAD_PARTY_TIME = 3
LOAD_POPUP_QUEST_TIME = 3
LOAD_CHARACTER_SKILL_TIME = 2
LOAD_QUEST_TIME = 9
LOAD_ITEM_PAGE_TIME = 9
LOAD_ITEM_TIME = 3
LOAD_QUEST_RESULTS_TIME = 100
LOAD_MAIN_EVENT_TIME = 9
START_ATTACK_TIME = 6
CHECK_VERIFY_BUTTON_TIME = 1
BASE_TIME_WAIT = 0.0
BROWSER_APP_NAME = "Microsoft Edge"

def clickRandom(region, match):
    location = match.getTarget()
    region.click(location.offset(random.randrange(-X_RANGE, X_RANGE), random.randrange(-Y_RANGE, Y_RANGE))) 

def waitRandom(time_wait):
    sleep((time_wait + random.randrange(WAIT_TIME_RANGE))/1000)

def skipNightmareQuest():
    global error_count

    if (not region.exists(NIGHTMARE_QUEST_IMG)):
        error_count += 1
        return
    waitRandom(BASE_TIME_WAIT)        
    clickRandom(region, region.getLastMatch())
    
    if (not region.exists(CLAIM_BUTTON_IMG, LOAD_POPUP_QUEST_TIME)):
        error_count += 1
        return
    waitRandom(BASE_TIME_WAIT)        
    clickRandom(region, region.getLastMatch())

    if (not region.exists(QUEST_RESULTS_IMG, LOAD_QUEST_RESULTS_TIME)):
        error_count += 1
        return
    waitRandom(BASE_TIME_WAIT)
    startQuest()

def fullAutoNightmareQuest():
    global error_count

    if (not region.exists(NIGHTMARE_EVENT_BOOKMARK_IMG)):
        error_count += 1
        return            
    waitRandom(BASE_TIME_WAIT)        
    clickRandom(region, region.getLastMatch())

    if (not region.exists(VYRN_IMG, LOAD_QUEST_TIME)):
        error_count += 1
        return
    waitRandom(BASE_TIME_WAIT)        

    if (region.exists(VERIFY_BUTTON_IMG, CHECK_VERIFY_BUTTON_TIME)):
        print(6)
        waitRandom(BASE_TIME_WAIT)        
        clickRandom(region, region.getLastMatch())
            
    #SCROLL FIND SUMMON
    scroll_count = 0
    while (not region.exists(SUMMON2_IMG, 0)):
        type(Key.DOWN)
        waitRandom(BASE_TIME_WAIT)
        scroll_count += 1
        if (scroll_count >= MAX_SCROLL_TIME): 
            return   
    waitRandom(BASE_TIME_WAIT)    
    clickRandom(region, region.getLastMatch())
            
    if (not region.exists(OK_IMG, LOAD_PARTY_TIME)):
        error_count += 1
        return 
    waitRandom(BASE_TIME_WAIT)        
    clickRandom(region, region.getLastMatch())

    if (region.exists(QUEST_BUTTON_IMG)):
        refillAP()
        return

    if (not region.exists(ATTACK2_BUTTON_IMG, LOAD_BATTLE_TIME)):
        error_count += 1
        return
        
    waitRandom(BASE_TIME_WAIT)
    clickRandom(region, region.getLastMatch())

    if (not region.exists(QUEST_RESULTS_IMG, LOAD_QUEST_RESULTS_TIME)):
        error_count += 1
        return
    waitRandom(BASE_TIME_WAIT)    

def refillAP():
    global half_elixir_count
    global full_elixir_count
    global error_count
    
    if (not region.exists(ITEM_BOOKMARK_IMG)):
        error_count += 1
        return            
    waitRandom(BASE_TIME_WAIT)        
    clickRandom(region, region.getLastMatch())

    if (not region.exists(CONSUMABLES_ITEM_IMG, LOAD_ITEM_PAGE_TIME)):
        error_count += 1
        return            
    waitRandom(1500)        
    clickRandom(region, region.getLastMatch())
    
    if half_elixir_count < MAX_HALF_ELIXIR:
        if (not region.exists(HALF_ELIXIR_IMG, LOAD_ITEM_TIME)):
            error_count += 1
            return            
        waitRandom(BASE_TIME_WAIT)        
        clickRandom(region, region.getLastMatch())
    else:    
        if full_elixir_count < MAX_FULL_ELIXIR:
           if (not region.exists(FULL_ELIXIR_IMG, LOAD_ITEM_TIME)):
                error_count += 1
                return            
           waitRandom(BASE_TIME_WAIT)        
           clickRandom(region, region.getLastMatch())
            
    if (not region.exists(USE_BUTTON_IMG)):
        error_count += 1
        return            
    waitRandom(BASE_TIME_WAIT)        
    clickRandom(region, region.getLastMatch())
    startQuest()
    
def startQuest():
    global error_count
    
    if (not region.exists(QUEST_BOOKMARK_IMG)):
        error_count += 1
        return            
    waitRandom(BASE_TIME_WAIT)        
    clickRandom(region, region.getLastMatch())

    if (not region.exists(VYRN_IMG, LOAD_QUEST_TIME)):
        error_count += 1
        return
    waitRandom(BASE_TIME_WAIT)        

    if (region.exists(VERIFY_BUTTON_IMG, CHECK_VERIFY_BUTTON_TIME)):
        print(6)
        waitRandom(BASE_TIME_WAIT)        
        clickRandom(region, region.getLastMatch())
            
    #SCROLL FIND SUMMON
    scroll_count = 0
    while (not region.exists(SUMMON_IMG, 0)):
        type(Key.DOWN)
        waitRandom(BASE_TIME_WAIT)
        scroll_count += 1
        if (scroll_count >= MAX_SCROLL_TIME): 
            return   
    waitRandom(BASE_TIME_WAIT)    
    clickRandom(region, region.getLastMatch())
            
    if (not region.exists(OK_IMG, LOAD_PARTY_TIME)):
        error_count += 1
        return 
    waitRandom(BASE_TIME_WAIT)        
    clickRandom(region, region.getLastMatch())

    if (region.exists(QUEST_BUTTON_IMG)):
        refillAP()
        return

    if (not region.exists(ATTACK_BUTTON_IMG, LOAD_BATTLE_TIME)):
        error_count += 1
        return
        
    waitRandom(BASE_TIME_WAIT)
    clickRandom(region, region.getLastMatch())

    if (not region.exists(QUEST_RESULTS_IMG, LOAD_QUEST_RESULTS_TIME)):
        error_count += 1
        return
    waitRandom(BASE_TIME_WAIT)

    if (not region.exists(MAIN_EVENT_BOOKMARK_IMG)):
        error_count += 1
        return
    waitRandom(BASE_TIME_WAIT)        
    clickRandom(region, region.getLastMatch())

    if (not region.exists(HOME_BUTTON_IMG, LOAD_MAIN_EVENT_TIME)):
        error_count += 1
        return
    waitRandom(BASE_TIME_WAIT)        

    if (region.exists(NIGHTMARE_QUEST_IMG, 1)):
        fullAutoNightmareQuest()
        return 

### MAIN CODE ###
app = App(BROWSER_APP_NAME)
region = app.focusedWindow()
Settings.MoveMouseDelay = 0
Settings.ObserveScanRate = 10
error_count = 0
half_elixir_count = 0
full_elixir_count = 0
while (True):   
    startQuest()
    if (error_count >= MAX_ERROR_COUNT or (half_elixir_count >= MAX_HALF_ELIXIR and full_elixir_count >= MAX_FULL_ELIXIR)):
        break
        

