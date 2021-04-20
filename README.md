# pipe_traceroute

Traceroute с определением номера автономной системы, региона и провайдера

Автор: Ивашкин Роман, КН-204

## Требования

Для запуска программы необходим `python3`

Для коректной работы программа должна быть запущена с правами администратора

## Запуск

`python3 traceroute.py <address or ip> <hops>`

`<address or ip>` - ip-адресс или доменное имя ресурса до которого необходимо проследить маршрут

`<hops>` - число, максимальная глубина отслеживания

## Пример вывода

````
sudo python3 traceroute.py ya.ru 30

#       host name                     host address                  AS                            country                       provider                      

1       _gateway                      10.113.224.1                                                                                                            

2       10.254.253.252                10.254.253.252                                                                                                          

3       10.255.201.6                  10.255.201.6                                                                                                            

4       10.255.101.5                  10.255.101.5                                                                                                            

5       10.255.100.2                  10.255.100.2                                                                                                            

6       195.239.186.161               195.239.186.161               AS3216                        RU                            Ekaterinburg branch NETS      

7       pe03.kk12.moscow.gldn.net     79.104.235.213                AS3216                        RU                            EDN SOVINTEL                  

8       * * * 
        ...
