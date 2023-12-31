init offset = -1









style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"

style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)


















screen say(who, what):

    style_prefix "say"

    if not _in_replay:
        key "K_F5" action [SetVariable("number_quicksave", number_quicksave+1), QuickSave()]
        key "K_F8" action QuickLoad()
    if _preferences.language is None:
        key "l" action Language("english")
        key "д" action Language("english")
    else:
        key "l" action Language(None)
        key "д" action Language(None)

    window:
        id "window"
        if not persistent.transparent_textbox:
            background Image("gui/textbox.png", xalign=0.5, yalign=1.0)
        hbox xsize gui.dialogue_xpos + gui.dialogue_width + 20:

            ysize gui.textbox_height - 35
            spacing 5
            viewport mousewheel "change" id "vp_say":

                has frame background None
                text what id "what" justify False
            vbar value YScrollValue("vp_say") style "say_vscroll"

    add SideImage() xalign 0.0 yalign 1.0 zoom 0.85
    if renpy.variant('small'):
        use quick_menu


init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style say_vscroll is vscrollbar:
    unscrollable "hide"

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height




style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos











screen input(prompt):
    style_prefix "input"

    window:

        has vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width










screen choice(items):

    style_prefix "choice"
    if not _in_replay:
        key "K_F5" action [SetVariable("number_quicksave", number_quicksave+1), QuickSave()]
        key "K_F8" action QuickLoad()
    if _preferences.language is None:
        key "l" action Language("english")
        key "д" action Language("english")
    else:
        key "l" action Language(None)
        key "д" action Language(None)

    frame background None area (1380, 815, 525, 245):

        has hbox spacing 5
        viewport spacing 0 draggable True mousewheel True id "vp_choice":

            has vbox xfill True spacing -3
            $ yy = 0
            for i in items:
                $ yy+=1
                button action i.action background None:
                    xpadding 0 ypadding 0 xmargin 0 ymargin 0
                    textbutton i.caption action i.action yalign .0 xpos 30
                    foreground "interface marker"

                key str(yy) action i.action
        vbar value YScrollValue("vp_choice") style "choice_vscroll"
    if len(items) == 1:
        key "K_SPACE" action items[0].action



define config.narrator_menu = True

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    size gui.text_size

style choice_vscroll is vscrollbar:
    unscrollable "hide"







screen quick_menu():


    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("История") action ShowMenu('history')
            textbutton _("Пропуск") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Авто") action Preference("auto-forward", "toggle")
            textbutton _("Сохранить") action ShowMenu('save')
            textbutton _("Б.Сохр") action QuickSave()
            textbutton _("Б.Загр") action QuickLoad()
            textbutton _("Опции") action ShowMenu('preferences')







default quick_menu = renpy.variant("small")

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")











screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        ypos 180

        spacing gui.navigation_spacing

        button action Start() style "nav_button":
            textbutton _("Начать новую игру") action Start()

        button action ShowMenu("history") style "nav_button":
            textbutton _("История") action ShowMenu("history")

        button action ShowMenu("load") style "nav_button":
            textbutton _("Загрузить игру") action ShowMenu("load")

        button action ShowMenu("save") style "nav_button":
            textbutton _("Сохранить игру") action ShowMenu("save")


        button action ShowMenu("preferences") style "nav_button":
            textbutton _("Настройки") action ShowMenu("preferences")

        if _in_replay:

            button action EndReplay(confirm=True) style "nav_button":
                textbutton _("Завершить повтор") action EndReplay(confirm=True)





        button action Quit(confirm=not main_menu) style "nav_button":
            textbutton _("Выйти из игры") action Quit(confirm=not main_menu)

        if renpy.variant("small"):

            button action EndReplay(confirm=True) style "nav_button":
                top_margin 200
                textbutton _("Назад") action Return()

style nav_button:
    background None
    xsize 300
    padding (0, 0, 0, 0)
    foreground "interface/marker.webp"

style navigation_button_text is gui_button_text:
    font "trebucbd.ttf"
    xpos 30
    yalign .0
    size gui.button_text_size
    idle_color gui.choice_button_text_idle_color
    hover_color gui.text_color
    selected_color gui.text_color






init:
    transform main_logo:
        on idle:
            zoom 1.0
        on hover:
            zoom 1.02

screen main_menu():

    $ recent_save = renpy.newest_slot()




    style_prefix "main_menu" tag menu
    if _preferences.language is None:
        key "l" action Language("english")
        key "д" action Language("english")
    else:
        key "l" action Language(None)
        key "д" action Language(None)

    add gui.main_menu_background

    vbox xalign 0.5 spacing -60:
        frame xalign 0.5 xsize 1235 background None:
            text "BIG BROTHER" font "BRLNSB.ttf" color "#FFFFFF" size 178 xalign .5 outlines [( 1, "#999999", 0, 2)]
        frame xalign 0.5 xsize 1235 background None:
            text "ANOTHER STORY" font "BRLNSB.ttf" color "#FFFFFF80" size 48 xalign 0.0 outlines [( 1, "#99999960", 1, 2)]
            $ _m1_screens__short_ver = config.version[0:4]
            text "v[config.version]" font "BRLNSB.ttf" color "#FFFFFF80" size 48 xalign 1.0 outlines [( 1, "#99999960", 1, 2)]

    imagebutton:
        idle "interface patreon logo"
        action OpenURL("https://www.patreon.com/aleksey90artimages")
        align (0.98, 0.63)
        at main_logo


    frame:
        background "gui/overlay/main_menu.webp"

    hbox align (0.5, 1.0) spacing 5:
        textbutton _("НОВАЯ ИГРА") action Start()

        if (recent_save is not None):
            $ recent_save_page, recent_save_name = recent_save.split("-")
        else:
            $ recent_save_page = recent_save_name = ""
        textbutton _("ПРОДОЛЖИТЬ"):
            action FileLoad(recent_save_name, confirm=True, page=recent_save_page)
            sensitive (recent_save is not None)
        textbutton _("ЗАГРУЗИТЬ"):
            action ShowMenu("load")
            sensitive (recent_save is not None)

        textbutton _("НАСТРОЙКИ") action ShowMenu("preferences")
        textbutton _("ВЫЙТИ") action Quit(confirm=not main_menu)

style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_button:
    xsize 360

style main_menu_button_text:
    font "hermes.ttf"
    idle_color "#FFFFFF"
    size 48
    xalign 0.5










screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.game_menu_background

    add "interface phon"
    label _("ГЛАВНОЕ МЕНЮ")

    if not renpy.variant('small'):
        imagebutton pos (1740, 100) auto "interface close %s" action Return() focus_mask True at close_zoom

    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    has vbox:
                        spacing 15
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial yinitial

                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    transclude

            else:

                transclude

    use navigation

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 150

style game_menu_navigation_frame:
    xsize 450
    yfill True

style game_menu_content_frame:
    left_margin 10
    right_margin 10
    top_margin 5

style game_menu_viewport:
    xsize 1300

style game_menu_vscrollbar:
    unscrollable gui.unscrollable
    xsize 5

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 150
    ypos 95
    ysize 50

style game_menu_label_text:
    color gui.accent_color
    font "hermes.ttf"
    size gui.title_text_size
    yalign 0.5










screen save_input(prompt="", last="", len=50):
    modal True
    window style "nvl_window":
        has vbox:
            xalign 0.5
            yalign 0.2
            xsize 720
            spacing 50

        text prompt xalign 0.5
        input default last length len style "input"

init -2 python:

    class get_save_name(FileSave):
        def __init__(self, name, confirm=True, newest=True, page=None, cycle=False):
            super(get_save_name,self).__init__(name=name,confirm=confirm,newest=newest,page=page,cycle=cycle)
        def __call__(self):
            renpy.call_in_new_context("get_save_name")
            return super(get_save_name,self).__call__()

label get_save_name:
    show screen save
    if persistent._file_page != "quick":
        if persistent.request_savename:
            $ save_name = renpy.call_screen("save_input", _("Введите описание файла сохранения:"), last_save_name, 50)
            $ last_save_name = save_name
        elif True:
            $ number_save += 1
            $ save_name = 'Save '+str(number_save)

    $ renpy.retain_after_load()
    return

init python:
    def get_extra_stuff(data):
        if '$@' in data:
            s_desc, load_wd, load_tm, load_day, load_quick, load_auto = data.split('$@')
            if persistent._file_page == "auto":
                s_desc = "AUTO-"+load_auto
            elif persistent._file_page == "quick":
                s_desc = "QUICK-"+load_quick
        else:
            load_wd = ''
            load_tm = ''
            load_day = ''
            s_desc =_('(Нет описания)')
        
        
        return (s_desc, load_wd, load_tm, load_day)

screen save():
    tag menu


    use file_slots("save")

screen load():
    tag menu


    use file_slots("load")

screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("{} страница"), auto=_("Автосохранения"), quick=_("Быстрые сохранения"))

    use game_menu(title):

        fixed:
            if persistent.grid_vbox == "grid":
                imagebutton pos (1200, 0) idle "gui/button/vbox_idle.webp" hover "gui/button/vbox_hover.webp" action SetVariable("persistent.grid_vbox", "vbox")
            else:
                imagebutton pos (1200, 0) idle "gui/button/grid_idle.webp" hover "gui/button/grid_hover.webp" action SetVariable("persistent.grid_vbox", "grid")




            order_reverse True



            frame xsize 1300 background None xalign 0.0:
                has button:
                    style "page_label"

                    key_events True
                    xalign .5
                    action NullAction()

                input:
                    style "page_label_text"
                    value page_name_value


            frame xsize 1300 ysize 735 background None xalign 0.0 yalign 0.5:
                if persistent.grid_vbox == "grid":
                    vpgrid cols gui.file_slot_cols:
                        mousewheel "change"
                        draggable True
                        scrollbars "vertical"

                        style_prefix "slot"

                        xalign 0.5
                        yalign 0.5

                        spacing gui.slot_spacing

                        for i in range(gui.file_slot_cols * gui.file_slot_rows):

                            $ slot = i + 1

                            $ load_day      = FileJson(slot, "day")
                            $ load_tm       = FileJson(slot, "tm")
                            $ load_wd       = FileJson(slot, "wd")
                            if load_day is None:
                                $ s_description, load_wd, load_tm, load_day = get_extra_stuff(FileSaveName(slot))
                            else:
                                if persistent._file_page == "auto":
                                    $ s_description = FileJson(slot, "auto")
                                    if s_description:
                                        $ s_description = "AUTO-"+str(s_description)
                                elif persistent._file_page == "quick":
                                    $ s_description = FileJson(slot, "quick")
                                    if s_description:
                                        $ s_description = "QUICK-"+str(s_description)
                                else:
                                    $ s_description = FileJson(slot, "desc")

                            button:
                                if title == "save":
                                    action get_save_name(slot)
                                else:
                                    action FileAction(slot)

                                vbox:

                                    add FileScreenshot(slot)

                                    text FileTime(slot, format=_("{#file_time}%a, %d %b %Y, %H:%M"), empty=_("Пустой слот")):
                                        style "slot_time_text"

                                    text "[s_description]" style "slot_name_text"

                                if load_day != "":
                                    vbox xalign 0.95:
                                        text "[load_wd!t], [load_tm]" style "ext_text"
                                        text _("ДЕНЬ [load_day]") style "ext_text"


                                key "save_delete" action FileDelete(slot)
                else:
                    vpgrid cols 1:
                        mousewheel "change"
                        draggable True
                        scrollbars "vertical"

                        xalign 0.5
                        yalign 0.5

                        spacing gui.slot_spacing

                        for i in range(gui.file_slot_cols * gui.file_slot_rows):

                            $ slot = i + 1
                            $ load_day      = FileJson(slot, "day")
                            $ load_tm       = FileJson(slot, "tm")
                            $ load_wd       = FileJson(slot, "wd")
                            if load_day is None:
                                $ s_description, load_wd, load_tm, load_day = get_extra_stuff(FileSaveName(slot))
                            else:
                                if persistent._file_page == "auto":
                                    $ s_description = FileJson(slot, "auto")
                                    if s_description:
                                        $ s_description = "AUTO-"+str(s_description)
                                elif persistent._file_page == "quick":
                                    $ s_description = FileJson(slot, "quick")
                                    if s_description:
                                        $ s_description = "QUICK-"+str(s_description)
                                else:
                                    $ s_description = FileJson(slot, "desc")

                            button xsize 1280 ysize 80:
                                if title == "save":
                                    action get_save_name(slot)
                                else:
                                    action FileAction(slot)
                                idle_background "gui/button/idle_save_button.webp"
                                insensitive_background "gui/button/insensitive_save_button.webp"
                                hover_background "gui/button/hover_save_button.webp"

                                fixed:
                                    text "[s_description]":
                                        color gui.hover_color
                                        size 36
                                        xalign .05
                                        yalign .5
                                    text FileTime(slot, format=_("{#file_time}%d %b %Y, %H:%M"), empty=_("Пустой слот")):
                                        size 20
                                        color gui.hover_color
                                        xalign .95
                                        yalign .99

                                    if load_day != "":
                                        text "[load_wd!t], [load_tm], ДЕНЬ [load_day]":
                                            size 30
                                            color gui.hover_color
                                            xalign .95
                                            yalign .01

                                key "save_delete" action FileDelete(slot)


            frame xsize 1300 background None xalign 0.0 yalign 1.0:
                has hbox:
                    style_prefix "page"

                    xalign 0.5

                    spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()


                textbutton _("{#auto_page}Автосохр.") action FilePage("auto")


                textbutton _("{#quick_page}Быстрые сохр.") action FilePage("quick")


                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text:
    color gui.hover_color

style ext_text:
    font "seguisb.ttf"
    size 28
    xalign 1.
    color "#ffffff"
    outlines [( 1, "#000000", 0, 0)]

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")

style slot_vscrollbar:
    xsize 5

style slot_vscrollbar:
    variant 'small'
    xsize 25







screen preferences():
    tag menu


    use game_menu(_("Настройки"), scroll="viewport"):

        vbox xpos 100:

            hbox:
                box_wrap True

                vbox:
                    if renpy.variant("pc"):
                        vbox:
                            style_prefix "radio"
                            label _("Режим экрана")
                            textbutton _("Оконный") action Preference("display", "window")
                            textbutton _("Полный") action Preference("display", "fullscreen")
                    vbox:
                        style_prefix "radio"
                        label _("Сторона отката")
                        textbutton _("Отключено") action Preference("rollback side", "disable")
                        textbutton _("Левая") action Preference("rollback side", "left")
                        textbutton _("Правая") action Preference("rollback side", "right")

                vbox:
                    vbox:
                        style_prefix "check"
                        label _("Пропуск")
                        textbutton _("Всего текста") action Preference("skip", "toggle")
                        textbutton _("После выборов") action Preference("after choices", "toggle")
                        textbutton _("Переходов") action InvertSelected(Preference("transitions", "toggle"))
                    vbox:
                        style_prefix "radio"
                        label _("Язык")
                        textbutton _("Русский") action Language(None)
                        textbutton _("English") action Language("english")
                        textbutton _("Deutsch") action Language("deutsch")

                vbox:
                    spacing 20
                    vbox:
                        style_prefix "radio"
                        label _("Дополнительно")
                        textbutton _("Patreon-интро") action SetVariable("persistent.orint", False)
                        textbutton _("Оригинальное интро") action SetVariable("persistent.orint", True)
                    vbox:
                        style_prefix "check"

                        textbutton _("Запрашивать название при сохранении") action ToggleVariable("persistent.request_savename")
                        textbutton _("Прозрачное текстовое окно") action ToggleVariable("persistent.transparent_textbox")
                        textbutton _("Отображать все \"Возможности\"") action ToggleVariable("persistent.all_opportunities")




            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Скорость текста")

                    bar value Preference("text speed")

                    label _("Скорость авточтения")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Громкость музыки")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Громкость звуков")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Тест") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Громкость голоса")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Тест") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Без звука"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 625









screen history():





    predict False tag menu

    use game_menu(_("История"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:



                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False



                        if "color" in h.who_args:
                            text_color h.who_args['color']


                $ what = h.what
                text what:
                    substitute False

        if not _history_list:
            label _("История диалогов пуста.")




define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign
    size 30

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    size 26

style history_label:
    xfill True

style history_label_text:
    xalign 0.5








screen help():
    tag menu


    default device = "keyboard"

    use game_menu(_("Помощь"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Клавиатура") action SetScreenVariable("device", "keyboard")
                textbutton _("Мышь") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Геймпад") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Прохождение диалогов, активация интерфейса.")

    hbox:
        label _("Пробел")
        text _("Прохождение диалогов без возможности делать выбор.")

    hbox:
        label _("Стрелки")
        text _("Навигация по интерфейсу.")

    hbox:
        label _("Esc")
        text _("Вход в игровое меню.")

    hbox:
        label _("Ctrl")
        text _("Пропускает диалоги, пока зажат.")

    hbox:
        label _("Tab")
        text _("Включает режим пропуска.")

    hbox:
        label _("Page Up")
        text _("Откат назад по сюжету игры.")

    hbox:
        label _("Page Down")
        text _("Откатывает предыдущее действие вперёд.")

    hbox:
        label "H"
        text _("Скрывает интерфейс пользователя.")

    hbox:
        label "S"
        text _("Делает снимок экрана.")

    hbox:
        label "V"
        text _("Включает поддерживаемый {a=https://www.renpy.org/l/voicing}синтезатор речи{/a}.")


screen mouse_help():

    hbox:
        label _("Левый клик")
        text _("Прохождение диалогов, активация интерфейса.")

    hbox:
        label _("Клик колёсиком")
        text _("Скрывает интерфейс пользователя.")

    hbox:
        label _("Правый клик")
        text _("Вход в игровое меню.")

    hbox:
        label _("Колёсико вверх\nКлик на сторону отката")
        text _("Откат назад по сюжету игры.")

    hbox:
        label _("Колёсико вниз")
        text _("Откатывает предыдущее действие вперёд.")


screen gamepad_help():

    hbox:
        label _("Правый триггер\nA/Нижняя кнопка")
        text _("Прохождение диалогов, активация интерфейса.")

    hbox:
        label _("Левый Триггер\nЛевый Бампер")
        text _("Откат назад по сюжету игры.")

    hbox:
        label _("Правый бампер")
        text _("Откатывает предыдущее действие вперёд.")


    hbox:
        label _("Крестовина, Стики")
        text _("Навигация по интерфейсу.")

    hbox:
        label _("Start, Guide")
        text _("Вход в игровое меню.")

    hbox:
        label _("Y/Верхняя кнопка")
        text _("Скрывает интерфейс пользователя.")

    textbutton _("Калибровка") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0















screen confirm(message, yes_action, no_action):



    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 45

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 150

            textbutton _("Да") action yes_action
            textbutton _("Нет") action no_action


    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")









screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox:
            spacing 9

        text _("Пропускаю")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform delayed_blink(delay, cycle):
    alpha .5

    pause delay
    block:

        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:

    font "DejaVuSans.ttf"









screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message


    timer 4.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")









screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed:
                yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id



define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")







style pref_vbox:
    variant "medium"
    xsize 675




screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Назад") action Rollback()
            textbutton _("История") action ShowMenu('history')
            textbutton _("Пропуск") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Авто") action Preference("auto-forward", "toggle")
            textbutton _("Скрыть интерфейс") action HideInterface()
            textbutton _("Меню") action ShowMenu()

default AutoScroll = None
default ChoiceHeight = 300

init python:
    def GetMenuHeight(items):
        yy = 0
        output = 0
        for i in items:
            yy+=1
            widget = renpy.get_widget('choice','vbb'+str(yy))
            output+= widget.window_size[1]
        return output

    def ScrlAuto(items):
        global AutoScroll, ChoiceHeight
        AutoScroll = 'vertical' if GetMenuHeight(items)>ChoiceHeight else None
        return

screen choice_clutch(items):
    timer .01 action Function(ScrlAuto,items)

screen choice(items):
    variant "small"

    use choice_clutch(items)
    style_prefix "choice"

    frame xalign 0.98 xsize gui.choice_button_width+50:
        ypos 750 yanchor 1.0 ysize 400
        background None
        has viewport:
            spacing 0
            draggable True
            mousewheel True
            scrollbars AutoScroll
            id "vp_ch"
            style "vp_choice"

            ymaximum 400
            yalign 1.0
            yminimum 50
        vbox xfill True spacing 5:
            $ yy = 0
            for i in items:
                $ yy += 1
                button action i.action:
                    text i.caption style "choice_button_text"
                    left_padding 50 right_padding 35
                    foreground "interface marker"
                    id 'vbb'+str(yy)

style vp_choice:
    variant 'small'
    unscrollable "hide"

style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
