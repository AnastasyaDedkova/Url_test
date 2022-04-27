import webbrowser
#  Обработка  введенного запроса
def req():
    call1 = input("Введите ссылку на сайт, который нужно проверить")
    call2 = call1.replace(' ', '')
    if call2[0] == 'h' and call2[4] == 's':
        call3 = call2[8:]
    elif call2[0] == 'h' and call2[4] == ':':
        call3 = call2[7:]
    else:
        call3 = call2
    if call3[-1] == '/':
        call = call3[:-1]
    else:
        call = call3
    return call
#  Переадресация на сайт
def test_url():
    webbrowser.open('https://www.virustotal.com/gui/search/' + site_url)

site_url = req()
test_url()