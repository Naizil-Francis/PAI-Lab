import math

def minimax_alpha_beta(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or len(node) == 1:
        return node[0]
    if maximizingPlayer:
        value = -math.inf
        for child in node[1:]:
            value = max(value, minimax_alpha_beta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = math.inf
        for child in node[1:]:
            value = min(value, minimax_alpha_beta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                 break
        return value

tree = [ 3,[5,[9],[1]],
    [
        6,
        [2],
        [0]
    ]
]

result = minimax_alpha_beta(tree, 3, -math.inf, math.inf, True)
print("Optimal value:", result)
