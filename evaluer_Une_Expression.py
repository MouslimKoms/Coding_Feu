import ast
import operator as op

# Dictionnaire des opérations autorisées pour les cinq opérateurs
operators = {
    ast.Add: op.add,     # Addition
    ast.Sub: op.sub,     # Soustraction
    ast.Mult: op.mul,    # Multiplication
    ast.Div: op.truediv, # Division
    ast.Mod: op.mod      # Modulo
}

def eval_expression(expr):
    """
    Évalue une expression arithmétique string et retourne le résultat.
    
    Parameters:
    expr (str): L'expression arithmétique à évaluer.
    
    Returns:
    float: Le résultat de l'évaluation de l'expression.
    """
    try:
        # Analyse l'expression en un arbre de syntaxe
        node = ast.parse(expr, mode='eval')
        # Évaluer l'expression en parcourant l'arbre de syntaxe
        return eval_node(node.body)
    except Exception as e:
        return f"Erreur: {str(e)}"

def eval_node(node):
    """
    Évalue un noeud de l'arbre de syntaxe pour l'expression.
    
    Parameters:
    node (ast.AST): Le noeud de l'arbre de syntaxe à évaluer.
    
    Returns:
    float: Le résultat de l'évaluation du noeud.
    """
    if isinstance(node, ast.BinOp):
        # Si le noeud est une opération binaire, évaluer les deux côtés
        left = eval_node(node.left)  # Évalue le côté gauche de l'opération
        right = eval_node(node.right)  # Évalue le côté droit de l'opération
        # Effectuer l'opération via le dictionnaire 'operators'
        return operators[type(node.op)](left, right)
    elif isinstance(node, ast.Constant):
        # Si le noeud est un nombre, retourner la valeur numérique
        return node.n
    else:
        # Si le noeud est d'un type incompatible, lever une exception
        raise TypeError(f'Node de type incompatible: {type(node)}')

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python evaluer_Une_Expression.py '< Expression>'")
    else:
        expression = sys.argv[1]
        print(eval_expression(expression))  # Affiche le résultat de l'expression.





    
    
