# Math Game  
## Description
Educational game meant to get young children (elementary school age) interested in practicing basic arithmetic through gamification of worksheet style problems.

The game revolves around collecting different schools of magic, which are different arithmetic operations and using those spells to overcome foes. It will use a final fantasy style rpg battle system to provide randomized practice problems for the children to solve.
## Features (and I Mean All of Them)
I making this a full scope work document, so I'm writing out all the features we will need to do the creative work on, scope out, and design.
### Fundamentals
These are the fundamental features that will make the game live and breathe as a game, but aren't going to necessarily show up in a base prototype. A lot of this stuff gets taken care of by a pre-built engine like RPG maker, but we can choose how we want to cross that bridge later. A lot of this stuff I've never done before in a general game engine (like GoDot or Unity) so there will be a lot of learning on my part.
#### Menus
Basic menus that allow the player to select stuff.

Attributes:
* Text that the player can select and it opens up a sub menu or directs the game somewhere else
* Overlay over the background with highlightable and selectable elements
#### Navigateable Map
This feature is meant to encompass both a world map and local maps.

Attributes:
* Local location that player can explore
* World Map that links them all together

Questions:
* Top down RPG? Metroidvania? Something else? I'm not doing 3D.
* Do we want a global/local view? Pokemon, for example, has an overall world map, but when you play the game everything exists in a local world, much like metroid. FF does not work like this. The overworld acts like a different experience
#### RPG Text Conversations
Think Pokemon, FF, any game where you can talk to other characters.

Attributes:
* Text overlay as a way to communicate with the player

Questions:
* How complicated do we want to make this? Fancy text features? Branching dialog trees based on what you've done in game? Meaningful options that the player can select? All of these add a layer of difficulty...

#### Interactable NPCs
Basic NPCs

Attributes:
* You can talk to them
* They can give you quests
* They can pick fights with you

#### Quests
Tasks for the player to do, get the McGuffin

Questions:
* What kind of quests do you want to have in the game? Given the other things on the list, this can be simple as go get the item from this place, go battle this many things, go talk to this person, go to this location, among other things. Thoughts?

#### Random Battle
Randomly generate monsters for the player to battle.

Attributes:
* Randomly select from pool of monsters with fixed (or random?) stats for the player to battle
* Player encounters monster, player fights monster, player wins and gains loot and experience, player loses and game over
#### Scalability of Characters and Enemies
Basic of all RPGs, gives you a sense of progression

Attributes:
* Enemies get harder with higher level
* Player gets stronger
* Some concept of numerical values that you can increase or decrease depending on level, gear, and other factors that determine how your character performs in game. A lot of the curves and functions will probably need to be play tested.
* As a general rule, some stuff will scale linearly and some geometrically. This mismatch makes the game get more challenging without much input on the part of the dev. Usually, games solve difficulty by setting enemy difficulty and forcing the player to meet it. Stuff like, if the player is this level, this boss should be easy.
* Leveling up, allocatable points(?), random stat boost(?), stat boost on a curve based on class(?)
* Abilities level up?
* Do we even want classes?

#### Loot
Basic of all RPGs, you collect stuff and that's part of how you get more powerful, from equipment to quest items

Attributes:
* Inventory system and way of tracking items and which items the players have.
* Way for the players to interact with said items so they can equip them or somehow use them.
* Way for the players to get items from the world either from NPCs or chests.
* Items should have a meaningful impact on the game, either unlocking new abilities, changing player stats, or completing quest objectives.

### Project Specific
These are the features to this game.
#### Math Spells
The main mechanic this game revolves around. A lot of the details can be hashed out later, but the basic experience can be created in a prototype in python.

Attributes:
* During random encounters, in order to battle, the player needs to select which spell they want to case
* Different spells are associated with different math problems
* Spells level up to get stronger, but in turn the math problems get harder as well
* Spells level up based on useage (do not want player to suddenly face hard problems, if they haven't practiced the easy stuff)
* Spells can be combined to make harder math problems
* At a base level, problems like 1 + 2 = ?, but also want stuff like 1 + ? = 3, similar skill sets, but teaches a different way of thinking about math
* Unlock different kinds of math as the game progresses
* Math come with different elemental types (see below)
* Depending on the difficulty of the math, we might need to create a more sophisticated solver. Basic arithmetic is pretty easy to implement, but anything symbolic becomes harder.

Questions:
* How do we want to do criticals?
* What do we want to have happen when the player gets the math problem wrong?
* Do we want a binary of right and wrong?

#### Weakness/Resistance Elemental-style Damage
Think Pokemon types.

Attributes:
* Monsters are typed, making them resistant and vulnerable to certain types of damage.
* Spells are typed, making them strong or weak against certain types
* This will force player to use spells that they might otherwise avoid (i.e. do math they don't like)

Questions:
* How many types?
* What kind of tree?
* Do we want immunity?
* Do we want status effects (think poison, paralysis, sleep, silence)?

## Versions
### Version 1: The Basics
Create a random battler with the following features:
* Create a battle system that implements all the basic of the math based, turn based combat described above.
* Have the player and monsters grow as more battles happen
* Win condition: player defeates x monsters

Advanced:
* Items the player can use or equip or upgrade
* Some form of stat system

Polish:
* Balance the math on the above systems and establish some meaningful progress gates as well as meaningful difficulty for encounters
* Make meaningful stats
* Figure out some item balancing

Concerns:
* A proper item system is a huge lift in this part. It's pretty easy to give the player a bunch of potions that they can time the healing of and what not. Or like you find a wand and you equip it, it increases these stats, but you have no way to unequip it until you find a new one.
* Stats are largely just math. So figure out a math formula that feels appropriate and stick to it. Pick the stats you want and choose what they do and then math it out so that the stats feel impactful.
### Version 2: Now with More Moving around
Take the above and embed it in a world.
* Player should be able to walk around and interact with things
* Random/placed encounters minimal level design, but possible
* Items and inventory the player can use
* Proper stats

Advanced:
* NPCs you can talk to
* Shops

Polish:
* Balanced money system
* Put some polish on all the things that make such a system good, like do we want the player to be able to freely navigate, are the maps grids? How do we do collisions? How do we load levels? Is it relatively efficient?

### Version 3: Now with more RPG
Take the above and add RPG elements
* Babies first quest
* Babies first npc conversation
* Babies first multi-level area (or dungeon)
* Babies first key item

Advanced:
* Fancy text engine with meaningful choices, this means story driven flags
* This adds a layer of complication to NPCs and represents the start of creating a story

Polish:
* Honestly, having meaningful RPG elements at this point is going to be largely polish. It's more important to create a system and work out the details and what type of story elements we want to accomplish

## Timeline
????

## Development Log
2/15/2022 - Super basic python prototype completed and design document made.

## Feature Ideas, Requests, Bug Fixes
Please add feature ideas, requests, and bug fixes here. This section is meant to document them, so we know what we've done and what we've considered.
### New
### Completed
### Rejected