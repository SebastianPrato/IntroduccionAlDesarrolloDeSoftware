from app import app, datos
import unittest

class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.data = {
            "capital_inicial": 1000,
            "tasa": 5,
            "anios": 3
        }
        self.client.post('/interes', json=self.data)

    def test_anios_no_debe_ser_null(self):
        self.assertIsNotNone(datos["anios"],"Se debe introducir una cantidad de años")

    def test_tasa_no_debe_ser_null(self):
        self.assertIsNotNone(datos['tasa'], "Se debe introducir una tasa")

    def test_capital_no_debe_ser_null(self):
        self.assertIsNotNone(datos['anios'], "Se debe introducir una cantidad de capital")

    def test_anios_debe_ser_mayor_a_cero(self):
        self.assertGreater(datos['anios'], 0, "La cantidad de anios debe ser mayor a cero")

    def test_tasa_debe_ser_mayor_a_cero(self):
        self.assertGreater(datos['tasa'], 0, "La tasa de ganancias debe ser mayor a cero")

    def test_capital_debe_ser_mayor_a_cero(self):
        self.assertGreater(datos['anios'], 0, "el capital inicial debe ser mayor a cero")

    def test_monto_final_es_correcto(self):
        esperado = 1000 * (1 + (5 / 100)) ** 3
        self.assertAlmostEqual(datos['monto_final'], esperado, places=2, msg="El monto final calculado es incorrecto")

    def test_post_interes_retorna_201(self):
        response = self.client.post('/interes', json=self.data)
        self.assertEqual(response.status_code, 201)
        json_data = response.get_json()
        self.assertIn("monto_final", json_data)

if __name__ == "__main__":
    unittest.main()