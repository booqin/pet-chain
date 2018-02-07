# -*- coding: utf-8 -*-

class PetChain:
    name = 'petchain'

    def __init__(self):
        self.name = 'hello'
        self.pet = 'pet'

    def login(self):
        print('登录成功')

    def getPet(self):
        self.pet = 'pet'

    def buy(self):
        return

if __name__ == '__main__':
    pet = PetChain()
    pet.login()
