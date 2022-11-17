class cuentas:
    def __init__ (self,usuario,contra,tipo,nombre,tel):
        self.usario=usuario
        self.contra=contra
        self.tipo=tipo
        self.nombre=nombre
        self.tel=tel
        return
    
    def get_usario(self):
        return self.usario
    def get_contra(self):
        return self.contra
    def get_tipo(self):
        return self.tipo
    def get_nombre(self):
        return self.nombre
    def get_tel(self):
        return self.tel
    def set_nom(self,nom):
        self.nombre =nom
        return 
    def set_tel(self,tel):
        self.tel =tel
        return 
    def set_contra(self,contraant,contra):
        if self.contra==contraant:
            self.contra=contra
        return 

    def log(self,usuario,contra):
        if self.usario!= usuario:
            return 'error usuario'
        if self.contra!= contra:
            return 'error contra'
        else:
            return 'exito login'