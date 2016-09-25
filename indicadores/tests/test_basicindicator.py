import unittest

from ..basicindicator import BasicIndicator
from ..TimeS import TimeSerie, TP, Barra, SerieEscalar

class iMV(BasicIndicator):
    def doCalc(self, cursor):
        return self.serie[0].Value(cursor)
    def doParams(self, params):
        self.interval = params[0]
        self.offset = 0

class iMV2(BasicIndicator):
    def doCalc(self, cursor):
        return self.serie[0].Value(cursor)
    def doParams(self, params):
        pass

def setUpModule():
    print "\nInit: Test indicator.py"

def tearDownModule():
    print "\nFin: Test indicator.py"


class BasicIndicatorTest(unittest.TestCase):
    def setUp(self):
        self.serie = SerieEscalar(3)
        for i in range(3):
            self.serie.appendValue(float(i+5))

    def test_falta_definir_doCalc(self):
        with self.assertRaises(NotImplementedError):
            ejemplo = BasicIndicator([self.serie,], 'EJEM')
            
    def test_indicador_mismo_valor(self):
        self.mv = iMV([self.serie,], 'mv')
        self.assertEqual(str(self.mv), '[0.0, 0.0, 0.0, 5.0, 6.0, 7.0]')

    def test_update_despues_de_anadir_valor(self):
        self.mv = iMV([self.serie,], 'mv')
        self.serie.appendValue(9.0)
        self.mv.update()
        self.assertEqual(str(self.mv), '[0.0, 0.0, 0.0, 5.0, 6.0, 7.0, 9.0]')

    def test_devolver_valor_etiqueta_ToIndicator(self):
        self.mv = iMV([self.serie,], 'mv')
        self.assertEqual(self.mv.ToIndicator().keys(), ['mv',])
        
    def test_devolver_valor_indicador_ToIndicator(self):
        self.mv = iMV([self.serie,], 'mv')
        self.s = SerieEscalar(3)
        for num in [5.0, 6.0, 7.0]:
            self.s.appendValue(num)
            
        self.assertEqual(
            self.mv.ToIndicator()['mv'], self.s)