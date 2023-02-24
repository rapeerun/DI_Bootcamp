# #  function to print Tic Tac Board

# def tic_t_tac(values):
#     print("\n")
#     print("\t  |    |")
#     print("\t {} |  {} | {}".format(values[0],values[1],values[2]))
#     # print(f"\t {values[0]}|{values[1]}|{values[2]}")
#     print('\t___|____|____')


#     print("\t  |    |")
#     print("\t {} |  {} | {}".format(values[3],values[4],values[5]))
#     # print(f"\t {values[3]}|{values[4]}|{values[5]}")
#     print('\t___|____|____')


#     print("\t  |    |")
#     print("\t {} |  {} | {}".format(values[6],values[7],values[8]))

#     # print(f"\t {values[6]}|{values[7]}|{values[8]}")
#     print('\t___|____|____')
#     print("\n")

# #  function to print the game

# def print_scoreboard(score_board):
#     print("\t--------------------------")
#     print("\t   SCOREBOAD   ")
#     print("\t-------------------")

#     players= list(score_board.keys()) 
#     print("\t", players[0], "\t  ", score_board[players[0]])
#     print("\t", players[1], "\t  ", score_board[players[1]])

#     print("\t----------------\n")

# #  Function to check if any player has won the game

# def check_winner(player_position,current_player):
#     win_combination=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    
# #  loop to check winning combination
#     for x in win_combination:
#         if all ("y in player_position{current_player} for y in x"):
#             return True
#         else:
#             return False
        
# # to check if the game is draw

# def check_draw(player_position):
#     if len(player_position['X']) + len(player_position['O'])==9:
#         return True
#     return False

# #  function for single game
# def single_game(current_position):
#     values=[''for x in range(9)]

#     player_position={'X':[],'O':[]}


# while True:
#     single_game()

#     try:
#         print("Player  ",current_player, )

#  since I was having an issue with the above code as my function was not working for single game I have used the course of week 5 to do the min project with OOP

import random


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_board()

            # taking user input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            # fixing the spot
            self.fix_spot(row - 1, col - 1, player)

            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()







            


    









     
    