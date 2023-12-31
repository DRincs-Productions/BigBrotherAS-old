
label cam0_ann_sleep:
    $ renpy.show('Ann cams sleep '+cam_poses_manager(ann, ['01', '02', '03'])+ann.dress, at_list=[laptop_screen])

    show FG cam-shum-act at laptop_screen
    if 'ann_sleep' not in cam_flag:
        $ cam_flag.append('ann_sleep')
        Max_01 "Как же повезло, что у меня такая горячая мама... Выглядит потрясающе, аж глаза отрывать не хочется!"
    return

label cam0_ann_shower:
    if tm[-2:] < '20' and ann.dress_inf != '00a':
        show FG cam-shum-noact at laptop_screen
        if 'ann_not_shower' not in cam_flag:
            $ cam_flag.append('ann_not_shower')
            if len(house[3].cams)>1:
                Max_09 "Мамы не видно через эту камеру... Может посмотреть через другую?"
            elif True:
                Max_09 "Мамы не видно через эту камеру..."
    elif True:
        $ ann.dress_inf = '00a'
        $ renpy.show('Ann cams shower 0'+str(cam_poses_manager(ann, [x for x in range(1, 10)])), at_list=[laptop_screen])
        show other cam-shower-water at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'ann_shower' not in cam_flag:
            $ cam_flag.append('ann_shower')
            Max_04 "Зрелище просто потрясающее... У меня очень горячая мама!"
    return

label cam1_ann_shower:
    if tm[-2:] < '20' and ann.dress_inf != '00a':

        if ann.dress_inf != '04a':
            $ _m1_ann_cam__r1 = {'04c':'a', '04d':'b', '02b':'c', '00':'d', '00a':'d'}[ann.dress_inf]
        elif True:
            $ _m1_ann_cam__r1 = renpy.random.choice(['a', 'b', 'c', 'd'])
            $ ann.dress_inf = {'a':'04c', 'b':'04d', 'c':'02b', 'd':'00'}[_m1_ann_cam__r1]

        $ renpy.show('Ann cams bath-mirror '+cam_poses_manager(ann, ['01', '02', '03'], 1)+_m1_ann_cam__r1, at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        if 'ann_bath_mirror' not in cam_flag:
            $ cam_flag.append('ann_bath_mirror')






            Max_03 "Мама, перед тем, как принять душ, красуется перед зеркалом. Глядя на эту красоту, можно мечтать лишь об одном!"
    elif True:

        show FG cam-shum-noact at laptop_screen
        if 'ann_shower1' not in cam_flag:
            $ cam_flag.append('ann_shower1')
            Max_09 "Мамы не видно через эту камеру... Может посмотреть через другую?"
    return

label cam0_ann_yoga:
    if int(tm[3:4])%3 == 0:
        $ renpy.show('Ann cams yoga 0'+str(renpy.random.randint(1, 3))+ann.dress, at_list=[laptop_screen])
    elif int(tm[3:4])%3 == 1:
        $ renpy.show('Ann cams yoga 0'+str(renpy.random.randint(4, 6))+ann.dress, at_list=[laptop_screen])
    elif True:
        $ renpy.show('Ann cams yoga 0'+str(renpy.random.randint(7, 9))+ann.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_yoga' not in cam_flag:
        $ cam_flag.append('ann_yoga')
        Max_02 "Мама, как и всегда в это время, занимается йогой. Здесь, хоть в какой позе, она выглядит очень сексуально..."
    return

label cam1_ann_yoga:
    show FG cam-shum-noact at laptop_screen
    if 'ann_yoga1' not in cam_flag:
        $ cam_flag.append('ann_yoga1')
        Max_09 "Через эту камеру ничего не видно... Может посмотреть через другую?"
    return

label cam0_ann_cooking:
    $ renpy.show('Ann cams cooking 01'+ann.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen

    if 'ann_cooking' not in cam_flag:
        $ cam_flag.append('ann_cooking')
        if tm < '12:00':
            Max_01 "Как и всегда, мама готовит завтрак. Вроде, ничего интересного, но она всё равно лучшая..."
        elif True:
            Max_01 "Мама сегодня готовит ужин. Будет очень вкусно..."
    return

label ann_cam_dress_inf(r1):
    $ ann.dress_inf = {
            '01':'02e',
            '01a':'02c',
            '02':'02',
            '02a':'02a',
            '02b':'02b',
            '03':'02i',
            '03a':'02h',
            '04':'02g',
            '05':'00',
            '06':'00',
            '07':'00',
            '08':'00',
            '09':'02j',
            '09a':'02d',
            '10':'01',
            '11':'01a',
            '12':'01',
        }[r1]
    return

label cam0_ann_dressed_work:
    if 'ann_dressed' in cam_flag:
        $ renpy.show('Ann cams dressed 11', at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        $ ann.dress_inf = '01d'
        if 'ann_dressed_txt' not in cam_flag:
            $ cam_flag.append('ann_dressed_txt')
            Max_09 "Ничего интересного я здесь уже не увижу, мама полностью оделась."
        return

    $ cam_flag.append('ann_dressed')

    $ Wait(10)
    $ _m1_ann_cam__list = ['03', '03a', '04'] if ann.dress=='d' else ['01', '01a', '02', '02a', '02b']
    $ _m1_ann_cam__ran1 = renpy.random.choice(_m1_ann_cam__list)
    call ann_cam_dress_inf (_m1_ann_cam__ran1) from _call_ann_cam_dress_inf

    $ renpy.show('Ann cams dressed '+_m1_ann_cam__ran1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_07 "Вот и мама наряжается, чтобы отправиться на работу..."
        "{i}продолжать смотреть{/i}" if True:
            pass
        "{i}достаточно{/i}" if True:
            jump open_site

    $ _m1_ann_cam__ran1 = renpy.random.choice(['05','06','07','08'])
    $ ann.dress_inf = '00'
    $ renpy.show('Ann cams dressed '+_m1_ann_cam__ran1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_02 "Ох! Голая мама - это восхитительное зрелище..."
        "{i}продолжать смотреть{/i}" if True:
            pass
        "{i}достаточно{/i}" if True:
            jump open_site


    $ Wait(10)
    $ _m1_ann_cam__ran1 = renpy.random.choice(['09', '09a'])
    call ann_cam_dress_inf (_m1_ann_cam__ran1) from _call_ann_cam_dress_inf_1
    $ renpy.show('Ann cams dressed '+_m1_ann_cam__ran1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    Max_04 "Да уж, её округлости равнодушным не оставят никого!"

    return

label cam0_ann_dressed_shop:
    if 'ann_dressed' in cam_flag:
        $ renpy.show('Ann cams dressed 11', at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        $ ann.dress_inf = '01d'
        if 'ann_dressed_txt' not in cam_flag:
            $ cam_flag.append('ann_dressed_txt')
            Max_09 "Ничего интересного я здесь уже не увижу, мама полностью оделась."
        return

    $ cam_flag.append('ann_dressed')

    $ Wait(10)
    $ _m1_ann_cam__list = ['03', '03a', '04'] if ann.dress=='d' else ['01', '01a', '02', '02a', '02b']
    $ _m1_ann_cam__ran1 = renpy.random.choice(_m1_ann_cam__list)
    call ann_cam_dress_inf (_m1_ann_cam__ran1) from _call_ann_cam_dress_inf_2

    $ renpy.show('Ann cams dressed '+_m1_ann_cam__ran1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_07 "Вот и мама наряжается, чтобы отправиться на шопинг..."
        "{i}продолжать смотреть{/i}" if True:
            pass
        "{i}достаточно{/i}" if True:
            jump open_site

    $ _m1_ann_cam__ran1 = renpy.random.choice(['05','06','07','08'])
    $ ann.dress_inf = '00'
    $ renpy.show('Ann cams dressed '+_m1_ann_cam__ran1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_02 "Ох! Голая мама - это восхитительное зрелище..."
        "{i}продолжать смотреть{/i}" if True:
            pass
        "{i}достаточно{/i}" if True:
            jump open_site


    $ Wait(10)
    $ _m1_ann_cam__ran1 = '10'
    call ann_cam_dress_inf (_m1_ann_cam__ran1) from _call_ann_cam_dress_inf_3
    $ renpy.show('Ann cams dressed '+_m1_ann_cam__ran1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    Max_04 "Да уж, её округлости равнодушным не оставят никого!"
    return

label cam0_ann_resting:
    if tm < '19:00':
        $ renpy.show('Ann cams relax-morning '+cam_poses_manager(ann, ['01', '02', '03'])+ann.dress, at_list=[laptop_screen])
    elif True:
        $ renpy.show('Ann cams relax-evening '+cam_poses_manager(ann, ['01', '02', '03'])+ann.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_resting' not in cam_flag:
        $ cam_flag.append('ann_resting')
        Max_01 "Мама даже когда отдыхает, выглядит очень сексуально..."
    return

label cam0_ann_read:
    $ renpy.show('Ann cams reading '+cam_poses_manager(ann, ['01', '02', '03'])+ann.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_read' not in cam_flag:
        $ cam_flag.append('ann_read')
        Max_01 "Мама увлечённо читает. Вроде бы ничего особенного, а смотреть на её округлые формы всё равно приятно!"
    return

label cam0_ann_sun:
    $ renpy.show('Ann cams sun '+cam_poses_manager(ann, ['01', '02', '03', '04', '05', '06']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_sun' not in cam_flag:
        $ cam_flag.append('ann_sun')
        Max_01 "Самая горячая мама на свете загорает! Не повезло тем зрителям, которые это пропускают..."
    return

label cam1_ann_sun:
    show FG cam-shum-noact at laptop_screen
    if 'ann_sun1' not in cam_flag:
        $ cam_flag.append('ann_sun1')
        Max_09 "Через эту камеру ничего не видно... Может посмотреть через другую?"
    return

label cam0_ann_swim:
    show FG cam-shum-noact at laptop_screen
    if 'ann_swim0' not in cam_flag:
        $ cam_flag.append('ann_swim0')
        if len(house[6].cams)>1:
            Max_09 "Ничего толком не видно... Стоит взглянуть через другую камеру..."
        elif True:
            Max_09 "Ничего не разглядеть... Нужно установить камеру, которая охватила бы весь бассейн..."
    return

label cam1_ann_swim:
    $ renpy.show('Ann cams swim '+cam_poses_manager(ann, ['01', '02', '03', '04']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_swim1' not in cam_flag:
        $ cam_flag.append('ann_swim1')
        Max_01 "На маму во дворе всегда приятно посмотреть..."
    return

label cam0_ann_alice_sun:
    $ renpy.show('Alice cams sun '+cam_poses_manager(alice, ['01', '02', '03', '04', '05', '06']), at_list=[laptop_screen])
    $ renpy.show('Ann cams sun '+cam_poses_manager(ann, ['01', '02', '03', '04', '05', '06']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_sun' not in cam_flag:
        $ cam_flag.append('ann_sun')
        $ cam_flag.append('alice_sun')
        Max_01 "Две загорающих красотки - лучше чем одна..."
    return

label cam1_ann_alice_sun:
    show FG cam-shum-noact at laptop_screen
    if 'ann_sun1' not in cam_flag:
        $ cam_flag.append('ann_sun1')
        Max_09 "Ничего толком не видно... Стоит взглянуть через другую камеру..."
    return

label cam0_ann_alice_swim:
    show FG cam-shum-noact at laptop_screen
    if 'ann_swim0' not in cam_flag:
        $ cam_flag.append('ann_swim0')
        if len(house[6].cams)>1:
            Max_09 "Ничего толком не видно... Стоит взглянуть через другую камеру..."
        elif True:
            Max_09 "Ничего не разглядеть... Нужно установить камеру, которая охватила бы весь бассейн..."
    return

label cam1_ann_alice_swim:






    $ _m1_ann_cam__alice_pose = cam_poses_manager(alice, ['01', '02', '03', '04'])
    $ _m1_ann_cam__ann_pose_list = {
            '01' : ['01', '03'],
            '02' : ['01', '03'],
            '03' : ['01', '02', '04'],
            '04' : ['01', '02', '03', '04'],
        }[_m1_ann_cam__alice_pose]
    $ renpy.show('Alice cams swim '+_m1_ann_cam__alice_pose, at_list=[laptop_screen])
    $ renpy.show('Ann cams swim '+cam_poses_manager(ann, _m1_ann_cam__ann_pose_list), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_swim' not in cam_flag:
        $ cam_flag.append('ann_swim')
        $ cam_flag.append('alice_swim')
        Max_01 "Две соблазнительные дамочки в бассейне, что может быть лучше? Только если бы они были ещё и голые!"
    return

label cam0_ann_bath:
    if tm[-2:] < '10':

        show Ann cams bath 01 at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'ann_bath0_st0' not in cam_flag:
            $ cam_flag.append('ann_bath0_st0')
            Max_01 "Такой шикарной попке, как у моей мамы, любая женщина может позавидовать..."
    elif tm[-2:] > '40':

        show Ann cams bath 05 at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'ann_bath0_st1' not in cam_flag:
            $ cam_flag.append('ann_bath0_st1')
            Max_04 "Не вытирайся, мам, ходи мокренькая..."
    elif True:
        $ renpy.show('Ann cams bath '+cam_poses_manager(ann, ['02', '03', '04']), at_list=[laptop_screen,])
        show FG cam-shum-act at laptop_screen
        if 'ann_bath0_st0' not in cam_flag:
            $ cam_flag.append('ann_bath0_st0')
            Max_05 "И зачем нужны все эти эротические ролики в интернете, когда можно посмотреть на мою маму в ванне?!"
    return

label cam1_ann_bath:
    show FG cam-shum-noact at laptop_screen
    if 'ann_bath1' not in cam_flag:
        $ cam_flag.append('ann_bath1')
        Max_09 "Мамы не видно через эту камеру... Может посмотреть через другую?"
    return

label cam0_ann_tv:
    $ renpy.show('Ann cams tv '+cam_poses_manager(ann, ['01', '02', '03']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen

    if 'ann_tv' not in cam_flag:
        $ cam_flag.append('ann_tv')
        Max_01 "Мама, как всегда, отдыхает за просмотром сериала или фильма."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
