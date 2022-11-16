"""

Riding the massive breakout success of your first game, Orcs
Vs. Goblins, your team dives right into developing its sequel:
Creature Clash. This new game features many new creature types... as
well as the classic goblins:

>>> goby = Goblin('Goby')
>>> goby.name
'Goby'

Like all creatures in this new game, Goblins have attributes for their
hitpoints, attack damage, and defensive armor.

>>> goby.hitpoints
10
>>> goby.damage
3
>>> goby.armor
1

Of course, your fan base will rebel if you don't also have orcs. Like
before, they're a bit tougher:

>>> morgash = Orc('Morgash')
>>> morgash.name
'Morgash'
>>> morgash.hitpoints
15
>>> morgash.damage
5
>>> morgash.armor
2

And now we introduce HillOrcs, who are even tougher (but with a
weakness you'll learn about later):

>>> narbul = HillOrc('Narbul')
>>> narbul.name
'Narbul'
>>> narbul.hitpoints
20
>>> narbul.damage
5
>>> narbul.armor
3

There's also skeletons, who don't have any armor at all:

>>> bonez = Skeleton('Bonez')
>>> bonez.name
'Bonez'
>>> bonez.hitpoints
8
>>> bonez.damage
4
>>> bonez.armor
0

And finally, Ewoks. Who are tiny, but pack a punch (by
creating clever, devastating traps):

>>> teebo = Ewok('Teebo')
>>> teebo.name
'Teebo'
>>> teebo.hitpoints
4
>>> teebo.damage
10
>>> teebo.armor
1

Each of these inherit from a class called Creature. In writing your
code, be sure to put as many methods and member variables as possible
in this base class, overriding in the subclass when necessary.

>>> isinstance(goby, Creature)
True
>>> isinstance(morgash, Creature)
True
>>> isinstance(narbul, Creature)
True
>>> isinstance(bonez, Creature)
True
>>> isinstance(teebo, Creature)
True

You can check whether a creature is alive:

>>> bonez.is_alive()
True
>>> bonez.hitpoints = 0
>>> bonez.is_alive()
False
>>> bonez.hitpoints = 8
>>> bonez.is_alive()
True

The hitpoints, damage and armor values come into play when the
creatures fight.  The total damage done is equal to the attacker's
"damage" value, minus the target's "armor" value. The attack() method
returns the net damage done:

>>> goby.hitpoints
10
>>> bonez.hitpoints
8
>>> bonez.attack(goby)
3
>>> goby.hitpoints
7

Skeletons have no armor, so they take the full impact!
>>> goby.attack(bonez)
3
>>> bonez.hitpoints
5

When there's more than one creature to fight, an attacker has to
choose. Goblins and Ewoks simply choose the first one in the list:

>>> creatures = [narbul, goby, teebo, bonez, morgash]
>>> target = goby.select_target(creatures)
>>> target.name
'Narbul'
>>> target = teebo.select_target(creatures)
>>> target.name
'Narbul'

Skeletons are more devious and opportunistic. They will choose the
creature in the list with the fewest hit points:

>>> target = bonez.select_target(creatures)
>>> target.name
'Teebo'

Orcs (including Hill Orcs) are more complex. First, they won't attack
other orcs at all... unless there's no one to attack *except* an
orc. And among those it's willing to attack, it will pick the one with
the worst armor:

>>> target = narbul.select_target(creatures)
>>> target.name
'Bonez'
>>> target = morgash.select_target(creatures)
>>> target.name
'Bonez'

If there's no one to attack BUT orcs, then an orc will happily attack
the one with the worst (lowest) armor:

>>> only_orcs = [narbul, morgash]
>>> nashba = Orc('Nashba')
>>> target = nashba.select_target(only_orcs)
>>> target.name
'Morgash'

Hill Orcs have a weakness. Though strong and tough, they are TERRIFIED of
skeletons. If they attack one, fear reduces their muscles to jelly, and they do
no damage at all:

>>> bonez.hitpoints
5
>>> narbul.attack(bonez)
0
>>> narbul.attack(bonez)
0
>>> narbul.attack(bonez)
0
>>> bonez.hitpoints
5

Goblins have one last trick. Generations of conflict with Orcs have
taught them especially effective tactics against their long-time
foes. So when they attack an Orc - *any* kind of Orc - they deal
double damage:

>>> nashba.hitpoints
15
>>> goby.attack(nashba)
4
>>> nashba.hitpoints
11

>>> narbul.hitpoints
20
>>> goby.attack(narbul)
3
>>> narbul.hitpoints
17

"""

# Write your code here:


class Creature:
    def __init__(self, name):
        self.name = name

    def is_alive(self):
        return self.hitpoints > 0

    def attack(self, creature):
        net_damage = self.damage - creature.armor
        creature.hitpoints -= net_damage
        return net_damage

    def describe(self):
        return f"{self.name} the {self.__class__.__name__}"

    def select_target(self, creatures):
        return creatures[0]


class Goblin(Creature):
    hitpoints = 10
    damage = 3
    armor = 1

    def attack(self, creature):
        original_damage = self.damage
        if isinstance(creature, Orc):
            self.damage *= 2
        net_damage = super().attack(creature)
        self.damage = original_damage
        return net_damage


class Orc(Creature):
    hitpoints = 15
    damage = 5
    armor = 2

    def select_target(self, creatures):
        targets = [creature for creature in creatures if not isinstance(creature, Orc)]
        if not targets:
            targets = creatures
        return min(targets, key=lambda target: target.armor)


class HillOrc(Orc):
    hitpoints = 20
    armor = 3

    def attack(self, creature):
        return 0 if isinstance(creature, Skeleton) else super().attack(creature)


class Skeleton(Creature):
    hitpoints = 8
    damage = 4
    armor = 0

    def select_target(self, creatures):
        return min(creatures, key=lambda creature: creature.hitpoints)


class Ewok(Creature):
    hitpoints = 4
    damage = 10
    armor = 1


# Do not edit any code below this line!

if __name__ == "__main__":
    import doctest

    count, _ = doctest.testmod()
    if count == 0:
        print("*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!")

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
