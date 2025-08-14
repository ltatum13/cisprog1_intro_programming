stroke_num = int(input())
par_num = int(input())
score_name = ""

if (par_num < 3) or (par_num > 5):
    print('Par ' + str(par_num) + ' in ' + str(stroke_num) + ' strokes is Error')

elif (stroke_num < (par_num - 2)) or ((par_num + 1) < stroke_num):
    print('Par ' + str(par_num) + ' in ' + str(stroke_num) + ' strokes is Error')

elif stroke_num == par_num - 2:
    score_name = 'Eagle'
    print('Par ' + str(par_num) + ' in ' + str(stroke_num) + ' strokes is ' + str(score_name))

elif stroke_num == par_num - 1:
    score_name = 'Birdie'
    print('Par ' + str(par_num) + ' in ' + str(stroke_num) + ' strokes is ' + str(score_name))

elif stroke_num == par_num:
    score_name = 'Par'
    print('Par ' + str(par_num) + ' in ' + str(stroke_num) + ' strokes is ' + str(score_name))

elif stroke_num == par_num + 1:
    score_name = 'Bogey'
    print('Par ' + str(par_num) + ' in ' + str(stroke_num) + ' strokes is ' + str(score_name))