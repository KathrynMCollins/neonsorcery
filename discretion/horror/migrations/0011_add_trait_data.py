from django.db import migrations


GENERAL_TRAITS_POSITIVE = [
    # (name, positive_effects, description)
    (
        "Astral Awakening",
        "Born with Astral soul. XP Cost: 3 × Level",
        None,
    ),
    (
        "Technomancy",
        "Born with Resonant soul – able to take technomancy traits. XP Cost: 3 × Level",
        None,
    ),
    (
        "Extra Upbringing Etiquette",
        "Gain additional upbringing etiquette. XP Cost: 6",
        None,
    ),
    (
        "Extra Career Etiquette",
        "Gain additional career etiquette. XP Cost: 4",
        None,
    ),
    (
        "Extra General Skills",
        "2 additional general skill points. XP Cost: 3",
        None,
    ),
    (
        "Extra Niche Skills",
        "3 additional niche skill points. XP Cost: 2",
        None,
    ),
    (
        "Extra Friend",
        "Gain extra contact at Power 3, Friendly affinity. XP Cost: 3",
        None,
    ),
    (
        "Good Friend",
        "Better friend – increase affinity for contact by 1 or increase power by 1. XP Cost: 4",
        None,
    ),
    (
        "Sturdy",
        "Increase health tracker by 1. XP Cost: 3",
        None,
    ),
    (
        "Focused",
        "Increase stun tracker by 1. XP Cost: 3",
        None,
    ),
    (
        "Blessed",
        "Permanent positive spell or program. XP Cost: 3–6",
        None,
    ),
    (
        "Deep Pockets",
        "5 extra fortune to spend per XP. XP Cost: 1",
        None,
    ),
    (
        "Surged",
        "Magically genetically altered, triggering inhuman physiological traits. XP Cost: variable",
        None,
    ),
    (
        "Infected",
        "Has contracted a mythic viral infection and belongs to a sentient monster group such as ghouls, vampires, or werewolves. XP Cost: variable",
        None,
    ),
]

GENERAL_TRAITS_NEGATIVE = [
    # (name, negative_effects, description)
    (
        "Extra Enemy",
        "Gain extra enemy contact at Power 3, Dislike affinity. XP Gain: 3",
        None,
    ),
    (
        "Grudge",
        "Worse enemy – decrease affinity for contact by 1 or increase power by 1. XP Gain: 4",
        None,
    ),
    (
        "Frail",
        "Decrease health tracker by 1. XP Gain: 3",
        None,
    ),
    (
        "Pain-Sensitive",
        "Decrease health tracker by 1 (stun). XP Gain: 3",
        None,
    ),
    (
        "Cursed",
        "Permanent negative spell or program. XP Gain: 3–6",
        None,
    ),
    (
        "Poor",
        "5 less fortune to spend per XP. XP Gain: 1",
        None,
    ),
    (
        "Criminal Record",
        "Character Global Heat +1. XP Gain: 5",
        None,
    ),
]

# Circumstantial traits: (name, condition, roll_effect, is_negative)
# is_negative=True → roll_effect goes in negative_effects; False → positive_effects
CIRCUMSTANTIAL_TRAITS = [
    (
        "Addiction",
        "Character is hooked on a substance – drug, tech or magic experience, euphoria, gambling, or sex.",
        "While distracted or under duress, all perception checks at −1 success. XP Gain: 3",
        True,
    ),
    (
        "Allergy",
        "Negative modifier to all tests when dealing with allergen because of distraction.",
        "Add an extra 1 to rolls made while affected by the allergy (double cost if common allergy). XP Gain: 3",
        True,
    ),
    (
        "Amiable",
        "Can defuse conflict.",
        None,
        False,
    ),
    (
        "Analytical Mind",
        "Naturally gifted at finding connections between seemingly unconnected elements.",
        "Add 3 more dice to non-specific research checks. XP Cost: 2",
        False,
    ),
    (
        "Animal Handler",
        "Skilled at handling animals.",
        None,
        False,
    ),
    (
        "Astral Chameleon",
        "Astral signature blends into background, stealthed casting is easier.",
        "Stealthed casting is easier. XP Cost: 3",
        False,
    ),
    (
        "Astral Sight",
        "Character was born with astral sight.",
        None,
        False,
    ),
    (
        "Blandness",
        "Character looks unremarkable for metatype; penalty for others to remember character description or recognise face.",
        "Remove a 1 from stealth rolls that depend on you not being identified. XP Cost: 2",
        False,
    ),
    (
        "Body Sculpted",
        "Improved attraction, aesthetics, or new face.",
        "Add 3 more dice to rolls where seduction or flirting is part of the check. XP Cost: 2",
        False,
    ),
    (
        "Brawny",
        "Can carry more than usual or use physical intimidation.",
        None,
        False,
    ),
    (
        "Combat Paralysis",
        "Penalty on initiative.",
        "Remove 1 success from initiative rolls. XP Gain: 2",
        True,
    ),
    (
        "Commando",
        "Skilled at hiding in almost plain sight.",
        None,
        False,
    ),
    (
        "Competitive Advantage",
        "Boost with sports and games of competition.",
        None,
        False,
    ),
    (
        "Curious",
        "Bonus on researching through conversation.",
        None,
        False,
    ),
    (
        "Diehard",
        None,
        None,
        False,
    ),
    (
        "Eye for Secrets",
        "Bonus to finding hidden caches and safes.",
        "Add 3 dice to checks to find hidden objects. XP Cost: 2",
        False,
    ),
    (
        "First Impression",
        "Bonus to social tests first time meeting a person.",
        "Add 3 dice to social rolls within the first hour of meeting someone. XP Cost: 2",
        False,
    ),
    (
        "Five Finger Discount",
        "Bonus to sleight of hand to pocket an item in crowded space.",
        "Add 1 success to stealth checks involving objects smaller than your palm. XP Cost: 3",
        False,
    ),
    (
        "Gremlins",
        "Natural trouble with technology and resonance.",
        "Add a 1 to all rolls involving technology. XP Gain: 2",
        True,
    ),
    (
        "Haggler",
        "Can get reduced price when negotiating.",
        None,
        False,
    ),
    (
        "Hawk Eye",
        "Can see further or better than average person. Incompatible with Bioware.",
        "Add 1 success to perception checks made if visual distance penalty applies. XP Cost: 3",
        False,
    ),
    (
        "High Pain Tolerance",
        "Can ignore pain up to a certain threshold; reduce rollover stun effects from wounds or pain.",
        "Halve the amount of stun damage taken from physical damage rollover. XP Cost: 1",
        False,
    ),
    (
        "Hollow Leg",
        "Increased tolerance for drugs.",
        None,
        False,
    ),
    (
        "Juryrigger",
        "Deep knowledge of how to fudge during crafting; bonus when crafting on the fly or using improvised parts.",
        "Add 1 success to hacking or rigging checks for analog or physical wiring. XP Cost: 3",
        False,
    ),
    (
        "Laugh at Danger",
        "Give boost to allies when you take damage.",
        "Add 1 success to assist rolls after you have taken physical damage. XP Cost: 3",
        False,
    ),
    (
        "Low Pain Tolerance",
        "Take extra stun from wounds and pain effects.",
        "Take 1 extra point of rollover stun damage from physical damage. XP Gain: 1",
        True,
    ),
    (
        "Lightning Reflexes",
        "Increased initiative under threat.",
        "Add 1 success to initiative checks if an enemy has spotted you. XP Cost: 3",
        False,
    ),
    (
        "Lightweight",
        "More susceptible to drugs.",
        None,
        True,
    ),
    (
        "Lucky SOB",
        "Somehow manages to come out of even the worst situations alright.",
        "If a roll would trigger alarm, remove 1 extra 1. XP Cost: 1",
        False,
    ),
    (
        "Motion Sickness",
        "Penalty on skill checks while in a moving vehicle.",
        "Remove 3 dice from skill checks made in a moving vehicle. XP Gain: 2",
        True,
    ),
    (
        "Oblivious",
        "Penalty to all perception rolls of a specific type (Social, Threat, Astral, etc.). You must have access to that perception type.",
        "Remove 1 success from all perception rolls of that type. XP Gain: 3",
        True,
    ),
    (
        "Phobia",
        "Character is afraid of a common thing. Can be rational or irrational, but fear is severe.",
        None,
        True,
    ),
    (
        "Quick-Witted",
        "Bonus to speech checks that require comebacks or on-the-fly improvisation.",
        None,
        False,
    ),
    (
        "Resistance",
        "You are naturally resistant to a specific type of damage (pick element, toxin, or poison).",
        "Remove 1 point of damage from that specific damage type. XP Cost: 1",
        False,
    ),
    (
        "Resonant Sight",
        "Character was born with resonant sight. Only available for technomancers.",
        None,
        False,
    ),
    (
        "Resonant Touch",
        "Character was born with resonant touch. Only available for technomancers.",
        None,
        False,
    ),
    (
        "Self-Taught",
        "More likely to make mistakes on skill checks.",
        "Add an extra 1 to skill checks when under stress or in a hurry. XP Gain: 2",
        True,
    ),
    (
        "Sensible",
        "Less likely to make mistakes during routine moments.",
        "Remove a 1 from rolls made in safe and neutral situations. XP Cost: 2",
        False,
    ),
    (
        "Spirit Affinity",
        "Has the favour of spirits; easier summoning or better favours.",
        None,
        False,
    ),
]


def add_traits(apps, schema_editor):
    QuirkCategory = apps.get_model("horror", "QuirkCategory")
    Quirk = apps.get_model("horror", "Quirk")

    general_cat = QuirkCategory.objects.create(
        name_de="General Traits",
        name_en="General Traits",
    )
    circumstantial_cat = QuirkCategory.objects.create(
        name_de="Circumstantial Traits",
        name_en="Circumstantial Traits",
    )

    for name, positive_effect, description in GENERAL_TRAITS_POSITIVE:
        Quirk.objects.create(
            name_de=name,
            name_en=name,
            category=general_cat,
            positive_effects_de=positive_effect,
            positive_effects_en=positive_effect,
            description_de=description,
            description_en=description,
        )

    for name, negative_effect, description in GENERAL_TRAITS_NEGATIVE:
        Quirk.objects.create(
            name_de=name,
            name_en=name,
            category=general_cat,
            negative_effects_de=negative_effect,
            negative_effects_en=negative_effect,
            description_de=description,
            description_en=description,
        )

    for name, condition, roll_effect, is_negative in CIRCUMSTANTIAL_TRAITS:
        kwargs = dict(
            name_de=name,
            name_en=name,
            category=circumstantial_cat,
            description_de=condition,
            description_en=condition,
        )
        if roll_effect and is_negative:
            kwargs["negative_effects_de"] = roll_effect
            kwargs["negative_effects_en"] = roll_effect
        elif roll_effect:
            kwargs["positive_effects_de"] = roll_effect
            kwargs["positive_effects_en"] = roll_effect
        Quirk.objects.create(**kwargs)


def remove_traits(apps, schema_editor):
    QuirkCategory = apps.get_model("horror", "QuirkCategory")
    QuirkCategory.objects.filter(
        name_de__in=["General Traits", "Circumstantial Traits"]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("horror", "0010_quirk_extensions"),
    ]

    operations = [
        migrations.RunPython(add_traits, remove_traits),
    ]
