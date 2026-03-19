from __future__ import annotations

import re
from pathlib import Path

import yaml


ENTREGA = Path("entrega/respuesta.md")
REGLAS = Path("rubrica/reglas.yaml")
SALIDA = Path("feedback.md")


def normalizar(texto: str) -> str:
    return texto.casefold()


def extraer_bloques(texto_md: str) -> list[tuple[str, str]]:
    patron = re.compile(
        r"\*\*Comando\*\*\s*```(?:[^\n]*)\n(.*?)\n```\s*"
        r"(?:\*\*Salida(?: del comando)?\*\*|\*\*Salida\*\*)\s*"
        r"```(?:[^\n]*)\n(.*?)\n```",
        re.DOTALL | re.IGNORECASE,
    )
    return [(cmd.strip(), out.strip()) for cmd, out in patron.findall(texto_md)]


def construir_mapa_bloques(bloques: list[tuple[str, str]]) -> dict[str, str]:
    return {normalizar(cmd): salida for cmd, salida in bloques}


def buscar_salidas_por_regla(textos_objetivo: list[str], mapa_bloques: dict[str, str]) -> str:
    salidas = []

    for texto_objetivo in textos_objetivo:
        objetivo = normalizar(texto_objetivo)

        if objetivo in mapa_bloques:
            salidas.append(mapa_bloques[objetivo])
            continue

        for comando, salida in mapa_bloques.items():
            if objetivo in comando or comando in objetivo:
                salidas.append(salida)
                break

    return "\n".join(salidas)


def evaluar_regla(regla: dict, mapa_bloques: dict[str, str]) -> tuple[bool, str]:
    textos = regla.get("textos", [])
    esperados = regla.get("contiene", [])

    salida = buscar_salidas_por_regla(textos, mapa_bloques)
    if not salida.strip():
        return False, "Incompleto"

    salida_norm = normalizar(salida)
    faltan = [item for item in esperados if normalizar(item) not in salida_norm]

    if faltan:
        return False, "Incompleto"

    return True, "Correcto"


def main() -> None:
    if not ENTREGA.exists():
        raise FileNotFoundError(f"No existe {ENTREGA}")

    if not REGLAS.exists():
        raise FileNotFoundError(f"No existe {REGLAS}")

    texto_md = ENTREGA.read_text(encoding="utf-8")
    reglas = yaml.safe_load(REGLAS.read_text(encoding="utf-8"))

    bloques = extraer_bloques(texto_md)
    mapa_bloques = construir_mapa_bloques(bloques)

    resultados: list[str] = []
    total = 0.0
    maximo = 0.0

    for nombre, regla in reglas["checks"].items():
        puntos = float(regla.get("puntos", 1))
        maximo += puntos

        ok, estado = evaluar_regla(regla, mapa_bloques)
        if ok:
            total += puntos
            resultados.append(f"✅ {nombre} (+{puntos})")
        else:
            resultados.append(f"❌ {nombre} (Incompleto)")

    nota_auto = round(total, 2)

    contenido = [
        "# Feedback automático",
        "",
        f"**Puntuación automática:** {nota_auto}/8",
        "",
        "## Detalle",
        "",
        *resultados,
        "",
    ]

    SALIDA.write_text("\n".join(contenido), encoding="utf-8")
    print("\n".join(contenido))


if __name__ == "__main__":
    main()
    main()
