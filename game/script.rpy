# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define nuke = Character("Reactor")
define coretana = Character("Coretana")
define stranger = Character("Stranger")
define engineer1 = Character("Engineer1")
define engineer2 = Character("Engineer2")
# The game starts here.

label start:

    init python:
        love = 0
        true_love = 0
        safety = 0
        worker_trust = 0
        government = 0
        power_choice = 0
        
    play music "by_the_seaside.mp3"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg field

    "You are a powerful government agent who has been given the task of utilizing 
    a powerful source of energy, nuclear."

    "In your position of primary engineer and manager for this new power plant, you will 
    need to plan out the construction, regulation, and maintainment of this facility"

    "In addition to the internal factors and problems you will face, there will also be 
    many extrenal factors that will require your attention"

    "First, we must ensure that you have some knowledge about nuclear power"

    label question_1:
    "How many US states use nuclear power?"

    menu:
        "48":
            jump incorrect_answer1
        "23":
            jump incorrect_answer1
        "50":
            jump incorrect_answer1  
        "30":
            jump correct_answer1          


    label correct_answer1:
        "Great, that is correct, also, as of 2018 Illinois has 11 reactors - 
        the most of any state. (Department of Energy)"
        jump question_2

    label incorrect_answer1:
        "That is incorrect, but try again"
        jump question_1

    label question_2:
        "What percentage of clean energy produced in the US is nuclear?"
    menu:
        "56":
            jump correct_answer2
        "18":
            jump incorrect_answer2
        "21":
            jump incorrect_answer2

    label correct_answer2:
        "Great, that is correct, Wind accounts for 18 percent, and hydro power for 21 percent."
        jump question_3

    label incorrect_answer2:
        "Sorry that's incorrect, try again"
        jump question_2

    label question_3:
        "What... is the airspeed velocity of an unladen swallow?"
        "Wait, no that's not the question that was supposed to show up, now for the actual question"
        "How is energy made in a nuclear reactor"
    menu:
        "Asking the atoms really nicely to explode":
            jump incorrect_answer3
        "Nuclear Fission":
            jump correct_answer3
        "Taking a lunch break and hoping the reactor doesn't melt down":
            jump incorrect_answer3

    label correct_answer3:
        "Great, that is correct, the process is very complicated, but you won't 
        need to get into that for this position"
        jump post_questions

    label incorrect_answer3:
        "As funny as this answer may be, that is incorrect, we all know that it is nuclear fission"
        jump post_questions         


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    label post_questions:

        scene bg office

        "Now that we know you are qualified for this job, what is your name?"
        python:
            name = renpy.input("What is your name?")

            name = name.strip() or "No name"

        "Alright [name], it's time to start thinking about how to make this power plant work, 
        and maybe you will find something you didn't know you were looking for"

    label first_meet:

        show nuclearreactor base at right 

        nuke "HAIIIIIIII :33333"

        "You feel a wave of confusion washing you over. What... is this thing? 
        And why is it talking to me? Why is it so... happy?"

        name "Um... hi. I heard you needed some help. I'm the new director."

        nuke "Oh it's good that they sent a new one! The last director was a meanie, 
        but you seem really nice! He made so much bad stuff happen."

        name "I'm... sorry to hear that. What bad stuff?"

        show nuclearreactor sad at right

        nuke "The humans are really stressed out. They keep talking about paperwork and not getting
        the plant to run and I just want to help out, but I can't. I haven't produced any power
        in so long. It makes me a bit sad to think about..."

        menu:
            "Oh no! You seem really distressed. I'll try my best, okay? Just try your best to stay positive.":
                jump d1o1
            "You shouldn't cry about things that are fixable. I'll go talk to them.":
                jump d1o2
            "Okay, I'll look into that":
                jump d1o3

        label d1o1:
            name "Oh no! You seem really distressed. I'll try my best, okay? Just try your best to stay positive."
            python:
                love = love+1
            show nuclearreactor blushing at right 
            nuke "Thank you director! :3"
            hide nuclearreactor blushing
            jump checklist

        label d1o2:
            name "You shouldn't cry about things that are fixable. I'll go talk to them."
            python:
                love = love-1
            show nuclearreactor base
            nuke "Okay"
            hide nuclearreactor base with dissolve
            jump checklist

        label d1o3:
            name "Okay, I'll look into that"
            show nuclearreactor base
            nuke "It was nice meeting you"
            hide nuclearreactor base with dissolve
            jump checklist

    label checklist:
        scene bg dirty_office
        "The reactor wasn't lying... this place really is a mess!"
        name "I guess I have to make a plan to reorganize the facility"
        name "What should I do?"

        menu:
            "Begin a checklist to allow smooth operation of energy production":
                jump d2o1
            "Let the workers try to figure out the problems for themselves":
                jump d2o2
            "Talk with a group of other engineers to get more ideas on how to proceed":
                jump d2o3

        label d2o1:
            name "Okay, so I need to make a checklist so the workers can feel guided and safe in the production of energy"
            name "I don't even know where to start, maybe I can talk to the reactor and see if it has any ideas, it would know best after all"
            show nuclearreactor base at right
            if(love == 1):
                nuke "Oh hey! :3"
            else:
                nuke "Hi, [name]"
            name "I'm working on creating a checklist to manage the production of energy, I was wondering if you could guide me in what that should include"
            nuke "The old manager tried to make a checklist, and then the workers were confused on what to do :("
            menu:
                "I was thinking of making a very in depth checklist while also knowing that the workers can understand basic procedures in this field. I mean, most of them have been working in this field for a long time.":
                    jump d3o1
                "Oh no! Maybe checklists aren't that good after all...":
                    jump d3o2
                "That's good to know! Where did they go wrong?":
                    jump d3o3

            label d3o1:
                name "I was thinking of making a very in depth checklist while also knowing that the workers can understand basic procedures in this field. I mean, most of them have been working in this field for a long time."    
                "Why did I feel the need to share that much information? It's almost as if I wanted to impress the reactor..."
                nuke "Oh hehe that's really smart of you! ^_^ Can you tell me more about it?"
                python:
                    love = love + 1
                    safety = safety + 1
                show nuclearreactor blushing at right
                "You got so distracted by your own ideas that you gain no additional information from the reactor."
                hide nuclearreactor blushing 
                jump power

            label d3o2:
                hide nuclearreactor
                "You give up on the idea of checklists and decide to continue regulating the power plant in other ways."
                python: 
                    safety = safety - 1
                jump power

            label d3o3:
                name "That's good to know! Where did they go wrong?"
                nuke "The checklist had one thing on it: Don't cause a disaster. The workers got angry :("
                name "Oh I see... Did they improve it at all?"
                nuke "I think they added a few more things, but not enough"
                name "So I can't have too many elements or else my workers will feel incompetent, but I also can't have too little or the checklist will be ineffective... Maybe I'm just not good enough for this task..."
                nuke "No director! Don't ever doubt your abilities! I can see that you are a very capable person :3"
                name "Th...thank you, reactor. By the way, you can call me [name]."
                show nuclearreactor blushing
                nuke "That's a really beautiful name ^_^"
                python:
                    safety = safety + 1
                    love = love + 1
                hide nuclearreactor
                jump power
            

        label d2o2:
            python:
                worker_trust = worker_trust - 1
            "The workers weren't happy with this decision, but most of them brushed it off as you being new."
            jump power

        label d2o3:  
            "You gather a group of engineers working in the nuclear plant in your 
            office and ask for assistance in a move forward"
            name "I've gathered you all here to assess the situation moving forward in the plant, does anyone have any ideas?"
            show engineer 1 at right
            engineer1 "Have you thought of making a checklist? They can be a vital resource in such a volatile field such as ours."
            show engineer 2 at left
            engineer2 "One thing I would add to that is to make sure that the checklist is not condescending towards the workers, 
            we wouldn't want them to think that they are bad at their jobs"
            show engineer 1 at right
            engineer1 "Yes, that's a good point, we also shouldn't try to describe every case where things can go wrong. 
            Inevitable failures shouldn't be addressed in this checklist, maybe just in one location for guidance in an emergency"
            name "Okay I can think about all of the logical steps that happen in the different jobs around here, that should ensure 
            that the workers know what to do while also feeling useful. Thank you everyone"
            hide engineer 
            jump d2o1


    label power:
        "You are now contemplating where to distribute this power when operations are running smoothly"
        "You can either give this power to the government, or to the public and ensure that more people are given clean energy."
        "One thing you must know is that this will undoubtedly lead to shared prosperity"
        "Along with this, you know that whoever gets access to this energy source will be more powerful."

        menu:
            "Distribute this power to the government":
                jump d4o1
            "Distribute this power to the public":
                jump d4o2

        label d4o1:
            "As a person in power in this situation, you realize that you have extreme influence on how this technology is distributed to society. 
            You decide that giving the government this boost of power will allow government run facilities to expand their abilities to help the general public."
            python:
                worker_trust = worker_trust - 1
                government = government + 1
                power_choice = 0
            jump post_power

        label d4o2:
            "As a person in power in this situation, you realize that you have extreme influence on how this technology is distributed to society. 
            You decide that giving the public access to this massive amount of power will enable more people to have access to what the government has had previously."
            python:
                worker_trust = worker_trust + 1
                government = government - 1
                power_choice = 1
            jump post_power

    label post_power:
        scene bg parkinglot
        "As you were heading back home from work, you heard a faint voice in the distance."
        show nuclearreactor base
        nuke "[name]..."
        name "Reactor? Is everything okay?"
        nuke "Yes... I've just overheard you talking about sharing nuclear power."
        name "Oh... Do you want to talk about it?"
        nuke "It's just that... You know what, it doesn't really matter."
        name "Reactor... Are you okay? You can trust me."
        "You feel a heavy weight on your chest. What if you caused this cheerful reactor to feel this way? How do you even fix it without 
        ruining this... bond? Wait... Do you like the nuclear reactor?"
        nuke "M...my feelings don't matter in this case. What are you planning on doing with my power?"
        
        if(power_choice == 0):
            menu:
                "Lie and tell the reactor that you will distribute the power to the public":
                    jump lies
                "Tell the truth and explain that you will distribute the power to the government":
                    jump d5o1
        else:
            menu:
                "Lie and tell the reactor that you will distribute the power to the government":
                    jump lies
                "Tell the truth and explain that you will distribute the power to the public":
                    jump d5o2
        
        label lies:
            "Your fear leads you to lie to the reactor."
            show nuclearreactor sad
            nuke "Your posture... it shifted. You're lying, aren't you? That's what the last director did as well..."
            name "I'm... I'm so sorry, reactor. Is there any way I can make this up to you?"
            nuke "You've broken my trust. I would've managed to live with your decision, 
            whatever it may have been, if only you didn't lie to me."
            "You feel a sharp pain in your chest. It is all too late to fix this now. Maybe it gets better with time."
            python:
                love = love - 3
            hide nuclearreactor sad
        
        label d5o1:
            name "I decided to distribute the power to the government."
            show nuclearreactor sad
            nuke "Oh... I see..."
            name "Reactor? Is everything okay?"
            nuke "Yes... I was just hoping that my power would go to the people. I wanted everyone to be happy."
            menu: 
                "That's a bit naive from you, isn't it?":
                    jump d6o1
                "If the government does its job, everything should be okay.":
                    jump d6o2
                "You're right... I should probably reconsider this.":
                    jump d6o3
            
            label d6o1:
                name "That's a bit naive from you, isn't it?"
                nuke "I don't know, [name]. You seem to be a meanie just like the previous director."
                python:
                    love = love - 1
                hide nuclearreactor sad
                jump actually_post_power

            label d6o2:
                name "If the government does its job, everything should be okay."
                nuke "How are you so sure, [name]?"
                name "I don't know reactor... Sometimes, you have to put trust in people. Maybe they're not as mean as they
                seem. I strive to assume the best from people - how else are we going to succeed? I see you're a caring soul.
                I know you understand."
                show nuclearreactor blushing
                nuke "I... I think I do, [name]. Thank you for being so kind. You're truly special. Please let the 
                workers know about your views as well. They will appreciate you for this."
                "The reactor was right. The workers began to understand how distributing the power to the government could help
                in the long run."
                python:
                    worker_trust = worker_trust + 1
                    government = government + 1
                    love = love + 1
                hide nuclearreactor
                jump actually_post_power
                
            label d6o3:
                name "You're right... Maybe I should actually redistribute power to the public."
                jump public_power

        label d5o2:
            name "I decided to redistribute power to the public."
            jump public_power

        label public_power:
            nuke "[name]... your courage is wonderful. I've never seen anything like this :3"
            show nuclearreactor blushing
            name "I would do anything in my power to ensure your safety and the safety of the population."
            "Is this... love?"
            python:
                love = love + 1
            hide nuclearreactor blushing
            jump actually_post_power

        label actually_post_power:
            scene bg office 
            "You head back into your office the next day and there is a sheet of paper sitting right at your desk."
            "The paper says that there will be a meeting will all of the engineers to help you understand how your new job isn't all internal affairs at the plant."
            
            show engineer 1 at right

            engineer1 "Good to see you [name], we are calling this meeting today to help you understand your job in it's relation to extrenal affairs."
            name "I understand, so where should we start?"
            show engineer 2  at left
            engineer2 "We want to bring up several topics to you. The first being the fact that the nuclear plant is a very authoritarian object in our society."
            engineer2 "It's presence as a high value energy source can bring the risk of foreign powers attempting to seize this."
            engineer2 "While this is extremely unlikely, we still feel that it is important for you to know the possible interaction with one such external factor."

            show engineer 1 at right
            engineer1 "The second thing we want to bring up to you is that the government will have constant communication with us."
            engineer1 "They do this because they need to ensure that things here are regulated here in the plant."
            engineer1 "Some things that they will regulate are very important, such as safety guildlines, worker's rights, energy output, and privacy."
            if (government == 1): 
                engineer1 "They will also keep strict guildlines that they are the only recipients of the power due to your decision earlier."
            if (government == -1): 
                engineer1 "They will also attempt to make guildlines that will ensure they will still get some of the power, even with your decision earlier"
            name "I see... discussing the politics of the nuclear reactor as an artifact is no easy task. Thank you for bringing that up."
        
            menu:
                "Do you have any ideas on how to approach this?":
                    jump d7o1
                "It's time for me to take charge. We would benefit from some authority around here.":
                    jump d7o2

            label d7o1:
                name "What are your suggestions for this?"
                python:
                    worker_trust = worker_trust + 1
                show engineer 2 at left
                engineer2 "I think we should organize a board meeting and vote on our next steps."
                show engineer 1 at right
                engineer1 "That will take quite some time to do, and we're already behind on our schedule."
                show engineer 2 at left
                engineer2 "I know, but it's the only democratic option we have. It's also good to get input from more than three people..."
                show engineer 1 at right
                engineer1 "The decision is yours, [name]."
                hide engineer
                
                menu:
                    "There is no time for meetings. We are already behind. I need to take charge.":
                        jump d7o2
                    "Although we're short on time, this is an important decision. We should have a meeting.":
                        jump d8o1
            
            label d7o2:
                name "I'll take charge. We don't have time for votes - you will have to trust my expertise."
                show engineer 2 at left
                engineer2 "That's... confident. I hope you can live up to your expectations, or else you might see many of your best workers leave."
                python:
                    worker_trust = worker_trust - 1
                hide engineer
                "After a few weeks of taking on the authoritarian approach, you begin to realize that your expertise may not be that great after all..."
                "How are you supposed to know who should oversee the reactor? And at what time? How are you supposed to know what is a reasonable price for new parts? How are you even supposed to run this thing?"
                "Taking on the jack of all trades approach when only being hyperspecialized in one field may not have been the greatest decision, but only time will tell..."
                python:
                    safety = safety - 1
                jump nuke_talk

            label d8o1:
                "The board voted, and new regulations were set in place. Everything seems to be running smoothly."
                python:
                    worker_trust = worker_trust + 1
                    safety = safety + 1
                jump nuke_talk
            
        label nuke_talk:
            scene bg parkinglot
            show nuclearreactor base
            if (love >= 2):
                nuke "Hey [name], how did your meeting go! :)"
                name "Hi! It just finished and we talked a lot about the type of style that should be used to manage the facility"
                nuke "Well I'm sure you made a decision that will make everything here go smoothly. You're always doing the best things for me, and ... of course everyone else here as well."
                name "I'm glad you like the things that I've been doing to keep the facility running. Uhmm, also, speaking of liking things." 
                name "I just want to say that you are a wonderful reactor and every minute I've been here makes me happy that we have the best reactor we could ask for :)"
                show nuclearreactor blushing
                nuke "Oh [name], that's so sweet! And I could say the same about your skills as our director, you really stimulate my energy production"
                python:
                    love = love + 1
                jump state_regulation
                
            if (love < 2):
                nuke "Hi Director." 
                name "Hey Reactor, how have you been doing?."
                if(safety >= 1): 
                    nuke "I've been feeling great! I am back to producing lots of energy and that makes me feel great."
                    name "I'm really glad to hear my tactics have been helping you out, see you tomorrow!"
                    jump state_regulation
                if(safety < 1):
                    show nuclearreactor sad
                    nuke "I'm still finding it very hard to function under these conditions. The workers are just feeling generally unsafe."
                    menu:
                        "I'm really sorry about that, I will try a little harder to increase the safety.":
                            jump safety_increase
                        "Let's keep trying these strategies and trusting the long term prospects of them.":
                            jump state_regulation
                        
                        
            label safety_increase:     
                name "The first thing I can do is hold a briefing for the workers to reassure them of what to do in these critical cases."
                python:
                    safety = safety + 1   
                jump state_regulation
                    
        label state_regulation:
            hide nuclearreactor 
            scene bg office
            "After a long day of work, I should start to think about the government's place in our affairs here at the power plant."
            "The government has given me some guidelines for regulation."
            if(government == 1):
                "Some things that the government is mandating of this facility is that a worker's union is established to maintain their rights."
                "They also mention things about privacy of workers and of all consumers of our power. These are very trivial regulations."
                "They have additionally requested that 100 percent of our power is always distributed to their research facilities, but they acknowledge that if this can't happen, it's okay."
                "What should I do?"
                menu:
                    "Keep the power to the government":
                        jump gov_power
                    "Give some of this power to the public domain":
                        jump reject

            if(government == -1):
                "Some things that the government is mandating is a 25 percent power redistribution to their research facilities."
                "I can also put a counteroffer on the table to ensure that my decision of public distribution stays strong."
                menu:
                    "Fight back against the government request":
                        jump reject_bad
                    "Concede this power to the government":
                        jump gov_power
            label reject:
                "I rejected the governments request for some power, but they understand that the public is also in need."
                jump post_decision 

            label reject_bad:
                "I am going to tell the government that the public is in greater need of this power and will reject their request."
                python:
                    government = government - 1    
                        
            label gov_power:
                "I give some of this power to the government because I know that is how I got this job."
                "They should get some of this power to do critical research." 
                python:
                    government = government + 1
                jump post_decision

        label post_decision:
            scene bg field
            "The hard work of decisions and stress from work have been very present since getting this job."
            "This job is definitely difficult, but all those feelings seem to disappear as you see the Reactor outside after work."
            "It's presence is so wonderful. You can feel all of your problems disappearing in a blink of an eye... All your thoughts converging into one."
            "As you leave your office after another long day, you stop to look at the sky, the mesmerizing yellows and reds of this summer evening taking you back to a much simpler time."
            scene ending sky
            "It's been so long since you looked up from your checklists and regulations and to the world around you."
            "You remember your teenage years. You remember seeing the bustling life around you with the wide-eyed wonder one can only experience a handful of times."
            "Maybe... maybe there is a part of you that is still holding on to these long-gone moments of youthful innocence."
            "A sudden yet welcome warmth engulfs your heart."
            "It is the reactor."
            "It always has been."
            "You walk outside only to be greeted by none other than your concrete beauty."
            show nuclearreactor base with fade
            nuke "H...hi, [name]. The sky is... really beautiful today..."
            if(love>=3):
                menu:
                    "N... not as beautiful as you, reactor.":
                        python:
                            love = love + 1
                        jump true_love
                    "It is! I haven't been outside in a while.":
                        jump fumble
            if(love>=2):
                menu:
                    "Yeah, you're right. I haven't thought about this since my youth.":
                        jump situationship
                    "Yeah! Well, time to go home...":
                        jump fumble
            jump fumble 

            label situationship:
                nuke "Oh! That's really beautiful, hehe ^_^"
                menu:
                    "I'm glad you liked the sky, haha! See you tomorrow!":
                        jump fumble
                    "Not as beautiful as you, reactor":
                        jump true_love

            label fumble:
                "You go home, looking forward to the next day"
                python:
                    true_love = 0
                jump ending

            label true_love:
                name "Not as beautiful as you, reactor. What's your name, by the way?"
                show nuclearreactor blushing at right
                nuke "Oh... um... :3"
                "You feel your cheeks turning red."
                nuke "My name is..."
                nuke "..."
                nuke "..."
                coretana "... Coretana."
                "Hearing these three syllables come out of Coretana's mouth formed the most beautiful symphony you have ever witnessed."
                name "I love you, Coretana."
                python:
                    true_love = 1
                jump ending

        label ending:
            scene bg office
            "Now, you can finally reflect on everything you've done so far"
            if(government == -2):
                python:
                    safety = safety - 1
            if(worker_trust == -2):
                python:
                    safety = safety - 1
            
            if(love >= 6):
                scene bg field
                show nuclearreactor blushing
                nuke "I love you, [name]"
                "You have such a wonderful bond with Coretana, and you decide to run away with her and leave the power plant behind."
                "Thanks for playing! Make sure to check out the other paths if you would like!"
                return
            if(true_love == 1 & safety > 0): 
                scene bg parkinglot
                show nuclearreactor blushing
                "You have discovered love with Coretana, and the entire power plant is thriving."
                "Thanks for playing! Make sure to check out the other paths if you would like!"
                return
            if(true_love == 1 & safety <= 0):
                "You have discovered that you love Coretana, but are unable to maintain the safety of the plant."
                "You are demoted to your previous job working in the government."
                "You are separated from Coretana, and this breaks your heart."
                "Hopefully someone else can step in and make things right."
                "Thanks for playing! Make sure to check out the other paths if you would like!"
                return
            if(true_love == 0 & safety > 0):
                show nuclearreactor base
                "You have maintained safety in the plant and excelled at your job as director."
                "Unfortunately, you feel as if there is still something missing."
                "Longing for a love that was lost."
                hide nuclearreactor with dissolve
                "Maybe one day, you will be able to rekindle an explosion in the heart of Coretana."
                "Thanks for playing! Make sure to check out the other paths if you would like!"
                return
            if(true_love == 0 & safety < 0):
                scene bad ending
                "What seemed to be any normal day at the plant turned horrible in just an instant."
                "Coretana began to meltdown..."
                "As disaster strikes the entire plant, you contemplate if you could have prevented any of this."
                "Perhaps you could have shown more care towards Coretana, or put more safety regulations into place."
                "But as you stare into the disaster you have created, it all fades to black."
                "Thanks for playing! Make sure to check out the other paths if you would like!"
                return
    return
