def check_winner(human,computer,game_history, count):
    if human > computer:
        print('크다')
        game_history.append( (human,'크다' )  )
    elif human < computer:
        print('작다')
        game_history.append( (human,'작다' )  )
    else:
        print(f'정답 횟수 : {count}')
        for guess_value, state in game_history:
            print(f'{guess_value} - {state}')
        return True
    return False