#### 2/28/2022
Here's my to do list:
-Play around with stats
-Play around with equipment
-Play around with items

Base Stats:
* Con - health, 20 to 1 with health
--> Just health?
* Dex - speed, faster speed score goes first
--> Just speed?
* Int - base damage, 1 to 1 with damage
--> Just base damage?
* Luck - general stat that affects rolls
We'll see if we get these stats to do anything else. 

Extra Stats:
* Gold Gain - bonus gold at end of battle, just ads percentage extra
* Item Gain - at end of battle roll chance to get common or rare item, adjusts thats
* Elemental Damage - extra damage for each damage type
* Elemental Damage Multiplier - this will change how resitance and weakness damages are calculated
* Crit Chance - you can crit, enemies can't, chance to crit on each attack, starts really low
* Crit Damage - damage bonus on crit
--> Break down by elemental type?
* Super Charge Rate - there's going to be a mechanic like overdrive, limit break, super special attack go that charges with damage/hits, this will affect that charge rate. I'm just going to call it super until I get a different name

Right now I'm thinking percentages and multipliers are not stackable. But all of this knowledge will be shared with the player, so they can go to their stat page and be like, what's my % chance to crit and find out directly.


Ok, so looking at the above stats, it introduces a couple of ideas:
1. How is luck going to be factored into rolls?
2. How is a super going to work?

Luck:
So currently we sample a uniform 0, 1 distribution and just use that with some range to determine things. I haven't worked out the details, but percent chance is going to be like if you have a 25% chance to get an common item, and a 5 % chance to get a rare item, if you roll between 71-95 you get a common item and if you roll between 96-100 you get a rare item. Something like that. 

Here are the things I can think of that are dictated by chance in the game:
Definitely in game:
* Enemy spawns
* Item drops
* Critical hits
Maybe in Game:
* Enemy critical hits
* Damage ranges on your attacks
* Damage ranges on enemy attacks
* Hit chance/evasion
I have to decide if some of these are going to be in the game. Some of these are bullshit or add to the bull shittery of games, so I'm inclined to leave them out. Like one thing I appreciated about DS is you do the damage that you do and you miss because you actually missed (like the two objects did not smash hit boxes together).

Of these, item drops is d100 and critical hits are d100 and unless we want there to be a rare enemy that spawns on a chance then then that could also exist on d100. Currently, no plans for that though. So luck will affect those two rolls.

Right now, I'm thinking something like square root of luck is added %. So let's see:
1 luck -> 1% increase from base
4 luck -> 2% increase from base
100 -> 10%
Right, but the diminshing returns makes stacking luck not super broken and it has a cap at 10000, which is pretty high.

For supers, I'm thinking there's a couple of aspects of it:
1. You can add some number of elements together to make the attack and the damage will get scaled based on each percentage type of damage.
2. Super bar is full at 10000, because of truncation design choice. This will make equipment with low increases in super charge rate relevant. These numbers may or may not be hidden from the player. So like 1% increase has an impact still despite the truncation, just with big and little hits.
3. Super charges when you get hit at a rate of 10 * % damage of total health. So if your health is dropped to zero from full, that will give you 1000 points.
4. Super charges when you hit an enemy at a rate of 10 * % damage of their total health. So every 10 enemies beaten should give you 1 use of super.
5. Bonus super charge rate is applied as a percent increase on one of these two. Possibly will have sadism vs. masochism (won't use those words) that skews the points one way or the other.
6. Create a little text UI that shows (something like Super: \[XX_________\] percentage charge)

In general, fractions are rounding down, always. Any time a float is converted to an integer it is simply truncated. THIS COULD LEAD TO PROBLEMS IN THE FUTURE, BUT THIS IS THE CURRENT POLICY.

Also, I'm going to make a store.

Couple of parting thoughts:
* Overkills? Yes or no?
* Python UI? Or just do everything in webcode??


-Andy


#### 2/27/2022
Here's a thought, why not make the game entirely on a website, you can the polish your JS and integrate some python into it. You'll have to learn about how to get them to play nice, but overall it shouldn't be too hard. Then your bro can just play the game from his browser, and you can do all of the UI design using CSS. The tech stack is probably going to be a mess, but as a first game not a bad idea. You can then use this as an opportunity to review all of the web code stuff.

GoDot is still a good option.
-Andy

#### Base Design statement
This Game Engine is a bit of a mess, but I threw it together to provide an
easily modifiable framework. I tried to compartmentalize as much of the
reuseable code into classes and such to make building out complexity easier.
I do not know how well I succeeded. Enjoy!
-Andy