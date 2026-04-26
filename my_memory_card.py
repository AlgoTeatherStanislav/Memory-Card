from random import shuffle, randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)

from PyQt5.QtGui import QPixmap

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, QTimer

class Question():
    def __init__(self, 
        question_text, 
        right_answer_text, 
        wrong1_text, wrong2_text, wrong3_text, 
        image=None, audio=None):
        self.question = question_text
        self.right_answer = right_answer_text
        self.wrong1 = wrong1_text
        self.wrong2 = wrong2_text
        self.wrong3 = wrong3_text
        self.image = image
        self.audio = audio

app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle('MemoryCard')
main_win.resize(540, 580)

lb_question = QLabel('Самый сложный вопрос в мире')

RadioGroupBox = QGroupBox('Варианты ответов')

answer_bnt1 = QRadioButton('1')
answer_bnt2 = QRadioButton('2')
answer_bnt3 = QRadioButton('3')
answer_bnt4 = QRadioButton('4')

bnt_answer = QPushButton('Ответить')

AnsGroupBox = QGroupBox('Результат теста')
is_correct = QLabel('Правильно/Неправильно')
correct_ans = QLabel('Правильный ответ')
correct_layout = QVBoxLayout()

correct_layout.addWidget(is_correct, alignment = (Qt.AlignLeft | Qt.AlignTop))
correct_layout.addWidget(correct_ans, alignment = Qt.AlignCenter)

AnsGroupBox.setLayout(correct_layout)

ans_layoutV1 = QVBoxLayout()
ans_layoutV1.addWidget(answer_bnt1)
ans_layoutV1.addWidget(answer_bnt2)

ans_layoutV2 = QVBoxLayout()
ans_layoutV2.addWidget(answer_bnt3)
ans_layoutV2.addWidget(answer_bnt4)

ans_layoutH = QHBoxLayout()
ans_layoutH.addLayout(ans_layoutV1)
ans_layoutH.addLayout(ans_layoutV2)

RadioGroupBox.setLayout(ans_layoutH)

layoutH1 = QHBoxLayout()
layoutH1.addWidget(lb_question, alignment = 
    (Qt.AlignHCenter | Qt.AlignVCenter))

layoutH2 = QHBoxLayout()
layoutH2.addWidget(RadioGroupBox)

layoutH2.addWidget(AnsGroupBox)

layoutH3 = QHBoxLayout()
layoutH3.addStretch(1)
layoutH3.addWidget(bnt_answer, stretch=2)
layoutH3.addStretch(1)

main_layout = QVBoxLayout()
main_layout.addLayout(layoutH1)
main_layout.addLayout(layoutH2)
main_layout.addLayout(layoutH3)
main_layout.setSpacing(25)

AnsGroupBox.hide()

RadioGroup = QButtonGroup()
RadioGroup.addButton(answer_bnt1)
RadioGroup.addButton(answer_bnt2)
RadioGroup.addButton(answer_bnt3)
RadioGroup.addButton(answer_bnt4)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    bnt_answer.setText('Следующий вопрос')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    bnt_answer.setText('Ответить')

    RadioGroup.setExclusive(False)
    answer_bnt1.setChecked(False)
    answer_bnt2.setChecked(False)
    answer_bnt3.setChecked(False)
    answer_bnt4.setChecked(False)
    RadioGroup.setExclusive(True)

answer = [answer_bnt1, answer_bnt2, answer_bnt3, answer_bnt4]

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    lb_question.setText(q.question)
    correct_ans.setText(q.right_answer)
    if q.image:
        lb_image.setPixmap(
            QPixmap(q.image).scaled(512, 512, Qt.KeepAspectRatio)
        )
        lb_image.show() 
    else:
        lb_image.hide()

    if q.audio:
        player.setMedia(QMediaContent(QUrl.fromLocalFile(q.audio)))
        bnt_audio.show()
        lb_audio_time.show()
        lb_audio_time.setText("00:00 / 00:00")
    else:
        player.stop()
        bnt_audio.hide()
        lb_audio_time.hide()

    show_question()

def check_answer():
    player.stop()
    audio_timer.stop()
    if answer[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
    elif (answer[1].isChecked() or 
            answer[2].isChecked() or 
            answer[3].isChecked()):
        show_correct('Неверно!')

    print("-----------------")
    print("Статистика")
    print("- Всего вопросов задано:", main_win.total)
    print("- Верно отвечено:", main_win.score)
    print("- Отвечено неверно:", main_win.total - main_win.score)
    print("Рейтинг:", main_win.score /main_win.total * 100, "%")
    print("-----------------")

def show_correct(correct_text):
    is_correct.setText(correct_text)
    show_result()

questions_list = [] # list()
questions_list.append(
    Question('Государственный язык Бразилии', 
            'Португальский', 
            'Русский', 
            'Английский', 
            'Бразильский')
)
questions_list.append(
    Question('Выбери перевод слова "переменная"', 
        'variable', 
        'changing', 
        'variation',
        'variant')
)
questions_list.append(
    Question('Самый сложный вопрос в мире', 
        '1', 
        '2', 
        '8',
        '9')
)
questions_list.append(
    Question('Какой народ является самым многочисленным в России?', 
        'Русские', 
        'Татары', 
        'Башкиры',
        'Китайцы')
)
questions_list.append(
    Question('Сколько языков в России?', 
        'Около 280', 
        'Около 1', 
        'Около 1000',
        'Около 830')
)
questions_list.append(
    Question('Какой процент населения России составляют русские? ', 
        'Около 72%', 
        'Около 50%', 
        'Около 90%',
        'Около 30%')
)
questions_list.append(
    Question('Где традиционно проживают чукчи и эскимосы?', 
        'Крайний Север и Дальний Восток', 
        'Кавказ', 
        'Поволжье',
        'Центральная Россия')
)
questions_list.append(
    Question('В каком регионе России находится Республика Саха?', 
        'Сибирь', 
        'Юг России', 
        'Северо-Запад',
        'Урал')
)
questions_list.append(
    Question('Какой танец является символом Кавказа и исполняется многими народами региона?', 
        'Лезгинка', 
        'Хота', 
        'Вальс',
        'Казачок')
)
questions_list.append(
    Question('Традиционный головной убор казаков?', 
        'Кубанка', 
        'Папаха', 
        'Ушанка',
        'Тюбетейка')
)
questions_list.append(
    Question('Что на картинке?', 
        'Кот', 
        'Собака','Медведь','Лиса', 
        'cat.jpg')
)
questions_list.append(
    Question(
        'Какой язык ты слышишь?',
        'Французский',
        'Испанский',
        'Итальянский',
        'Португальский',
        audio='french.mp3'
    )
)


def next_question():
    main_win.total += 1
    print("-----------------")
    print("Статистика")
    print("- Всего вопросов задано:", main_win.total)
    print("-----------------")
    cur_question = randint(0, len(questions_list) - 1)
    ask(questions_list[cur_question])

def click_ok():
    if bnt_answer.text() == 'Ответить':
        check_answer()
    else:
        next_question()

def format_time(ms):
    s = ms // 1000
    return f"{s//60:02}:{s%60:02}"

def update_audio_time():
    cur = player.position()
    dur = player.duration()
    lb_audio_time.setText(
        f"{format_time(cur)} / {format_time(dur)}"
    )

def play_audio():
    if player.state() == QMediaPlayer.PlayingState:
        player.stop()

    player.play()
    audio_timer.start()

def audio_finished(status):
    if status == QMediaPlayer.EndOfMedia:
        audio_timer.stop()


lb_image = QLabel()
lb_image.setAlignment(Qt.AlignCenter)
main_layout.insertWidget(0, lb_image)

bnt_audio = QPushButton("▶ Воспроизвести")
lb_audio_time = QLabel("00:00 / 00:00")

audio_layout = QHBoxLayout()
audio_layout.addWidget(bnt_audio, stretch = 5)
audio_layout.addWidget(lb_audio_time)
audio_layout.setAlignment(Qt.AlignCenter)

main_layout.insertLayout(1, audio_layout, )

bnt_audio.hide()
lb_audio_time.hide()

player = QMediaPlayer()
audio_timer = QTimer()
audio_timer.setInterval(50)

bnt_audio.clicked.connect(play_audio)
audio_timer.timeout.connect(update_audio_time)
player.mediaStatusChanged.connect(audio_finished)

bnt_answer.clicked.connect(click_ok)
main_win.total = 0
main_win.score = 0
next_question()

main_win.setLayout(main_layout)
main_win.show()
app.exec_()