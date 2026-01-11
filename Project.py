import random

SUITS = ["S", "H", "D", "C"]
RANKS = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

SCORE_MAP = {
    "2":2, "3":3, "4":4, "5":5, "6":6,
    "7":7, "8":8, "9":9, "10":10,
    "J":11, "Q":12, "K":13, "A":20
}


def build_deck():
    deck = []
    for s in SUITS:
        for r in RANKS:
            deck.append(r + s)
    return deck


def deal_hands(deck, players):
    random.shuffle(deck)
    hands = {}

    for p in players:
        hands[p] = []

    index = 0
    for i in range(5):
        for p in players:
            hands[p].append(deck[index])
            index += 1

    return hands


def hand_score(hand):
    total = 0
    for card in hand:
        value = card[:-1]
        total += SCORE_MAP[value]
    return total


def tie_signature(hand):
    counts = {}

    for card in hand:
        value = card[:-1]
        if value not in counts:
            counts[value] = 1
        else:
            counts[value] += 1

    max_count = 0
    for v in counts.values():
        if v > max_count:
            max_count = v

    best_ranks = []
    for r in counts:
        if counts[r] == max_count:
            best_ranks.append(SCORE_MAP[r])

    best_ranks.sort(reverse=True)
    return max_count, best_ranks


def compare_players(p1, h1, p2, h2):
    s1 = hand_score(h1)
    s2 = hand_score(h2)

    if s1 > s2:
        return 1
    if s1 < s2:
        return -1

    t1 = tie_signature(h1)
    t2 = tie_signature(h2)

    if t1 > t2:
        return 1
    if t1 < t2:
        return -1

    return 0


def round_results(hands):
    players = list(hands.keys())
    best = [players[0]]

    for p in players[1:]:
        result = compare_players(best[0], hands[best[0]], p, hands[p])
        if result == -1:
            best = [p]
        elif result == 0:
            best.append(p)

    real_best = []
    for p in players:
        is_best = True
        for q in players:
            if p != q:
                if compare_players(p, hands[p], q, hands[q]) == -1:
                    is_best = False
        if is_best:
            real_best.append(p)

    best = real_best

    if len(best) == 1:
        losers = []
        for p in players:
            if p not in best:
                losers.append(p)
    else:
        losers = []

    return best, losers


def print_round(hands):
    print("\n--- ROUND ---")
    for p in hands:
        cards = ""
        for c in hands[p]:
            cards += c + " "
        score = hand_score(hands[p])
        same, ranks = tie_signature(hands[p])
        print(p, ":", cards, "| score =", score, "| max same =", same)


def play_game(players):
    active = players[:]

    while len(active) > 1:
        deck = build_deck()
        hands = deal_hands(deck, active)

        print_round(hands)

        best, losers = round_results(hands)

        if len(losers) == 0:
            print("TIE – nobody eliminated")
        else:
            worst = losers[0]
            for p in losers:
                if compare_players(worst, hands[worst], p, hands[p]) == 1:
                    worst = p

            active.remove(worst)
            print("Eliminated:", worst)
            print("Remaining:", active)

    print("\nWINNER:", active[0])



players = []

try:
    players.append(input("Enter player 1 name: "))
    players.append(input("Enter player 2 name: "))
    players.append(input("Enter player 3 name: "))

    play_game(players)

except Exception as e:
    print("An error occurred:", e)




