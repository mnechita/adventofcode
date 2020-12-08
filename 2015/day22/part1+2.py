import functools
import logging

from contextlib import contextmanager, ExitStack
from random import sample


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('RPG')


def magic_missile(p1, p2):
    p2['hp'] -= 4
    logger.debug(f'[MAGIC MISSILE] {p2["name"]} loses 4 hp down to {p2["hp"]}')


def drain(p1, p2):
    p2['hp'] -= 2
    logger.debug(f'[DRAIN] {p2["name"]} loses 2 hp down to {p2["hp"]}')
    p1['hp'] += 2
    logger.debug(f'[DRAIN] {p1["name"]} gains 2 hp up to {p1["hp"]}')


@contextmanager
def shield(p1, p2):
    p1['arm'] += 7
    logger.debug(f'[SHIELD] {p1["name"]} receives 7 armor')
    yield
    p1['arm'] -= 7
    logger.debug(f'[SHIELD] {p1["name"]} losses buff')


@contextmanager
def poison(p1, p2):
    p2['hp'] -= 3
    logger.debug(f'[POISON] {p2["name"]} loses 3 hp down to {p2["hp"]}')
    yield


@contextmanager
def recharge(p1, p2):
    p1['mana'] += 101
    logger.debug(f'[RECHARGE] {p1["name"]} gains 101 mana up to {p1["mana"]}')
    yield


def get_valid_spell(player, effects):
    while True:
        found = False
        for spell_name in sample(spells.keys(), len(spells.keys())):
            spell = spells[spell_name]
            if spell['name'] not in effects.keys() and spell['cost'] <= player['mana']:
                yield spell
                found = True
                break
        if not found:
            yield None


def print_stats(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        player, boss, effects = args[:3]
        logger.debug('----------------------------------------------------------')
        logger.debug(f'[STATS] - Player has {player["hp"]} hp, {player["arm"]} armor, {player["mana"]} mana')
        logger.debug(f'[STATS] - Boss has {boss["hp"]} hp, {boss["dmg"]} damage')
        logger.debug(f'[STATS] - Effects: {[(eff_name, turns) for eff_name, (_, _, turns) in effects.items()]}')

        return func(*args, **kwargs)

    return wrapper


def check_victory(player, boss):
    if player['hp'] <= 0:
        return boss
    if boss['hp'] <= 0:
        return player
    return None


@contextmanager
def resolve_effects(effects):
    with ExitStack() as stack:
        for eff_name, (effect, args, turns) in effects.copy().items():
            stack.enter_context(effect(*args))
            if turns == 1:
                logger.debug(f'[EFFECT] {eff_name} wears off')
                del effects[eff_name]
            else:
                effects[eff_name] = (effect, args, turns - 1)
        yield


@print_stats
def boss_turn(player, boss, effects):
    logger.debug('[BOSS] turn')
    with resolve_effects(effects):
        winner = check_victory(player, boss)
        if winner is not None:
            return winner
        player['hp'] -= max(boss['dmg'] - player['arm'], 1)
        logger.debug(f"[BOSS] hits player for {max(boss['dmg'] - player['arm'], 1)} down to {player['hp']}")
    return check_victory(player, boss)


@print_stats
def player_turn(player, boss, effects, spell_gen):
    global ans
    if part2:
        player['hp'] -= 1
    with resolve_effects(effects):
        winner = check_victory(player, boss)
        if winner is not None:
            return winner
        spell = next(spell_gen)
        if spell is None:
            logger.debug('[PLAYER] No valid spell')
            return boss
        logger.debug(f'[PLAYER] casting {spell["name"]} for {spell["cost"]} mana')
        player['mana'] -= spell['cost']
        ans += spell['cost']
        cast.append(spell['name'])
        if 'duration' in spell:
            effects[spell['name']] = (spell['effect'], (player, boss), spell['duration'])
        else:
            spell['effect'](player, boss)
    return check_victory(player, boss)


def duel(player, boss):
    effects = {}
    spell_gen = get_valid_spell(player, effects)
    winner = player_turn(player, boss, effects, spell_gen)
    while winner is None:
        if ans > 5000:
            return boss
        winner = boss_turn(player, boss, effects)
        if winner is not None:
            return winner
        winner = player_turn(player, boss, effects, spell_gen)
    return winner


spells = {
    'magic_missile': {
        'cost': 53,
        'name': 'magic_missile',
        'effect': magic_missile
    },
    'drain': {
        'cost': 73,
        'name': 'drain',
        'effect': drain
    },
    'shield': {
        'cost': 113,
        'duration': 6,
        'name': 'shield',
        'effect': shield
    },
    'poison': {
        'cost': 173,
        'duration': 6,
        'name': 'poison',
        'effect': poison
    },
    'recharge': {
        'cost': 229,
        'duration': 5,
        'name': 'recharge',
        'effect': recharge
    }
}

data = open('in').read().split('\n')
bhp = int(data[0].split(': ')[1])
bdm = int(data[1].split(': ')[1])

bstats = {'name': 'boss', 'hp': bhp, 'mana': 0, 'dmg': bdm, 'arm': 0}
pstats = {'name': 'player', 'hp': 50, 'mana': 500, 'dmg': 0, 'arm': 0}

# part 1
part2 = False
m = float('inf')
best = None

for i in range(10**4):
    ans = 0
    cast = []
    winner = duel(pstats.copy(), bstats.copy())
    if ans < m and winner['name'] == 'player':
        m = ans
        best = cast
print(m, best)

# part 2
part2 = True
m = float('inf')
best = None

for i in range(5*10**4):
    ans = 0
    cast = []
    winner = duel(pstats.copy(), bstats.copy())
    if ans < m and winner['name'] == 'player':
        m = ans
        best = cast
print(m, best)
