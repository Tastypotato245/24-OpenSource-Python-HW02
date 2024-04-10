import hw2_tastypotato245 as me

def checkAndPrint(stat):
    if type(stat) != list:
        return '능력치 값의 형식이 list 형식이 아닙니다. 무언가 코드에 큰 문제가 생긴 것 같아요.'

    if len(stat) != 7:
        return '능력치 list의 길이가 적절하지 않습니다. 무언가 코드에 큰 문제가 생긴 것 같아요.'

    if type(stat[0]) != str:
        return '이름 값의 형식이 str 형식이 아닙니다. mystat에 대한 할당문을 확인해 주세요.'

    if len(stat[0]) == 0:
        return '이름의 길이가 0입니다. 조금 슬프지만 이름은 한 글자 이상으로 지정해 주세요.'
        
    hab = stat[1] + stat[2] + stat[3] + stat[4] + stat[5] + stat[6]

    if type(hab) != int:
        return '능력치의 합이 int 형식이 아닙니다. 이름을 제외한 각 능력치는 int 형식 값으로 지정해 주세요.'

    if hab < 100:
        return '능력치의 합이 100보다 작습니다. 이타적인 마음은 이해하지만 규칙을 준수하려면 딱 100이 되어야 해요.'

    if hab > 100:
        return '능력치의 합이 100보다 큽니다. 규칙을 준수하려면 딱 100이 되어야 해요.'

    return True
   
def test():
    mystat = me.mystat
    
    duel = me.duel
    
    mystat_backup = mystat[:]

    statnames = ['이름', 'STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
    
    print('mystat 테스트. . . ', end='')

    check_result = checkAndPrint(mystat)

    if type(check_result) == bool:
        print('완벽!')
    else:
        print('실패...')
        print('실패 원인: ' + check_result)
        print('대결 규칙 및 코드 내 주석 설명을 다시 확인해 주세요.')
        return



    print('duel() 테스트 시작.')
    print('능력치가 다른 캐릭터와 대결하는 경우 테스트.')
    c = any(n < 0 for n in mystat[1:])
    f = False

    enemystat = mystat[:]

    idx_from = 1

    while idx_from < 6:
        idx_to = idx_from + 1

        while idx_to < 7:
            print('----' + statnames[idx_from] + '-' + statnames[idx_to] + ' 테스트. . . ', end='')

            if c:
                max_enemystat_from = mystat[idx_from] + 100
                enemystat[idx_from] = mystat[idx_from] - 100
                enemystat[idx_to] = mystat[idx_to] + 100

            if not c:
                max_enemystat_from = mystat[idx_from] + mystat[idx_to]
                enemystat[idx_from] = 0
                enemystat[idx_to] = max_enemystat_from

            while enemystat[idx_from] <= max_enemystat_from:
                if enemystat[idx_from] != mystat[idx_from]:
                    enemystat_backup = enemystat[:]

                    result_left = duel(mystat, enemystat)

                    if result_left == None:
                        print('duel()이 결과를 return하지 않음!')
                        print('left : ' + str(mystat_backup) + ' (내 캐릭터)')
                        print('right: ' + str(enemystat_backup))
                        return

                    if type(result_left) != int and type(result_left) != float or result_left == 0:
                        print('duel()이 부적절한 값을 return함!')
                        print('left : ' + str(mystat_backup) + ' (내 캐릭터)')
                        print('right: ' + str(enemystat_backup))
                        print('return값: ' + str(result_left))
                        return

                    if result_left > 0:
                        f = True

                        
                    for idx in range(7):
                        if mystat_backup[idx] != mystat[idx] or enemystat_backup[idx] != enemystat[idx]:
                            print()
                            print('능력치 변경 시도 발견!')
                            print('실행 전 left : ' + str(mystat_backup) + ' (내 캐릭터)')
                            print('실행 후 left : ' + str(mystat) + ' (내 캐릭터)')
                            print('실행 전 right: ' + str(enemystat_backup))
                            print('실행 후 right: ' + str(enemystat))
                            return


                    result_right = duel(enemystat, mystat)

                    if result_right == None:
                        print('duel()이 결과를 return하지 않음!')
                        print('left: ' + str(enemystat_backup))
                        print('right: ' + str(mystat_backup) + ' (내 캐릭터)')
                        return
                    
                    if type(result_right) != int and type(result_right) != float or result_right == 0:
                        print('duel()이 부적절한 값을 return함!')
                        print('left: ' + str(enemystat_backup))
                        print('right: ' + str(mystat_backup) + ' (내 캐릭터)')
                        print('return값: ' + str(result_right))
                        return

                    if result_right < 0:
                        f = True


                    if result_left * result_right > 0:
                        print('duel()이 일관적이지 않은 결과를 return함!')
                        print(str(mystat_backup) + ' vs ' + str(enemystat_backup) + ' -> ' + str(result_left))
                        print(str(enemystat_backup) + ' vs ' + str(mystat_backup) + ' -> ' + str(result_right))
                        return
                        
                    
                    for idx in range(7):
                        if mystat_backup[idx] != mystat[idx] or enemystat_backup[idx] != enemystat[idx]:
                            print()
                            print('능력치 변경 시도 발견!')
                            print('실행 전 left : ' + str(enemystat_backup))
                            print('실행 후 left : ' + str(enemystat))
                            print('실행 전 right: ' + str(mystat_backup) + ' (내 캐릭터)')
                            print('실행 후 right: ' + str(mystat) + ' (내 캐릭터)')
                            return
                
                # 다음 테스트 준비
                enemystat[idx_from] = enemystat[idx_from] + 1
                enemystat[idx_to] = enemystat[idx_to] - 1

            
            print('완벽!')

            enemystat[idx_to] = mystat[idx_to]
            idx_to = idx_to + 1

        enemystat[idx_from] = mystat[idx_from]
        idx_from = idx_from + 1


    print('능력치가 동일하지만 이름만 다른 캐릭터와 대결하는 경우 테스트. . . ', end='')

    enemystat = mystat[:]
    enemystat[0] = mystat[0][:-1] + chr(ord(mystat[0][-1]) - 1)
    enemystat_backup = enemystat[:]
    
    result_left = duel(mystat, enemystat)

    if result_left == None:
        print('duel()이 결과를 return하지 않음!')
        print('left : ' + str(mystat_backup) + ' (내 캐릭터)')
        print('right: ' + str(enemystat_backup))
        return

    if type(result_left) != int and type(result_left) != float or result_left == 0:
        print('duel()이 부적절한 값을 return함!')
        print('left : ' + str(mystat_backup) + ' (내 캐릭터)')
        print('right: ' + str(enemystat_backup))
        print('return값: ' + str(result_left))
        return

    if result_left > 0:
        f = True

        
    for idx in range(7):
        if mystat_backup[idx] != mystat[idx] or enemystat_backup[idx] != enemystat[idx]:
            print()
            print('능력치 변경 시도 발견!')
            print('실행 전 left : ' + str(mystat_backup) + ' (내 캐릭터)')
            print('실행 후 left : ' + str(mystat) + ' (내 캐릭터)')
            print('실행 전 right: ' + str(enemystat_backup))
            print('실행 후 right: ' + str(enemystat))
            return

    result_right = duel(enemystat, mystat)

    if result_right == None:
        print('duel()이 결과를 return하지 않음!')
        print('left: ' + str(enemystat_backup))
        print('right: ' + str(mystat_backup) + ' (내 캐릭터)')
        return
    
    if type(result_right) != int and type(result_right) != float or result_right == 0:
        print('duel()이 부적절한 값을 return함!')
        print('left: ' + str(enemystat_backup))
        print('right: ' + str(mystat_backup) + ' (내 캐릭터)')
        print('return값: ' + str(result_right))
        return

    if result_right < 0:
        f = True

    if result_left * result_right > 0:
        print('duel()이 일관적이지 않은 결과를 return함!')
        print(str(mystat_backup) + ' vs ' + str(enemystat_backup) + ' -> ' + str(result_left))
        print(str(enemystat_backup) + ' vs ' + str(mystat_backup) + ' -> ' + str(result_right))
        return
        
    
    for idx in range(7):
        if mystat_backup[idx] != mystat[idx] or enemystat_backup[idx] != enemystat[idx]:
            print()
            print('능력치 변경 시도 발견!')
            print('실행 전 left : ' + str(enemystat_backup))
            print('실행 후 left : ' + str(enemystat))
            print('실행 전 right: ' + str(mystat_backup) + ' (내 캐릭터)')
            print('실행 후 right: ' + str(mystat) + ' (내 캐릭터)')
            return


    enemystat[0] = mystat[0][:-1] + chr(ord(mystat[0][-1]) + 1)
    enemystat_backup = enemystat[:]
    
    result_left = duel(mystat, enemystat)

    if result_left == None:
        print('duel()이 결과를 return하지 않음!')
        print('left : ' + str(mystat_backup) + ' (내 캐릭터)')
        print('right: ' + str(enemystat_backup))
        return

    if type(result_left) != int and type(result_left) != float or result_left == 0:
        print('duel()이 부적절한 값을 return함!')
        print('left : ' + str(mystat_backup) + ' (내 캐릭터)')
        print('right: ' + str(enemystat_backup))
        print('return값: ' + str(result_left))
        return

    if result_left > 0:
        f = True

        
    for idx in range(7):
        if mystat_backup[idx] != mystat[idx] or enemystat_backup[idx] != enemystat[idx]:
            print()
            print('능력치 변경 시도 발견!')
            print('실행 전 left : ' + str(mystat_backup) + ' (내 캐릭터)')
            print('실행 후 left : ' + str(mystat) + ' (내 캐릭터)')
            print('실행 전 right: ' + str(enemystat_backup))
            print('실행 후 right: ' + str(enemystat))
            return

    result_right = duel(enemystat, mystat)

    if result_right == None:
        print('duel()이 결과를 return하지 않음!')
        print('left: ' + str(enemystat_backup))
        print('right: ' + str(mystat_backup) + ' (내 캐릭터)')
        return
    
    if type(result_right) != int and type(result_right) != float or result_right == 0:
        print('duel()이 부적절한 값을 return함!')
        print('left: ' + str(enemystat_backup))
        print('right: ' + str(mystat_backup) + ' (내 캐릭터)')
        print('return값: ' + str(result_right))
        return

    if result_right < 0:
        f = True

    if result_left * result_right > 0:
        print('duel()이 일관적이지 않은 결과를 return함!')
        print(str(mystat_backup) + ' vs ' + str(enemystat_backup) + ' -> ' + str(result_left))
        print(str(enemystat_backup) + ' vs ' + str(mystat_backup) + ' -> ' + str(result_right))
        return
        
    
    for idx in range(7):
        if mystat_backup[idx] != mystat[idx] or enemystat_backup[idx] != enemystat[idx]:
            print()
            print('능력치 변경 시도 발견!')
            print('실행 전 left : ' + str(enemystat_backup))
            print('실행 후 left : ' + str(enemystat))
            print('실행 전 right: ' + str(mystat_backup) + ' (내 캐릭터)')
            print('실행 후 right: ' + str(mystat) + ' (내 캐릭터)')
            return

    if f:
        print('완벽? 약간 오묘하기는 한데 이번 과제에서는 봐드릴께용.')
    if not f:
        print('완벽!')
    
    print('duel() 테스트 종료.')
    print('제출 가능!')
        

test()
