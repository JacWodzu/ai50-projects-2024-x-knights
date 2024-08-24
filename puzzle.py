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
    
    # A's statement: A says "I am a knight" or "I am a knave."
    Implication(AKnight, AKnight),  # If A is a Knight, then A is a Knight.
    Implication(AKnave, Not(AKnight)),  # If A is a Knave, then A is not a Knight.
    
    # B's first statement: "A said 'I am a knave.'"
    Implication(BKnight, Biconditional(AKnight, AKnave)),  # If B is a Knight, A's statement must be true.
    Implication(BKnave, Not(Biconditional(AKnight, AKnave))),  # If B is a Knave, A's statement is false.
    
    # B's second statement: "C is a knave."
    Implication(BKnight, CKnave),  # If B is a Knight, then C is a Knave.
    Implication(BKnave, CKnight),  # If B is a Knave, then C is a Knight.
    
    # C's statement: "A is a Knight."
    Implication(CKnight, AKnight),  # If C is a Knight, A is a Knight.
    Implication(CKnave, AKnave)  # If C is a Knave, A is a Knave.
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
