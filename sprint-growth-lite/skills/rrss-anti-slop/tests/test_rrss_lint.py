import os, sys, tempfile, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import rrss_lint as r

def tipos(t):
    return {x["tipo"] for x in r.analizar(t)}

class T(unittest.TestCase):
    def test_cliche(self):
        self.assertIn("cliché", tipos("En el acelerado mundo de hoy necesitas descubrir el poder de tu marca"))
        self.assertIn("cliché", tipos("Unlock the power of your brand"))

    def test_voseo(self):
        for t in ("Vos sabés que funciona", "Mirá este reel", "Comprá la nueva colección", "Podés pedirlo hoy"):
            self.assertIn("voseo", tipos(t), t)

    def test_tuteo_ok(self):
        self.assertNotIn("voseo", tipos("Mira este reel. Puedes pedirlo hoy y sabes que llega en dos días."))

    def test_hashtags_emojis(self):
        t = r.analizar("#a #b #c #d #e #f #g " + "\U0001F600" * 7)
        self.assertIn("exceso de hashtags", {x["tipo"] for x in t})
        self.assertIn("exceso de emojis", {x["tipo"] for x in t})

    def test_clean(self):
        self.assertEqual(r.analizar("Tres errores al elegir un sofá: medir mal el espacio, ignorar la profundidad y no pedir muestras."), [])

    def test_exit_code_voseo(self):
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as f:
            f.write("Vos podés")
        self.assertEqual(r.main(["--archivo", f.name]), 1)
        self.assertEqual(r.main(["--archivo", "/no/existe"]), 2)

if __name__ == "__main__":
    unittest.main()
