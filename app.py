import conexao as cn
from time import sleep
from selenium.webdriver.common.keys import Keys
import random


class InstaBot:
    lista_comentarios = ['Muito bom!', 'Top!', 'Show!', 'Bem legal isso!', "Ótimo trabalho!", "Absolutamente fantástico!",
                        'Tenha um bom dia!', 'Que incrível!', 'Adorei!', 'Que legal!', 'Amei isso!', 'Realmente encantador!', 'maravilhoso!',
                        'incrível!', 'Amei as cores', 'Amei a composição', 'Desejo-lhe um dia fantástico!', 'Amei isso! Continue com seu grande trabalho!',
                        'Oi Bela postagem, já apertei o amei.', 'Boa postagem!', 'Gostei muito', 'Maravilhoso! ', 'Tenha um bom dia', 'Ótimo!', 'Legal!',
                        'Realmente interessante!', 'Gostei muito e tenha um bom dia', 'Continue assim!', 'Muito bem!', 'Postagem incrível!',
                        'Inspirador!', 'Showww!', 'Impressionante!', 'Muito lindo! É isso aí!', 'Gostei muito!', 'Tá ótimo!', 'Top de linha!', 'Oiee, gostei do seu conteúdo!',
                        'Inspirador sua postagem!', 'Showww esse post!', 'Que conteúdo bacana você tem!', 'Muito lindo!', 'Genial! Muito legal!']
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        self.driver = cn.conexao('Firefox').selecionaBrowser()

    def login(self):
        # driver = cn.conexao('Firefox').selecionaBrowser()
        driver = self.driver
        driver.get("https://www.instagram.com/")
        sleep(7)
        txt_user = driver.find_element('xpath', '//input[@name="username"]')
        txt_user.click()
        txt_user.clear()
        txt_user.send_keys(self.usuario)

        txt_senha = driver.find_element('xpath', '//input[@name="password"]')
        txt_senha.click()
        txt_senha.clear()
        txt_senha.send_keys(self.senha)

        txt_senha.send_keys(Keys.RETURN)
        sleep(15)

    def abrir_posts_hashtag(self, hashtag):
        driver = self.driver
        driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        sleep(10)
        for i in range(5):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)
        # tags_a = driver.find_elements('tag name', 'a')
        tags_a = driver.find_elements('xpath', '//div[@class="_aabd _aa8k _aanf"]/a')
        hrefs = [tag.get_attribute('href') for tag in tags_a]
        print(len(hrefs))
        for href in hrefs:
            driver.get(href)
            sleep(5)
            try:
                self.curtir_fotos()
                self.comentar_posts()
            except Exception as e:
                print(e)
                sleep(5)

    def comentar_posts(self):
        driver = self.driver
        comentario = random.choice(self.lista_comentarios)
        driver.find_element('xpath', '//textarea[@placeholder="Adicione um comentário..."]').click()
        txt_comentario = driver.find_element('xpath', '//textarea[@placeholder="Adicione um comentário..."]')
        sleep(2)
        self.digitaComentario(comentario, txt_comentario)
        txt_comentario.send_keys(Keys.RETURN)

    def curtir_fotos(self):
        driver = self.driver
        # driver.find_element('xpath', '//button[@class="_abl-"]').click()
        bt = driver.find_element('xpath', '//span[@class="_aamw"]/button[@class="_abl-"]')
        bt.click()
        # driver.execute_script("arguments[0].click();", bt)

    @staticmethod
    def digitaComentario(frase, campo):
        for letra in frase:
            campo.send_keys(letra)
            sleep(1/random.randint(1, 5))



if __name__ == '__main__':
    user = input('Usuário: ')
    password = input('Senha: ')
    app = InstaBot(user, password)
    app.login()
    app.abrir_posts_hashtag('memesbrasil')