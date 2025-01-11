import re
response = """Neil corre até o terminal de segurança e começa a digitar furiosamente os códigos que aprendeu durante sua preparação. O sistema começa a responder lentamente, mas logo ele consegue acessar o banco de dados central da HacksNow. Uma série de arquivos confidenciais surge na tela, e Neil rapidamente localiza o núcleo da Matrix que controla a humanidade. Ele começa a baixar as informações vitais necessárias para iniciar a destruição do sistema. Mas, antes que possa concluir o processo, o alarme do edifício começa a tocar, e luzes vermelhas se acendem. A HacksNow detectou a invasão e está enviando uma força-tarefa para neutralizá-lo. Neil sabe que precisa agir rapidamente. Com as informações agora em suas mãos, ele deve decidir entre continuar com o hack, que pode ser interrompido a qualquer momento, ou escapar antes que a segurança chegue, levando as informações consigo.

1 - Continuar com o hack, arriscando ser pego, mas garantindo a conclusão da missão.  
2 - Desligar o terminal e fugir, levando os dados já baixados com ele.  
3 - Tentar destruir os servidores, impedindo que a HacksNow use as informações contra ele.  

game-over: no  
game-win: no"""
resonse1 = re.split(r'\n\n', response)
print(len(resonse1))