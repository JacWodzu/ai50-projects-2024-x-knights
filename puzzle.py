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
    Implication(AKnight, Biconditional(AKnight, BKnight)),  
    Implication(AKnave, Not(Biconditional(AKnight, BKnight))),  
    Implication(BKnight, Not(Biconditional(AKnight, BKnight))),  
    Implication(BKnave, Biconditional(AKnight, BKnight))  
)

# Puzzle 3
knowledge3 = And(
    Or(AKnight, AKnave),  # A is either a knight or a knave
    Or(BKnight, BKnave),  # B is either a knight or a knave
    Or(CKnight, CKnave),  # C is either a knight or a knave
    Implication(AKnight, Or(AKnight, AKnave)),  # A says he is a knight or a knave
    Implication(AKnave, Not(Or(AKnight, AKnave))),  # A cannot claim both
    Implication(BKnight, AKnave),  # If B is a knight, A must be a knave
    Implication(BKnave, AKnight),  # If B is a knave, A must be a knight
    Implication(BKnight, CKnight),  # If B is a knight, C is a knave
    Implication(BKnave, CKnave),  # If B is a knave, C is a knight
    Implication(CKnight, AKnight),  # If C is a knight, A is a knight
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
