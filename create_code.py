import time

#save/load I/O

def SaveGame(filename):
    save_file = open('{}.txt'.format(filename),'w')
    save_file.write(password)
    save_file.close()
def LoadGame(x):
    load_file = open(x, "r")
    load_file = load_file.read()
    password = load_file
    if password == 'AAAA':
        print('Type in slumbering_wood() to restore your progress!')
    elif password == 'AAAB':
        print('Type in slumbering_wood_LEFT_DONE() to restore your progress!')
    elif password == 'AABA':
        print('Type in slumbering_wood_COMPLETE() to restore your progress!')
    elif password == 'BBBB':
        print('Type tree_stump_path() to restore your progress!')
    elif password == 'BBBA':
        print('Type tree_stump_path_NO_AXE() to restore your progress!')
    elif password == 'BBAB':
        print('Type tree_stump_path_COMPLETE() to restore your progress!')
    elif password == 'CCCC':
        print('Type wild_path() to restore your progress!')
    elif password == 'CCCA':
        print('Type wild_path_NO_SWORD() to restore your progress!')
    elif password == 'CCAC':
        print('Type wild_path_NO_TORCH() to restore your progress!')
    elif password == 'CCAA':
        print('Type wild_path_COMPLETE() to restore your progress!')
    elif password == 'CAAA':
        print('Type wild_path_NO_ITEMS() to restore your progress!')
    else:
        print('Your save file could not be read.')

inventory = []       

#function for room inventory management

def get(x):
    inventory.append(x)
    return inventory

#intro text, name input, game over

print('Type intro() to begin the game; to load a saved game,\nuse the function LoadGame("x.txt") using your saved filename\nas "x" to restore your state.')

def intro():
    print("Welcome to Serf's Quest! You, a lowly peasant, must traverse the Slumbering Wood\nto the cave of Dargon the Dragon, and slay him.")
    print("It is a text based adventure where you input your commands!\nIf confused at any point during gameplay, type HELP on THIS title screen; instructions will appear!\nFor info. on loading and saving a file, see HELP command for more!")
    command = input("Would you like to play? Input PLAY or NO!\n\nWhat do thou want to do?> ")
    if command.lower().strip() == 'help':
        print('instructions: type what you want to do.\nImportant words are the all caps ones; type them in verbatim for the commands to work;\ncapitalization or punctuation of your inputs does not matter.\n')
        command = input('What dost thou want to do?> ')
    if command.lower().strip() == 'play':
        game_intro()
    elif command.lower().strip() == 'no':
        
        exit()
    else:
        print("I didn't recognize your command. Type HELP while on the intro text for information.")
            
def game_intro():
    print('\n*After a long day of working the field for thoust king, thou return to\nthine cottage and thou seest with rage the smoldering ashes of where thine cottage once stood.')
    print('Observing the ruins, thou notice unmistakable footprints -- the footprints of the terrible Dargon.\nThou knowest what thou must do -- thou must go slay the terrible dragon, Dargon.')
    print('Thou vow, "Dargon will perish by my hand! I, er... what is mine name again?"')
    player = input("\nWhat is thine name?> ")
    print('\n*"Ah, yes, I,', player, 'will vanquish the terrible dragon, Dargon,\nbe it the last thing I do!"')
    print('*Fortunately, thine cottage is a mere 5 minute stroll from the\nforest that houses the cave that, in turn, houses the fearsome Dargon.')
    print('Perhaps this has something to do with the torching of thine cottage; disregarding this matter, thou, %s, press onto the mouth of the Slumbering Wood.\n'%player)
    slumbering_wood()

def game_over():
    print('*Thou have perished! Thine deeds will be remembered throughout the ages.')
    print('REST IN PEACE, FOR THINE QUEST HAS TRAGICALLY ENDED!')
    time.sleep(10)
    exit()

def game_won():
    print('*Congratulations! Thou have survived thine ordeal. While Dargon lives, so do you, and, being honest, that is the best possible outcome for thou given thine quest.')
    print('LIVE IN PEACE, FOR THINE QUEST IS SURVIVED!')
    time.sleep(10)
    exit()

#Area 1 and variations: slumbering wood

def slumbering_wood():
    global password
    password = 'AAAA'
    print('*Upon reaching the entrance of the Slumbering Wood, thou observe three paths, all carrying some distinctions...')
    print("*To thine left, thou seest a short, short path; so short, in fact, thou can see the end of the path from where thou are standing.\nIt ends with a small tree stump. Thou note it as the TREE STUMP PATH.")
    print("*Directly in front of thou, thou seest a dark and winding path with no end in sight... \ncertainly a departure from the shorter path on thine left. Thou note it as the DARK PATH.")
    print("*And finally, to thine right, you see a jagged path that seems to veer off in many directions. \nThe foilage is thick; though it is far brighter than the middle path. Thou note this as the WILD PATH.\n")
    command = input("Where wouldst thou wish to go?> ")
    if command.lower().strip() == 'tree stump path':
        tree_stump_path()
    elif command.lower().strip() == 'dark path':
        print('*Thou realize, upon taking a few steps down this path, thou cannot see two feet in front of thou. Thou will need some lighting to traverse this path.')
        slumbering_wood()
    elif command.lower().strip() == 'wild path':
        wild_path_NO_ITEMS()
    elif command.lower().strip() == 'save':
        filename = input('What wouldst thou like to name thine file?> ')
        SaveGame(filename)
        slumbering_wood()
    else:
        print("I didn't recognize your command. Type HELP for help.")
        slumbering_wood()

def slumbering_wood_LEFT_DONE():
    global password
    password = 'AAAB'
    print('*Upon reaching the entrance of the Slumbering Wood, thou observe three paths, all carrying some distinctions...')
    print("*To thine left, thou seest a short, short path; so short, in fact, thou can see the end of the path from where thou are standing.\nIt ends with a small, newly split stump.")
    print("*Directly in front of thou, thou seest a dark and winding path with no end in sight... \ncertainly a departure from the shorter path on thine left. Thou note it as the DARK PATH.")
    print("*And finally, to thine right, you see a jagged path that seems to veer off in many directions. \nThe foilage is thick; though it is far brighter than the middle path. Thou note this as the WILD PATH.\n")
    command = input("Where wouldst thou wish to go?> ")
    if command.lower().strip() == 'tree stump path':
        print('Thou realize that thou has nothing left to do on that path, and decide to go somewhere more useful with thine time.')
        slumbering_wood_LEFT_DONE()
    elif command.lower().strip() == 'dark path':
        print('*Thou realize, upon taking a few steps down this path, thou cannot see two feet in front of thou. Thou will need some lighting to traverse this path.')
        slumbering_wood_LEFT_DONE()
    elif command.lower().strip() == 'wild path':
        wild_path()
    elif command.lower().strip() == 'save':
        filename = input('What wouldst thou like to name thine file?> ')
        SaveGame(filename)
        slumbering_wood_LEFT_DONE()
    else:
        print("I didn't recognize your command. Type HELP for help.")
        slumbering_wood_LEFT_DONE()

def slumbering_wood_COMPLETE_SAVE():
    global password
    password = 'AABA'
    print('*Upon reaching the entrance of the Slumbering Wood, thou observe three paths, all carrying some distinctions...')
    print('*(This is your last chance to save. Save now?)')
    command = input('YES or NO?> ')
    if command.lower().strip() == 'yes':
        filename = input('What wouldst thou like to name thine file?> ')
        SaveGame(filename)
    elif command.lower().strip() == 'no':
        print('*Very well... in that case...')
    elif command.lower().strip()!=('yes' or 'no'):
        print("I didn't recognize your command. Type HELP for help.")
        slumbering_wood_COMPLETE_SAVE()
    print('*The DARK PATH beckons...')
    command = input('\nArt thou ready? YES or NO?> ')
    if command.lower().strip() == 'no':
        print('Seriously? But thou must!')
        print("Let's try that once more...")
        slumbering_wood_COMPLETE_SAVE()
    elif command.lower().strip() == 'yes':
        dark_path()
    elif command.lower().strip()!= ('yes' or 'no'):
        print("I didn't recognize your command. Type HELP for help.")
        slumbering_wood_COMPLETE_SAVE()

def slumbering_wood_COMPLETE():
    print('*Upon reaching the entrance of the Slumbering Wood, thou observe three paths, all carrying some distinctions...')
    print('*The DARK PATH beckons...')
    dark_path()
    
#Area 2 and variations - tree stump        

def tree_stump_path():
    global password
    password = 'BBBB'
    print('\n*There is not much of note down the tree stump path; aside from some dead TREES, and the elusive STUMP.')
    command = input("\nWhat wouldst thou check?> ")
    if command.lower().strip() == 'trees':
        print('*What luck! Wedged into a dead tree is a dull, but usable axe. Thou take the axe.')
        get('*axe')
        tree_stump_path_NO_AXE()
    if command.lower().strip() == 'stump':
        print('*It is a very weathered tree stump. Thou see SOMETHING GLISTENING in the tree stump; thou considers to LEAVE as well.')
        command = input('\nWhat dost thou want to do?> ')
        if command.lower().strip() == "something glistening":
            print("*Thou seest ye flask. Thou can GET ye flask, or LEAVE.")
            command = input('\nWhat dost thou want to do?> ')
            if command.lower().strip() == 'get':
                if '*axe' not in inventory:
                    print('*Thou cannot, at the moment, get ye flask. It is wedged deeply inside a stump, which used to be a tree, which is rooted firmly in the Earth around it.\nThou can leave now.')
                    tree_stump_path()
                elif '*axe' in inventory and '*flask' not in inventory:
                    print("*With one fell axe swoop, ye split the stump and retrive ye flask. It seems to be filled with a potion of some sort;\nyou drink it, and are filled with an overwhelming feeling of strength.\n'Dargon... I'm coming...' thou mutter to nobody in particular.")
                    get('*flask')
                    tree_stump_path()
            elif command.lower().strip() == 'leave':
                tree_stump_path()
            elif command.lower().strip() == 'save':
                filename = input('What wouldst thou like to name thine file?> ')
                SaveGame(filename)
                tree_stump_path()
            elif command.lower().strip()!= ('get' or 'leave' or 'save'):
                print("I didn't recognize your command. Type HELP while on the intro text for information.")
                tree_stump_path()
        elif command.lower().strip() == 'leave':
            tree_stump_path()
        elif command.lower().strip() == 'save':
            filename = input('What wouldst thou like to name thine file?> ')
            SaveGame(filename)
            tree_stump_path()
        else:
            print("I didn't recognize your command. Type HELP while on the intro text for information.")
            tree_stump_path()
    elif command.lower().strip() == 'save':
        filename = input('What wouldst thou like to name thine file?> ')
        SaveGame(filename)
        tree_stump_path()
    else:
        print("I didn't recognize your command. Type HELP while on the intro text for information.")
        tree_stump_path()

def tree_stump_path_NO_AXE():
    global password
    password = 'BBBA'
    print('\n*There is not much of note down the tree stump path; aside from some dead TREES, and the elusive STUMP.')
    command = input("\nWhat wouldst thou check?> ")
    if command.lower().strip() == 'trees':
        print('*There seems to be nothing else of note amongst the dead trees.')
        tree_stump_path_NO_AXE()
    if command.lower().strip() == 'stump':
        print('*It is a very weathered tree stump. Thou see SOMETHING GLISTENING in the tree stump; thou considers to LEAVE as well.')
        command = input('\nWhat dost thou want to do?> ')
        if command.lower().strip() == "something glistening":
            print("*Thou seest ye flask. Thou can GET ye flask, or LEAVE.")
            command = input('\nWhat dost thou want to do?> ')
            if command.lower().strip() == 'get':
                if '*axe' not in inventory:
                    print('*Thou cannot, at the moment, get ye flask. It is wedged deeply inside a stump, which used to be a tree, which is rooted firmly in the Earth around it.\nThou can leave now.')
                    tree_stump_path_NO_AXE()
                elif '*axe' in inventory and '*flask' not in inventory:
                    print("*With one fell axe swoop, ye split the stump and retrive ye flask. It seems to be filled with a potion of some sort;\nyou drink it, and are filled with an overwhelming feeling of strength.\n'Dargon... I'm coming...' thou mutter to nobody in particular.")
                    get('*flask')
                    tree_stump_path_COMPLETE()
            elif command.lower().strip() == 'leave':
                tree_stump_path_NO_AXE()
            elif command.lower().strip() == 'save':
                filename = input('What wouldst thou like to name thine file?> ')
                SaveGame(filename)
                tree_stump_path_NO_AXE()
            else:
                print("I didn't recognize your command. Type HELP while on the intro text for information.")
                tree_stump_path_NO_AXE()
        elif command.lower().strip() == 'leave':
                tree_stump_path_NO_AXE()
        elif command.lower().strip() == 'save':
            filename = input('What wouldst thou like to name thine file?> ')
            SaveGame(filename)
            tree_stump_path_NO_AXE()
        else:
            print("I didn't recognize your command. Type HELP while on the intro text for information.")
            tree_stump_path_NO_AXE()
    elif command.lower().strip() == 'save':
        filename = input('What wouldst thou like to name thine file?> ')
        SaveGame(filename)
        tree_stump_path_NO_AXE()
    else:
        print("I didn't recognize your command. Type HELP while on the intro text for information.")
        tree_stump_path_NO_AXE()

def tree_stump_path_COMPLETE():
    global password
    password = 'BBAB'
    print('\n*There is not much of note down the tree stump path; aside from some dead TREES, and the elusive STUMP. The ENTRANCE beckons thou from mere yards behind.')
    command = input("\nWhat wouldst thou check?> ")
    if command.lower().strip() == 'trees':
        print('*There seems to be nothing else of note amongst the dead trees.')
        tree_stump_path_COMPLETE()
    if command.lower().strip() == 'stump':
        print('*There is now just a stump with a large gash down the middle; thou considers to LEAVE.')
        command = input('\nWhat dost thou want to do?> ')
        if command.lower().strip() == "leave":
            tree_stump_path_COMPLETE()
        elif command.lower().strip() == 'save':
            filename = input('What wouldst thou like to name thine file?> ')
            SaveGame(filename)
            tree_stump_path_COMPLETE()
        else:
            print("I didn't recognize your command. Type HELP while on the intro text for information.")
            tree_stump_path_COMPLETE()
    elif command.lower().strip() == 'entrance':
        slumbering_wood_LEFT_DONE()
    elif command.lower().strip() == 'save':
        filename = input('What wouldst thou like to name thine file?> ')
        SaveGame(filename)
        tree_stump_path_COMPLETE()
    else:
        print("I didn't recognize your command. Type HELP while on the intro text for information.")
        tree_stump_path_COMPLETE()

#area 3 and variations: wild path

def wild_path():
    global password
    password = 'CCCC'
    print('*Walking this scraggly path thou seest a CHEST; sitting a few yards away from the chest is a small rocky ALCOVE. There is light escaping the alcove...')
    command = input('\nWhat wouldst thou check?> ')
    if command.lower().strip() == 'chest':
        print('*Though the hinges are rusted and stiff, with a great heave thou flingst open the chest. Thou discover a sword inside; which, thou, then, equip.\nThou wonder how thy intended to slay Dargon barehanded to begin with.')
        wild_path_NO_SWORD()
    elif command.lower().strip() == 'alcove':
        print('*Wandering under the alcove, thou discover a torch! Alongside the remains of several scorched human remains.\nThou tear the torch from the wall and equip it, unsure if the remains are victims of Dargon or stupidity.')
        wild_path_NO_TORCH()
    elif command.lower().strip() == 'save':
        filename = input('What wouldst thou like to name thine file?> ')
        SaveGame(filename)
        wild_path()
    else:
        print("I didn't recognize your command. Type HELP while on the intro text for information.")
        wild_path()

def wild_path_NO_SWORD():
    global password
    password = 'CCCA'
    print('*Walking this scraggly path thou seest a CHEST; sitting a few yards away from the chest is a small rocky ALCOVE. There is light escaping the alcove...')
    command = input('\nWhat wouldst thou check?> ')
    if command.lower().strip() == 'chest':
        print('*If thou wishes to kill Dargon, perhaps, thou thinks, that wasting time rechecking empty chests is, at its best, a waste of time.')
        wild_path_NO_SWORD()
    elif command.lower().strip() == 'alcove':
        print('*Wandering under the alcove, thou discover a torch! Alongside the remains of several scorched human remains.\nThou tear the torch from the wall and equip it, unsure if the remains are victims of Dargon or stupidity.')
        wild_path_COMPLETE()
    elif command.lower().strip() == 'save':
        filename = input('What wouldst thou like to name thine file?> ')
        SaveGame(filename)
        wild_path_NO_SWORD()
    else:
        print("I didn't recognize your command. Type HELP while on the intro text for information.")
        wild_path_NO_SWORD()

def wild_path_NO_TORCH():
    global password
    password = 'CCAC'
    print('*Walking this scraggly path thou seest a CHEST; sitting a few yards away from the chest is a small rocky ALCOVE.')
    command = input('\nWhat wouldst thou check?> ')
    if command.lower().strip() == 'chest':
        print('*Though the hinges are rusted and stiff, with a great heave thou flingst open the chest. Thou discover a sword inside; which, thou, then, equip.\nThou wonder how thy intended to slay Dargon barehanded to begin with.')
        wild_path_COMPLETE()
    elif command.lower().strip() == 'alcove':
        print('*Wandering under the alcove, thou discover... nothing thou missed the first time!\nPerhaps thou should be concerned with thine OWN safety when using that torch...')
        wild_path_NO_TORCH()
    elif command.lower().strip() == 'save':
        filename = input('What wouldst thou like to name thine file?> ')
        SaveGame(filename)
        wild_path_NO_TORCH()
    else:
        print("I didn't recognize your command. Type HELP while on the intro text for information.")
        wild_path_NO_TORCH()

def wild_path_COMPLETE():
    global password
    password = 'CCAA'
    print('*Walking this scraggly path thou seest a CHEST; sitting a few yards away from the chest is a small rocky ALCOVE. The ENTRANCE looms behind thou.')
    command = input('\nWhat wouldst thou check?> ')
    if command.lower().strip() == 'chest':
        print('*If thou wishes to kill Dargon, perhaps, thou thinks, that wasting time rechecking empty chests is, at its best, a waste of time.')
        wild_path_COMPLETE()
    elif command.lower().strip() == 'alcove':
        print('*Wandering under the alcove, thou discover... nothing thou missed the first time!\nPerhaps thou should be concerned with thine OWN safety when using that torch...')
        wild_path_COMPLETE()
    elif command.lower().strip() == 'entrance':
        slumbering_wood_COMPLETE_SAVE()
    elif command.lower().strip() == 'save':
        filename = input('What wouldst thou like to name thine file?> ')
        SaveGame(filename)
        wild_path_COMPLETE()
    else:
        print("I didn't recognize your command. Type HELP while on the intro text for information.")
        wild_path_COMPLETE()

def wild_path_NO_ITEMS():
    global password
    password = 'CAAA'
    print('*Walking this scraggly path thou seest a CHEST; sitting a few yards away from the chest is a small rocky ALCOVE. The ENTRANCE looms behind thou.')
    command = input('\nWhat wouldst thou check?> ')
    if command.lower().strip() == 'chest':
        print('*Thou lack the upper body strength to open the chest; thou art but a weak peasant.')
        wild_path_NO_ITEMS()
    elif command.lower().strip() == 'alcove':
        print('*Wandering under the alcove, thou discover... a torch! Thou art too feeble to remove the torch from the wall.')
        wild_path_NO_ITEMS()
    elif command.lower().strip() == 'entrance':
        slumbering_wood()
    elif command.lower().strip() == 'save':
        filename = input('What wouldst thou like to name thine file?> ')
        SaveGame(filename)
        wild_path_NO_ITEMS()
    else:
        print("I didn't recognize your command. Type HELP while on the intro text for information.")
        wild_path_NO_ITEMS()

#areas 4, 5 -- Dark Path, Dargon's Cave
def dark_path():
    print('*With thine torch and sword in hand, thou, venture bravely into the dark woods...')
    print('Thine torch illuminating thine way, thou are filled with a newfound confidence and assuredness marching toward Dargon...')
    print('*And marching... and marching... hey, art thou lost...? Dost thou turn LEFT or RIGHT at thine next fork in the road?')
    command = input('\nWhich direction dost thou go?> ')
    if command.lower().strip() == 'left':
        print('*I knew it; thou ART lost. After wandering through the darkness for an extended time, thou wander out of the woods and stumble once again on the mouth of the woods...')
        slumbering_wood_COMPLETE()
    elif command.lower().strip() == 'right':
        print('*I knew it; thou ART lost. Despite this, after wandering through the darkness for an extended time, thou wander into another fork in the road... LEFT, RIGHT, or STRAIGHT?')
        command = input("\nWhat direction dost thou go?> ")
        if command.lower().strip() == 'left':
            print('*I knew it; thou ART lost. After wandering through the darkness for an extended time, thou wander out of the woods and stumble once again on the mouth of the woods...')
            slumbering_wood_COMPLETE()
        elif command.lower().strip() == 'straight':
            print('*I knew it; thou ART lost. After wandering through the darkness for an extended time, thou wander out of the woods and stumble once again on the mouth of the woods...')
            slumbering_wood_COMPLETE()
        elif command.lower().strip() == 'right':
            print('*Thou have an exceptional internal sense of navigation; never have thou had reason to doubt it, and thine confidence only grows as the path continues winding...')
            print('*Most unfortunately, you begin stumbling across charred bodies; telltale signs of Dargon nearby...')
            print('*Thou stumble across not one, but two caverns, both side by side, both emblazoned with "DAGRON" crudely carved above each... one on the LEFT, one on the RIGHT.')
            print("*'C'mon, internal navigator, I need thou now more than ever...' thou think.")
            command = input('\nWhich direction dost thou go?> ')
            if command.lower().strip() == 'left':
                print('*Alas! Thou fall in a pit... which seems to have no bottom... or at least a very, very deep one.\nThou, unfortunately, starve on the fall before what can only be presumed to end in an eventual splat...')
                print('*Thou art falling...')
                i = 0
                while i<5:
                    i = i+1
                    time.sleep(2)
                    print('*And falling... and...')
                else:
                    game_over()
            elif command.lower().strip() == 'right':
                print('*Aha! In step with thine amazing internal compass, thou have been smiled upon by fortune and chosen the true cave of the fierce Dargon.\n Now, thou must venture deeper... and slay Dargon.')
                dargon_cave()
            else:
                print("In thine confusion and misdirected input, thou find thineself back at the entrance of the path...")
                dark_path()
        else:
            print("In thine confusion and misdirected input, thou find thineself back at the entrance of the path...")
            dark_path()
    else:
        print("In thine confusion and misdirected input, thou find thineself at the entrance of the path...")
        dark_path()
                
def dargon_cave():
    print('*The lair of thine enemy... Dargon. Art thou prepared?')
    command = input('YEA or NAY?> ')
    print('*Great! Thine enemy approaches with each step thou takest into the den...')
    time.sleep(2)
    print('*Closer...')
    time.sleep(2)
    print('*Clooooser...')
    time.sleep(4)
    print('*And thine foe is confronting thee!\nThou have but an instant before Dargon is upon thee, claws outstretched. Will thy DEFLECT the oncoming blow, or attempt to STRIKE?')
    command = input('\nWhat will thou do?> ')
    if command.lower().strip() == 'strike':
        print('*Thou attempt to swing thine sword into the fierce beast; however, Dargon pierces thine heart with a claw before the swing is finished. Thou art very dead.')
        game_over()
    elif command.lower().strip() == 'deflect':
        print('*Thine sharp wit is sharper than the oncoming claws; thou deflect the blow deftly.\n*Now is thine chance! Will thou DISCUSS thine issues with the beast, or STAB it in the neck?')
        command = input('\nWhat will thou do?> ')
        if command.lower().strip() == 'discuss':
            print('*Strangely, Dargon does not seem much for talking at the moment. Midway through thine first word, thou art burned to a crisp. Needless to say, thou art dead.')
            game_over()
        elif command.lower().strip() == 'stab':
            print('*With great vigor and gusto, thou stab the beast in the neck fiercly! Dargon stumbles...')
            time.sleep(3)
            print('*And begins, "I am in absolute shock. A peasant actually stuck me one!" Dargon then plucks the sword from his neck.\n"Honestly, I am astounded! Nobody -- knights, peasants, N-O-B-O-D-Y has actually ever got me like that!')
            print('*"Good for you, little peasant. For that, I will let you WALK AWAY with your life. Or we can go the OTHER ROUTE... well, whaddya say, little guy?')
            command = input('\nWell, what now, genius?> ')
            if command.lower().strip() == 'walk away':
                print('*It cannot be called cowardice if it is really the only option thou havest left... So, thou bailed. And escaped with thine life!')
                game_won()
            elif command.lower().strip() == 'other route':
                print('*"AH, I was JUST HOPING you would say that!"')
                time.sleep(4)
                print('*Well, what did thou think would happen? No doubt, thou will have much time to reflect from within the belly of Dargon... at least thou died standing by thine word.')
                game_over()
            else:
                print("I didn't recognize your command. Unfortunately, Dargon did not take the time to wait for thou to decide what to do, and incinerated you amidst the confusion. Thou art dead.")
                game_over()
        else:
            print("I didn't recognize your command. Unfortunately, Dargon did not take the time to wait for thou to decide what to do, and incinerated you amidst the confusion. Thou art dead.")
            game_over()
    else:
        print("I didn't recognize your command. Unfortunately, Dargon did not take the time to wait for thou to decide what to do, and incinerated you amidst the confusion. Thou art dead.")
        game_over()
    
          

                
    
