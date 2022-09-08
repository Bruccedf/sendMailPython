# Importa biblioteca SMTP
import smtplib
import getpass
import os

# Importa mime dos campos
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print("------------------------------------------")
print(" Olá, bem vindo ao Desafio SendMailPython!")
print(" Por: Elismar Ramos")
print("------------------------------------------")
print("   ")
print("   ")

# Instancia as varáveis de envio
smtpServer = input("Informe o servidor SMTP (Ex: smtp.seudominio.com): ")

print("  ")
print("Escolha da porta conforme provedor SMTP:")
print("25 - Sem autenticação.")
print("465 - Autenticação SSl.")
print("587 - Autenticação TLS.")
print("  ")
smtpPort = int(input("Digite uma porta: "))

mailFrom = input("Email REMETENTE: ")

mailFromKey = input("Informe a senha de email REMETENTE: ")

mailTo = input("Email DESTINATÁRIO: ")

mailSubject = input("Assunto do email: ")

mailMessage = input("Mensagem: ")
print("   ")
print("   ")

# Resumo do envio
print("o Email será enviado da seguinte forma: ")
print("   ")
print("   ")

print("De: " + mailFrom)
print("Para: " + mailTo)
print("Assunto: " + mailSubject)
print("Mensagem: " + mailMessage)
print("   ")
print("   ")

# Condiciona o envio
sendMail = input("Confirma o envio do email? [s,n]")
print("   ")
print("   ")

if sendMail == 's':

        # Instancia objeto da mensagem
        mensagem = MIMEMultipart()

        # Parametriza
        mensagem['From'] = mailFrom
        mensagem['To'] = mailTo
        mensagem['Subject'] = mailSubject

        # Corpo do email
        mensagem.attach(MIMEText(mailMessage))

        print("Autenticando no servidor SMTP...")

        if smtpPort == 25:

                server = smtplib.SMTP(smtpServer, smtpPort)

        elif smtpPort == 465:

                server = smtplib.SMTP_SSL(smtpServer, smtpPort)

                # Loga no servidor de email
                server.login(mensagem['From'], mailFromKey)

        elif smtpPort == 587:

                server = smtplib.SMTP(smtpServer, smtpPort)

                # Inicia o servidor
                print('Iniciando TLS...')
                server.starttls()

                # Loga no servidor de email
                server.login(mensagem['From'], mailFromKey)


        # Envia o email
        print('Enviando email...aguarde!')
        server.sendmail(mensagem['From'], mensagem['To'], mensagem.as_string())

        # Finaliza o servidor
        print('Finalizando servidor...')
        server.quit()

        print("Email enviado com sucesso para %s: " % (mensagem['To']))

        # Mantem o console aberto
        os.system("PAUSE")

elif sendMail == 'n':

    print('Email não enviado, os dados foram descartados.')
    print("   ")

else:

    print('Sem confirmação ou informações incompletas.')

print("   ")
print("   ")

# Mantem o console aberto
os.system("PAUSE")
