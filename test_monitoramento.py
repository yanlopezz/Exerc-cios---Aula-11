import unittest
import datetime
from datetime import date
from monitoramento import avaliar_temperatura,avaliar_cpu,avaliar_memoria,classificar_latencia,avaliar_disco,validar_certificado,prever_armazenamento,analisar_trafego


class TestAvaliarTemperatura(unittest.TestCase):

    def test_frio_negativo(self):
        self.assertEqual(avaliar_temperatura(-10), "Frio")

    def test_frio_zero(self):
        self.assertEqual(avaliar_temperatura(0), "Frio")

    def test_frio_tipico(self):
        self.assertEqual(avaliar_temperatura(10), "Frio")

    def test_frio_limite_superior(self):
        self.assertEqual(avaliar_temperatura(19.9), "Frio")

    def test_ideal_limite_inferior(self):
        self.assertEqual(avaliar_temperatura(20), "Ideal")

    def test_ideal_tipico(self):
        self.assertEqual(avaliar_temperatura(30), "Ideal")

    def test_ideal_limite_superior(self):
        self.assertEqual(avaliar_temperatura(39.9), "Ideal")

    def test_alerta_limite_inferior(self):
        self.assertEqual(avaliar_temperatura(40), "Alerta")

    def test_alerta_tipico(self):
        self.assertEqual(avaliar_temperatura(55), "Alerta")

    def test_alerta_limite_superior(self):
        self.assertEqual(avaliar_temperatura(69.9), "Alerta")

    def test_risco_critico_limite_inferior(self):
        self.assertEqual(avaliar_temperatura(70), "Risco crítico")

    def test_risco_critico_tipico(self):
        self.assertEqual(avaliar_temperatura(85), "Risco crítico")

    def test_risco_critico_extremo(self):
        self.assertEqual(avaliar_temperatura(120), "Risco crítico")


class TestAvaliarCpu(unittest.TestCase):

    def test_normal_zero(self):
        self.assertEqual(avaliar_cpu(0), "Normal")

    def test_normal_tipico(self):
        self.assertEqual(avaliar_cpu(20), "Normal")

    def test_normal_limite_superior(self):
        self.assertEqual(avaliar_cpu(39.9), "Normal")

    def test_alta_limite_inferior(self):
        self.assertEqual(avaliar_cpu(40), "Alta")

    def test_alta_tipico(self):
        self.assertEqual(avaliar_cpu(60), "Alta")

    def test_alta_limite_superior(self):
        self.assertEqual(avaliar_cpu(80), "Alta")

    def test_sobrecarga_limite_inferior(self):
        self.assertEqual(avaliar_cpu(80.1), "Sobrecarga")

    def test_sobrecarga_tipico(self):
        self.assertEqual(avaliar_cpu(90), "Sobrecarga")

    def test_sobrecarga_maximo(self):
        self.assertEqual(avaliar_cpu(100), "Sobrecarga")


class TestAvaliarMemoria(unittest.TestCase):

    def test_confortavel_zero(self):
        self.assertEqual(avaliar_memoria(0), "Confortável")

    def test_confortavel_tipico(self):
        self.assertEqual(avaliar_memoria(30), "Confortável")

    def test_confortavel_limite_superior(self):
        self.assertEqual(avaliar_memoria(49.9), "Confortável")

    def test_monitorar_limite_inferior(self):
        self.assertEqual(avaliar_memoria(50), "Monitorar")

    def test_monitorar_tipico(self):
        self.assertEqual(avaliar_memoria(70), "Monitorar")

    def test_monitorar_limite_superior(self):
        self.assertEqual(avaliar_memoria(84.9), "Monitorar")

    def test_critica_limite_inferior(self):
        self.assertEqual(avaliar_memoria(85), "Crítica")

    def test_critica_tipico(self):
        self.assertEqual(avaliar_memoria(92), "Crítica")

    def test_critica_maximo(self):
        self.assertEqual(avaliar_memoria(100), "Crítica")


class TestClassificarLatencia(unittest.TestCase):

    def test_excelente_zero(self):
        self.assertEqual(classificar_latencia(0), "Excelente")

    def test_excelente_tipico(self):
        self.assertEqual(classificar_latencia(5), "Excelente")

    def test_excelente_limite_superior(self):
        self.assertEqual(classificar_latencia(9.9), "Excelente")

    def test_boa_limite_inferior(self):
        self.assertEqual(classificar_latencia(10), "Boa")

    def test_boa_tipico(self):
        self.assertEqual(classificar_latencia(25), "Boa")

    def test_boa_limite_superior(self):
        self.assertEqual(classificar_latencia(39.9), "Boa")

    def test_regular_limite_inferior(self):
        self.assertEqual(classificar_latencia(40), "Regular")

    def test_regular_tipico(self):
        self.assertEqual(classificar_latencia(70), "Regular")

    def test_regular_limite_superior(self):
        self.assertEqual(classificar_latencia(99.9), "Regular")

    def test_ruim_limite_inferior(self):
        self.assertEqual(classificar_latencia(100), "Ruim")

    def test_ruim_tipico(self):
        self.assertEqual(classificar_latencia(200), "Ruim")

    def test_ruim_extremo(self):
        self.assertEqual(classificar_latencia(1000), "Ruim")


class TestAvaliarDisco(unittest.TestCase):

    def test_seguro_maximo(self):
        self.assertEqual(avaliar_disco(100), "Seguro")

    def test_seguro_tipico(self):
        self.assertEqual(avaliar_disco(60), "Seguro")

    def test_seguro_limite_inferior(self):
        self.assertEqual(avaliar_disco(40), "Seguro")

    def test_atencao_limite_superior(self):
        self.assertEqual(avaliar_disco(39.9), "Atenção")

    def test_atencao_tipico(self):
        self.assertEqual(avaliar_disco(30), "Atenção")

    def test_atencao_limite_inferior(self):
        self.assertEqual(avaliar_disco(20), "Atenção")

    def test_critico_limite_superior(self):
        self.assertEqual(avaliar_disco(19.9), "Crítico")

    def test_critico_tipico(self):
        self.assertEqual(avaliar_disco(10), "Crítico")

    def test_critico_zero(self):
        self.assertEqual(avaliar_disco(0), "Crítico")


class TestValidarCertificado(unittest.TestCase):

    def _fmt(self, d: date) -> str:
        return d.strftime("%d/%m/%Y")

    def test_valido_emitido_hoje(self):
        hoje = date.today()
        self.assertEqual(validar_certificado(self._fmt(hoje), 2), "Certificado válido")

    def test_valido_60_dias_para_vencer(self):
        expiracao = date.today() + datetime.timedelta(days=60)
        emissao = date(expiracao.year - 1, expiracao.month, expiracao.day)
        self.assertEqual(validar_certificado(self._fmt(emissao), 1), "Certificado válido")

    def test_valido_31_dias_para_vencer(self):
        expiracao = date.today() + datetime.timedelta(days=31)
        emissao = date(expiracao.year - 1, expiracao.month, expiracao.day)
        self.assertEqual(validar_certificado(self._fmt(emissao), 1), "Certificado válido")

    def test_expira_em_breve_30_dias(self):
        expiracao = date.today() + datetime.timedelta(days=30)
        emissao = date(expiracao.year - 1, expiracao.month, expiracao.day)
        self.assertEqual(validar_certificado(self._fmt(emissao), 1), "Certificado expira em breve")

    def test_expira_em_breve_15_dias(self):
        expiracao = date.today() + datetime.timedelta(days=15)
        emissao = date(expiracao.year - 1, expiracao.month, expiracao.day)
        self.assertEqual(validar_certificado(self._fmt(emissao), 1), "Certificado expira em breve")

    def test_expira_em_breve_1_dia(self):
        expiracao = date.today() + datetime.timedelta(days=1)
        emissao = date(expiracao.year - 1, expiracao.month, expiracao.day)
        self.assertEqual(validar_certificado(self._fmt(emissao), 1), "Certificado expira em breve")

    def test_expirado_ha_1_dia(self):
        expiracao = date.today() - datetime.timedelta(days=1)
        emissao = date(expiracao.year - 1, expiracao.month, expiracao.day)
        self.assertEqual(validar_certificado(self._fmt(emissao), 1), "Certificado expirado")

    def test_expirado_ha_1_ano(self):
        emissao = date(date.today().year - 3, 6, 1)
        self.assertEqual(validar_certificado(self._fmt(emissao), 1), "Certificado expirado")

    def test_expirado_ha_varios_anos(self):
        emissao = date(date.today().year - 5, 1, 1)
        self.assertEqual(validar_certificado(self._fmt(emissao), 1), "Certificado expirado")


class TestPreverArmazenamento(unittest.TestCase):

    def test_retorna_tupla(self):
        self.assertIsInstance(prever_armazenamento(100, 0.10, 1), tuple)

    def test_tupla_tem_dois_elementos(self):
        self.assertEqual(len(prever_armazenamento(100, 0.10, 1)), 2)

    def test_calculo_juros_compostos_1_ano(self):
        final, _ = prever_armazenamento(1000, 0.10, 1)
        self.assertAlmostEqual(final, 1100.0, places=1)

    def test_calculo_juros_compostos_2_anos(self):
        final, _ = prever_armazenamento(100, 0.10, 2)
        self.assertAlmostEqual(final, 121.0, places=1)

    def test_calculo_taxa_zero(self):
        final, _ = prever_armazenamento(300, 0.0, 5)
        self.assertAlmostEqual(final, 300.0, places=1)

    def test_seguro_tipico(self):
        final, status = prever_armazenamento(100, 0.10, 5)
        self.assertLess(final, 500)
        self.assertEqual(status, "Seguro")

    def test_seguro_limite_superior(self):
        final, status = prever_armazenamento(499, 0.0, 1)
        self.assertEqual(status, "Seguro")

    def test_monitorar_limite_inferior(self):
        final, status = prever_armazenamento(500, 0.0, 1)
        self.assertEqual(status, "Monitorar")

    def test_monitorar_tipico(self):
        final, status = prever_armazenamento(300, 0.15, 5)
        self.assertGreaterEqual(final, 500)
        self.assertLess(final, 2000)
        self.assertEqual(status, "Monitorar")

    def test_monitorar_limite_superior(self):
        final, status = prever_armazenamento(1999, 0.0, 1)
        self.assertEqual(status, "Monitorar")

    def test_upgrade_limite_inferior(self):
        final, status = prever_armazenamento(2000, 0.0, 1)
        self.assertEqual(status, "Upgrade necessário")

    def test_upgrade_tipico(self):
        final, status = prever_armazenamento(500, 0.20, 10)
        self.assertGreaterEqual(final, 2000)
        self.assertEqual(status, "Upgrade necessário")


class TestAnalisarTrafego(unittest.TestCase):

    def test_retorna_tupla(self):
        self.assertIsInstance(analisar_trafego(10, 20, 30), tuple)

    def test_tupla_tem_dois_elementos(self):
        self.assertEqual(len(analisar_trafego(10, 20, 30)), 2)

    def test_calculo_media_inteiros(self):
        media, _ = analisar_trafego(100, 200, 300)
        self.assertAlmostEqual(media, 200.0)

    def test_calculo_media_valores_iguais(self):
        media, _ = analisar_trafego(50, 50, 50)
        self.assertAlmostEqual(media, 50.0)

    def test_baixo_trafego_tipico(self):
        _, status = analisar_trafego(10, 20, 30)
        self.assertEqual(status, "Baixo tráfego")

    def test_baixo_trafego_zero(self):
        _, status = analisar_trafego(0, 0, 0)
        self.assertEqual(status, "Baixo tráfego")

    def test_baixo_trafego_limite_superior(self):
        media, status = analisar_trafego(99, 99, 99)
        self.assertLess(media, 100)
        self.assertEqual(status, "Baixo tráfego")

    def test_moderado_limite_inferior(self):
        media, status = analisar_trafego(100, 100, 100)
        self.assertEqual(media, 100.0)
        self.assertEqual(status, "Tráfego moderado")

    def test_moderado_tipico(self):
        _, status = analisar_trafego(100, 200, 300)
        self.assertEqual(status, "Tráfego moderado")

    def test_moderado_limite_superior(self):
        media, status = analisar_trafego(499, 499, 499)
        self.assertLess(media, 500)
        self.assertEqual(status, "Tráfego moderado")

    def test_alto_limite_inferior(self):
        media, status = analisar_trafego(500, 500, 500)
        self.assertEqual(media, 500.0)
        self.assertEqual(status, "Tráfego alto")

    def test_alto_tipico(self):
        _, status = analisar_trafego(500, 600, 700)
        self.assertEqual(status, "Tráfego alto")

    def test_alto_extremo(self):
        _, status = analisar_trafego(1000, 2000, 3000)
        self.assertEqual(status, "Tráfego alto")


if __name__ == "__main__":
    unittest.main(verbosity=2)
