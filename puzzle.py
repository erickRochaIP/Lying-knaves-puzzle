from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
Asays0 = And(AKnight, AKnave)
knowledge0 = And(
    Or(AKnight, AKnave),
    Biconditional(AKnave, Not(AKnight)),
    Biconditional(Not(Asays0), AKnave)
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
Asays1 = And(AKnave, BKnave)
knowledge1 = And(
    Or(AKnight, AKnave),
    Biconditional(AKnave, Not(AKnight)),
    Or(BKnight, BKnave),
    Biconditional(BKnave, Not(BKnight)),
    Biconditional(Not(Asays1), AKnave)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
Asays2 = Or(And(AKnave, BKnave), And(AKnight, BKnight))
Bsays2 = Or(And(AKnave, BKnight), And(AKnight, BKnave))
knowledge2 = And(
    Or(AKnight, AKnave),
    Biconditional(AKnave, Not(AKnight)),
    Or(BKnight, BKnave),
    Biconditional(BKnave, Not(BKnight)),
    Biconditional(Not(Asays2), AKnave),
    Biconditional(Not(Bsays2), BKnave)

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
AsaysAKnave = Symbol("A says 'I am a knave'")
AsaysAKnight = Symbol("A says 'A am a knight'")

Bsays31 = (AsaysAKnave)
Bsays32 = (CKnave)
Csays3 = (AKnight)

knowledge3 = And(
    Or(AKnight, AKnave),
    Biconditional(AKnave, Not(AKnight)),
    Or(BKnight, BKnave),
    Biconditional(BKnave, Not(BKnight)),
    Or(CKnight, CKnave),
    Biconditional(CKnave, Not(CKnight)),

    Or(AsaysAKnave, AsaysAKnight),
    Biconditional(AsaysAKnight, Not(AsaysAKnave)),

    Implication(AKnight, AsaysAKnight),
    Implication(AKnave, AsaysAKnight),
    Biconditional(Not(Bsays31), BKnave),
    Biconditional(Not(Bsays32), BKnave),
    Biconditional(Not(Csays3), CKnave)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave, AsaysAKnight, AsaysAKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
