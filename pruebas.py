import cuentas 
import unittest

class testcuentas (unittest.TestCase):
    def test_cambio_contraexitosa(self):
        a=cuentas.cuentas('aaa','abc123','admin','pepe','3123412')
        a.set_contra('abc123','1234')
        self.assertEqual('1234',a.get_contra())    
    def test_cambio_contrafalla(self):
        a=cuentas.cuentas('aaa','abc123','admin','pepe','3123412')
        a.set_contra('abc122','1234')
        self.assertEqual('abc123',a.get_contra())
    def test_login_exitoso(self):
         a=cuentas.cuentas('aaa','abc123','admin','pepe','3123412')
         self.assertEqual('exito login',a.log('aaa','abc123'))
    
    def test_loginfallocontra(self):
         a=cuentas.cuentas('aaa','abc123','admin','pepe','3123412')
         self.assertEqual('error contra',a.log('aaa','abc13'))
    
    def test_loginfallacontra (self):
         a=cuentas.cuentas('aaa','abc123','admin','pepe','3123412')
         self.assertEqual('error usuario',a.log('aa','abc123'))

if __name__ == '__main__':
    unittest.main()