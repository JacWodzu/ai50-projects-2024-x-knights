from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
knowledge0 = And(
    Or(AKnight, AKnave),  
    Not(And(AKnight, AKnave)),  
    Implication(AKnight, And(AKnight, AKnave)),  
    Implication(AKnave, Not(And(AKnight, AKnave)))  
)

# Puzzle 1
knowledge1 = And(
    Or(AKnight, AKnave),  
    Or(BKnight, BKnave),  
    Implication(AKnight, And(AKnave, BKnave)),  # A saying they are both knaves
    Implication(AKnave, Not(And(AKnave, BKnave)))  # If A is a knave, it's not possible for them to both be knaves
) 

# Puzzle 2
knowledge2 = And(
    Or(AKnight, AKnave),  
    Or(BKnight, BKnave),  
    Implication(AKnight, Biconditional(AKnight, BKnight)),  # If A is a knight, B is a knight
    Implication(AKnave, Not(Biconditional(AKnight, BKnight))),  # If A is a knave, B is not a knight (knave)
    Implication(BKnight, Not(Biconditional(AKnight, AKnave))),  # If B is knight, then A is a knave
    Implication(BKnave, Biconditional(AKnight, AKnave))  # If B is a knave, A is not a knave (so A is a knight)
)

# Puzzle 3
knowledge3 = And(
    Or(AKnight, AKnave),  
    Or(BKnight, BKnave),  
    Or(CKnight, CKnave),  
    Biconditional(AKnight, Or(AKnight, AKnave)),  # A says either
    Implication(BKnight, AKnave),                    # If B is a knight, then A should be a knave
    Implication(BKnave, AKnight),                    # If B is a knave, then A should be a knight
    Implication(BKnight, CKnight),                   # If B is a knight, then C is indicated to be a knave
    Implication(BKnave, CKnave),                   # If B is a knave, C is supposed to be a knight
    Implication(CKnight, AKnight)                   # If C is knight, then A must be knight
)

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
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
