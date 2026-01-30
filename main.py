import os
import random
os.system("clear")

print("WORDLE TIME ;)")

word_list = ["ABOUT","ALERT","ARGUE","BEACH","ABOVE","ALIKE","ARISE","BEGAN","ABUSE","ALIVE","ARRAY","BEGIN","ACTOR","ALLOW","ASIDE","BEGUN","ACUTE","ALONE","ASSET","BEING","ADMIT","ALONG","AUDIO","BELOW","ADOPT","ALTER","AUDIT","BENCH","ADULT","AMONG","AVOID","BILLY","AFTER","ANGER","AWARD","BIRTH","AGAIN","ANGLE","AWARE","BLACK","AGENT","ANGRY","BADLY","BLAME","AGREE","APART","BAKER","BLIND","AHEAD","APPLE","BASES","BLOCK","ALARM","APPLY","BASIC","BLOOD","ALBUM","ARENA","BASIS","BOARD","BOOST","BUYER","CHINA","COVER","BOOTH","CABLE","CHOSE","CRAFT","BOUND","CALIF","CIVIL","CRASH","BRAIN","CARRY","CLAIM","CREAM","BRAND","CATCH","CLASS","CRIME","BREAD","CAUSE","CLEAN","CROSS","BREAK","CHAIN","CLEAR","CROWD","BREED","CHAIR","CLICK","CROWN","BRIEF","CHART","CLOCK","CURVE","BRING","CHASE","CLOSE","CYCLE","BROAD","CHEAP","COACH","DAILY","BROKE","CHECK","COAST","DANCE","BROWN","CHEST","COULD","DATED","BUILD","CHIEF","COUNT","DEALT","BUILT","CHILD","COURT","DEATH","DEBUT","ENTRY","FORTH","GROUP","DELAY","EQUAL","FORTY","GROWN","DEPTH","ERROR","FORUM","GUARD","DOING","EVENT","FOUND","GUESS","DOUBT","EVERY","FRAME","GUEST","DOZEN","EXACT","FRANK","GUIDE","DRAFT","EXIST","FRAUD","HAPPY","DRAMA","EXTRA","FRESH","HARRY","DRAWN","FAITH","FRONT","HEART","DREAM","FALSE","FRUIT","HEAVY","DRESS","FAULT","FULLY","HENCE","DRILL","FIBRE","FUNNY","NIGHT","DRINK","FIELD","GIANT","HORSE","DRIVE","FIFTH","GIVEN","HOTEL","DROVE","FIFTY","GLASS","HOUSE","DYING","FIGHT","GLOBE","HUMAN","EAGER","FINAL","GOING","IDEAL","EARLY","FIRST","GRACE","IMAGE","EARTH","FIXED","GRADE","INDEX","EIGHT","FLASH","GRAND","INNER","ELITE","FLEET","GRANT","INPUT","EMPTY","FLOOR","GRASS","ISSUE","ENEMY","FLUID","GREAT","IRONY","ENJOY","FOCUS","GREEN","JUICE","ENTER","FORCE","GROSS","JOINT","JUDGE","METAL","MEDIA","NEWLY","KNOWN","LOCAL","MIGHT","NOISE","LABEL","LOGIC","MINOR","NORTH","LARGE","LOOSE","MINUS","NOTED","LASER","LOWER","MIXED","NOVEL","LATER","LUCKY","MODEL","NURSE","LAUGH","LUNCH","MONEY","OCCUR","LAYER","LYING","MONTH","OCEAN","LEARN","MAGIC","MORAL","OFFER","LEASE","MAJOR","MOTOR","OFTEN","LEAST","MAKER","MOUNT","ORDER","LEAVE","MARCH","MOUSE","OTHER","LEGAL","MUSIC","MOUTH","OUGHT","LEVEL","MATCH","MOVIE","PAINT","LIGHT","MAYOR","NEEDS","PAPER","LIMIT","MEANT","NEVER","PARTY","PEACE","POWER","RADIO","ROUND","PANEL","PRESS","RAISE","ROUTE","PHASE","PRICE","RANGE","ROYAL","PHONE","PRIDE","RAPID","RURAL","PHOTO","PRIME","RATIO","SCALE","PIECE","PRINT","REACH","SCENE","PILOT","PRIOR","READY","SCOPE","PITCH","PRIZE","REFER","SCORE","PLACE","PROOF","RIGHT","SENSE","PLAIN","PROUD","RIVAL","SERVE","PLANE","PROVE","RIVER","SEVEN","PLANT","QUEEN","QUICK","SHALL","PLATE","SIXTH","STAND","SHAPE","POINT","QUIET","ROMAN","SHARE","POUND","QUITE","ROUGH","SHARP","SHEET","SPARE","STYLE","TIMES","SHELF","SPEAK","SUGAR","TIRED","SHELL","SPEED","SUITE","TITLE","SHIFT","SPEND","SUPER","TODAY","SHIRT","SPENT","SWEET","TOPIC","SHOCK","SPLIT","TABLE","TOTAL","SHOOT","SPOKE","TAKEN","TOUCH","SHORT","SPORT","TASTE","TOUGH","SHOWN","STAFF","TAXES","TOWER","SIGHT","STAGE","TEACH","TRACK","SINCE","STAKE","TEETH","TRADE","SIXTY","START","TEXAS","TREAT","SIZED","STATE","THANK","TREND","SKILL","STEAM","THEFT","TRIAL","SLEEP","STEEL","THEIR","TRIED","SLIDE","STICK","THEME","TRIES","SMALL","STILL","THERE","TRUCK","SMART","STOCK","THESE","TRULY","SMILE","STONE","THICK","TRUST","SMITH","STOOD","THING","TRUTH","SMOKE","STORE","THINK","TWICE","SOLID","STORM","THIRD","UNDER","SOLVE","STORY","THOSE","UNDUE","SORRY","STRIP","THREE","UNION","SOUND","STUCK","THREW","UNITY","SOUTH","STUDY","THROW","UNTIL","SPACE","STUFF","TIGHT","UPPER","UPSET","WHOLE","WASTE","WOUND","URBAN","WHOSE","WATCH","WRITE","USAGE","WOMAN","WATER","WRONG","USUAL","TRAIN","WHEEL","WROTE","VALID","WORLD","WHERE","YIELD","VALUE","WORRY","WHICH","YOUNG","VIDEO","WORSE","WHILE","YOUTH","VIRUS","WORST","WHITE","WORTH","VISIT","WOULD","VITAL","VOICE"]
secret = random.choice(word_list)



incorrect_letters = []
correct_letters = []
build = ["x","x","x","x","x"]

for i in range(5):

    guess = input("Please guess a 5 letter word. > ").upper()
    

    while len(guess) != 5:
        print("THATS NOT 5 LETTERS CHEATER")
        guess = input("Please guess a 5 letter word. > ").upper()
    while guess not in word_list:
        print("THAT IS NOT A VALID GUESS")
        guess = input("Please guess a 5 letter word. > ").upper()

    
    for i in range(len(build)):
        if secret[i] == guess[i]:
            build[i] = secret[i]
        elif guess[i] in secret and guess[i] not in correct_letters:
            correct_letters.append(guess[i])
        elif guess[i] not in secret and guess[i] not in incorrect_letters:
            incorrect_letters.append(guess[i])

    if "".join(build) != secret:
        
        print(f"\n \n NICE TRY! \n incorrect: {incorrect_letters}, \n correct: {correct_letters}")
        print(" CURRENT GUESS: ", "".join(build), " \n \n ")
    else:
        
        print("\n \n GOOD JOB YOU DID IT")
        print(f" SECRET WORD: {secret} \n \n")

    

print("TIMES OUT, TRY AGAIN TMW ;)")



