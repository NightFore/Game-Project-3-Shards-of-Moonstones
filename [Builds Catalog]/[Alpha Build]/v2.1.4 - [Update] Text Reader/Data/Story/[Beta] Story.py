def Game_Intro_1()
    # OST
    pygame.mixer.music.load(Serenity)
    pygame.mixer.music.play(-1)

    gameExit = False
    while not gameExit:
        events = pygame.event.get()
        pygame.display.update()
        
        # Setup
        GameStateReset("All")
        Story_Event()
        Text_Input(events)
        
        # Background
        gameDisplay.blit(Background_Introduction, 0,0)
    
        # Story
        Wake up young child...

        Huh...? Where am I?

        Tell me your name.
        And maybe I can answer you.

            (Enter Character Name)

        That doesn't seem like a real name!
        Please, tell me your name!

        My name is %s.

        I see... You're %s...
        So my new Summon name is %s

        Wh... What do you mean?"

        It means that I will look after you.
        But you will also have to obey me.
        I hope you won't disappoint me.
        I will send you off to accomplish // a important mission.

        So what is that mission?"

        You don't have to know about it.
        You will understand when you will // have to do when you confront her.

        You're going to fall asleep now.




        for event in events:
            if event.type == pygame.QUIT:
                exit()


    # Game Intro 2
# Background
Black_Screen
Background_House

# OST
Around_a_Campfire

# Story
    (Background_House)

1 Week Later...

Hm... Huh... What's happening?
It's been noisy for a while now.
I probably should go check out // what's happening outside."

GameStateIG.Game_Progress == 0





    # GameStateIG.Game_Progress == 1
# Background
Background_Fight

# OST
Fight_1_1_Fierce_Riposte

# Enemy List
Wolf LvL 1

# Introduction
    (Wolf Howl)
Wow! What was that?
Wasn't that a Monster just now?
Here he is!

# Victory
What was a Monster doing here?
Something must've happened to // the village.
I wonder if they are all safe...
I should prepare myself for a fight.

Results_Screen()








    # Main_Menu
# Background
Background_Main_Menu_1
Background_Main_Menu_2

# OST
Main_Menu_1_Getting_Ready
Main_Menu_2_1_Times_of_Crisis
Main_Menu_2_2_Prepare_Yourself

# Menu
Next_Level()
Training()
Shop()

Characters()
Inventory()
Game_Save()
World_Map()




    # GameStateIG.Game_Progress == 2
# Background
Background_Fight

# OST
Fight_1_2_Pushing_Forward

# Enemy List
Wolf LvL 2

# Introduction
Oh, there is another wolf there...
It's weird, it looked like he's guarding this area.
He's alone, I should be able to take him down easily.

Wait, there is another one!
Well, got no choice but to go through them...
Let's go!

# Victory
Phew... I'm beat.
Now, I should be near the village.
Let's see what's happening...

Wh...What!? The village is in fire!
What happened there?
I can see some people still trying to escape!
I have to rush over there and help them!




    # GameStateIG.Game_Progress == 3
# Background
Background_Fight

# OST
Fight_1_2_Pushing_Forward

# Enemy List
Direwolf LvL 1

# Introduction
This wolf doesn't seem like the other one.
He looks way more bigger.
I should be more careful around him.

# Victory
Alright! I'll soon reach the village.
Let's keep up this pace!
These villagers need my people to escape such monsters like that.



    # GameStateIG.Game_Progress == 4
# Background
Background_Fight

# OST
Fight_1_2_Pushing_Forward

# Enemy List
Wolf LvL 2
Wolf LvL 2
Wolf LvL 2

# Introduction
Hey, that's quite a big pack of wolves!
I wonder if I'll be able to face all of them...
I'll need help but for now let's stop the ones that are standing before me.

# Victory
The more I approach the village, the more stronger they become...
I still hear the villagers screaming over there.
I need to hurry up and join them.




    # GameStateIG.Game_Progress == 5
# Background
Background_Fight

# OST
Fight_1_3_Pushing_Forward

# New Ally
Iris LvL 3

# Enemy List
Direwolf LvL 2
Wolf LvL 3
Wolf LvL 3

# Introduction
The air is blazing!
I hope we will be able to evacuate everyone.
Wait, someone over there is fighting a group of wolves!
I have to help him fight them!

Hey! Need my help over here!?
I'll help you take them down!

Yes! I'll gladly accept your offer!
My name is Iris, let's beat all of them out of the village!

# Victory
It was the last one of them!
Your precision with the bow is really amazing!
You were a great help!

No, I should be the one thanking you!
I wonder how I would've end up if you weren't there as a vanguard...
I don't really want to think about it though.

Lucky I rushed over here then I guess.

We've got other people to help.
Let's move on.

Yeah, you're right.




    # GameStateIG.Game_Progress == 6
# Background
Background_Fight

# OST
Fight_1_3_Pushing_Forward

# Enemy List
Direwolf LvL 2
Direwolf LvL 2

# Introduction
We should head toward the center of the Village.
From what I've seen, it seems like that most of the wolves were gathering there.

There are a couple of wolves over there!
Get ready!

# Victory
We're near the center of the village now.

Their numbers keep growing up...
I wonder what's happening here...




    # GameStateIG.Game_Progress == 6
# Background
Background_Fight

# OST
Fight_1_4_Intimidating_Foe

# Enemy List
Shadow Figure LvL ??
Direwolf LvL 4
Wolf LvL 5

# Introduction
So, we reached the center of the Village.
What do we do now? Have you seen their numbers?


If we want to halt the slaughter, we must stop them from there.

Isn't that dangerous to take them all at once!?

We can bait them out of there.
I'll throw an explosive on them so they run away from here.

I hope they don't run toward us.

    (SFX_Explosive)
    (SFX_Wolf_Howl)

Alright, it worked!
Now, let's look for their leader and take him down!

    (SFX_Shadow_figure)

Is that thing their leader...?
It doesn't seem like a living being...
Can we kill it?

What is a demon doing out there?

A demon?

Yes, it's a creature summoned by the Dark Lord to help him conquering territories.
The one in front of us is probably one of its general.
Though this Shadow Figure doesn't have a body, it still should receive damage from our attacks.

If you say so, then let's go!
We've got no other choice!

# Victory
They're gone! We beat them!
The village is safe now!

Let's look for surviving people.
I'm sure a few of them are injured or need some help.

We should also gather the people over here.

Yes, you're right. Let's do that.

