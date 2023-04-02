#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel)
from random import shuffle
class Question():
        def __init__ (self,question, right_answer, wrong1, wrong2, wrong3):
                self.question = question
                self.right_answer = right_answer
                self.wrong1 = wrong1
                self.wrong2 = wrong2
                self.wrong3 = wrong3
app = QApplication([]) 
btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('Самый сложный вопрос в мире!')
 
RadioGroupBox = QGroupBox("Варианты ответов") 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
 
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 
 
RadioGroupBox.setLayout(layout_ans1) 
 
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')
 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() 
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)
 
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=3)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
 
def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
 
def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 
 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
 
def ask(question, right_answer, wrong1, wrong2, wrong3):
    ''' функция записывает значения вопроса и ответов в соответствующие виджеты, 
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    lb_Question.setText(question)
    lb_Correct.setText(right_answer) 
    show_question() 
 
def show_correct(res):
    ''' показать результат - установим переданный текст в надпись "результат" и покажем нужную панель '''
    lb_Result.setText(res)
    show_result()
 
def check_answer():
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
quat_list = []
quat_list.append(Question('Что такое доброта?','смешарики','добрый человек','дружба','черта характера'))
quat_list.append(Question('Как умер Ромео из повести "Ромео и Джульетте?"','трагично','от Париса','от яда','от Париса'))
quat_list.append(Question('Где была первая встреча Ромео и Джульетты?','на баллу','на балконе','в замке','на свадьбе'))
quat_list.append(Question('Как звали священника который благословил Ромео и Джульетту?','Марк','Дориан','Лоренцо','Парис'))
quat_list.append(Question('Кто убил Меркуцио из повести Ромео и Дужльетту?','Тибальт','Марк','Дориан','Ромео'))
quat_list.append(Question('Когда началась первая мировая война?','1911','1913','1914','1917'))
quat_list.append(Question('Когда образовалась Монгольская империя?','1255','1234','1223','1211'))
quat_list.append(Question('Сколько пальцев можно вместить в рот человека?','5','15','19','55'))
quat_list.append(Question('Сколько было пальцев у Миккиланджело из Черепашек Ниндзя?','3','5','4','1'))
quat_list.append(Question('Какой праздник 1 мая?','День труда','День единности народов','День дружбы народов','день жуков'))
quat_list.append(Question('Зачем Джульетта заколола себя кинжалом?','от смерти Ромео','От смерти отца','по рофлу','От горечи утраты'))
quat_list.append(Question('Чингизхан какой нации был?','казах','монгол','немец','китаеза'))
quat_list.append(Question('Как образовалась Алаш Орда?','из за того что права казахов принижали','для захвата Российской империи','эпично','че там'))
quat_list.append(Question('Когда образовалась Алаш Орда?','1912','1922','1917','1918'))
quat_list.append(Question('Кто придумал блок страйк','ты','я','аурум','вместе'))
quat_list.append(Question('Зачем Ромео выпил яд?','ему все надоело','из за смерти Джульетты','из за смертного приговора в суде','случайно'))
quat_list.append(Question('Кем Тибальт был Джульетте?','родной брат','двоюродный брат','папа','бойфренд'))
quat_list.append(Question('Из какой семьи была Джульетте?','блатной','Капулетти','Монтекки','крутой'))
quat_list.append(Question('Почему мы ходим в школу?','пакачену','зачем то','по приколу и чтоб балду гонять','ради директора'))
quat_list.append(Question('Сколько идет новый год?','месяц','год','3 дня','1 ночь'))
btn_OK.clicked.connect(check_answer) 
 
window.show()
app.exec()
#закрытие и отображение оконого приложения
