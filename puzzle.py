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
    # Each character must either be a Knight or a Knave
    Or(AKnight, AKnave),  
    Or(BKnight, BKnave),  
    Or(CKnight, CKnave),  
    
    # A's statement, since we know A must be a knight
    Implication(AKnight, And(Not(AKnave), Not(And(AKnight, AKnave)))),  # A claims to be a knight
    Implication(AKnave, Not(AKnight)),  # If A is a knave, then they can't be the knight

    # B's statements
    Implication(BKnight, Or(AKnave)),  # B claims that A said 'I am a knave' if B is a knight
    Implication(BKnave, Not(Or(AKnave))),  # If B is a knave, then A cannot be a knave

    # Truth about C from B and C's statement
    Implication(BKnight, CKnight),  # If B is a knight, C is a knave
    Implication(BKnave, CKnave),     # If B is a knave, C is a knight 
    Implication(CKnight, AKnight)     # C claims A is a knight, which is true
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
